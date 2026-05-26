---
name: polymorphic-branch-refactoring
description: 実装・リファクタリングで、同じBool、enum、種別、モード条件に基づくif/switch/match/whenが複数のプロパティ、UI、サービス、validator、formatterに重複しているとき、言語に応じたInterface、Protocol、trait、abstract base classなどとStrategy実装へ振る舞いを集約し、条件分岐の重複、関心混在、修正漏れリスクを下げる設計支援。Use when adding a new mode, replacing flags such as isHospital, reviewing repeated conditional logic, or separating mode-specific data and behavior.
---

# Polymorphic Branch Refactoring

同じ条件に基づく分岐が散らばっている場合に、多態性とStrategyで振る舞いを分離する。特定言語の機能名に引きずられず、対象言語の自然な抽象化手段を選ぶ。

## Vocabulary

- **Interface**: SwiftのProtocol、TypeScript/Kotlin/Java/C#のinterface、Rustのtrait、PythonのABCまたはduck typing、Haskell系のtypeclassなど、呼び出し側が依存する共通契約。
- **Strategy**: モード、種別、状態ごとの具体実装。表示データ、計算、入力可否、検証規則、導線など、同じ条件に属する振る舞いを持つ。
- **Selection boundary**: 既存のBool、enum、DB値、設定値、ドメイン状態からStrategyを選ぶ境界。分岐を残すなら原則ここだけに集約する。

## Core Rule

同じ条件で複数箇所の値や振る舞いを切り替えている場合は、条件分岐を呼び出し側へ広げない。モードごとのデータとロジックをStrategyに閉じ込め、呼び出し側は共通Interfaceだけを見る形へ寄せる。

特に次の形を見つけたら、Strategy化を優先して検討する。

- `isHospital ? ... : ...` がtitle、subtitle、lead、buttonLabelなど複数プロパティに出ている。
- 同じenum、tag、type、stateの`switch`や`match`がUI、service、formatter、validatorに重複している。
- 新しい状態を追加すると複数ファイルの分岐更新が必要になる。
- 表示文言、入力可否、遷移先、検証規則など、同じモードに属する仕様が別々の場所に散らばっている。

## Workflow

1. 重複している条件を探す。条件名、分岐先の値、分岐が現れるファイル、追加モード時に変更が必要な箇所を確認する。
2. 分岐ごとに変わるものを列挙する。表示文字列、入力制約、導線、計算、永続化値、通知文言などを混ぜずに分類する。
3. 呼び出し側が本当に必要とする共通の面だけをInterfaceにする。Interfaceには「全モードが提供すべき振る舞い」だけを置く。
4. 各モードを独立したStrategy実装にする。関連するデータとロジックを同じ実装単位に置き、モード固有の判断を外へ漏らさない。
5. 条件からStrategyを選ぶ箇所を1箇所に集約する。Factory、constructor、composition root、dependency injection、handler生成時など、既存構造に合う境界を選ぶ。
6. 呼び出し側をInterface利用へ置き換える。UIやserviceから`if isHospital`や重複`switch`を消す。
7. 新しいモード追加の手順を確認する。既存呼び出し側を触らずに新しい具象型を追加できるかを見る。
8. 既存テスト、スナップショット、UI確認、contract test、または最小のユニットテストで、各モードの出力と遷移が変わっていないことを確認する。

## General Shape

分岐が散っている状態：

```text
title    = isHospital ? "入院中" : "通常時"
subtitle = isHospital ? "病院での予定" : "自宅での予定"
homeLead = isHospital ? "病棟で確認すること" : "家で確認すること"
```

Strategy化した状態：

```text
interface CareContextStrategy {
    title
    subtitle
    homeLead
}

HospitalCareContextStrategy implements CareContextStrategy {
    title = "入院中"
    subtitle = "病院での予定"
    homeLead = "病棟で確認すること"
}

HomeCareContextStrategy implements CareContextStrategy {
    title = "通常時"
    subtitle = "自宅での予定"
    homeLead = "家で確認すること"
}
```

選択境界は1箇所に置く：

```text
makeCareContextStrategy(contextState) -> CareContextStrategy {
    if contextState.isHospital {
        return HospitalCareContextStrategy()
    }
    return HomeCareContextStrategy()
}
```

呼び出し側は条件を知らない：

```text
renderCareHome(strategy: CareContextStrategy) {
    renderText(strategy.title)
    renderText(strategy.subtitle)
    renderText(strategy.homeLead)
}
```

## Language Mapping

- Swift: `protocol` + `struct`/`class` + `any Protocol`またはgenerics。
- TypeScript: `interface` + object/class implementation。UI propsやservice引数にinterfaceを渡す。
- Kotlin/Java/C#: `interface`または`abstract class` + concrete class。DI containerやfactoryで選択する。
- Rust: `trait` + concrete type。動的ディスパッチが必要なら`dyn Trait`、静的で足りるならgenericsを使う。
- Python: `abc.ABC`、`Protocol`、またはduck typing。規模が小さい場合は関数オブジェクトやdataclassでもよい。
- 関数型寄りの環境: typeclass、record of functions、module signatureなど、呼び出し側が共通契約だけを見る形を選ぶ。

## Design Checks

- Interface名は`ModeInterface`のような抽象名にせず、呼び出し側に提供する責務で名付ける。
- Interfaceを巨大にしない。全モードで不要な値が混ざるなら、責務を分けるか、呼び出し側の境界を見直す。
- `Bool`のまま広げない。`isHospital`のようなフラグは、Strategy選択境界の入力に閉じ込める。
- 具象型同士で重複する実装が増えたら、共通helperや既存ドメイン型へ寄せる。ただし、共通化でモード固有の意味を隠さない。
- UI、handler、controller、application serviceにモード固有の表示仕様や業務分岐を埋め込まない。呼び出し側はStrategyを使うだけに近づける。
- 永続化モデルに表示文言や画面導線を持たせない。保存形式、ドメイン規則、表示整形を混ぜない。
- enumやsealed classを使う場合でも、同じswitch/matchを複数箇所へ複製しない。単一のStrategy生成境界、visitor、またはenum内の単一責務メソッドへ集約する。

## Do Not Over-Abstract

次の場合は、Interface/Strategy化より局所的な整理を優先してよい。

- 分岐が1箇所だけで、追加モードの見込みも低く、周辺へ漏れていない。
- enum、sealed class、tagged unionが閉じたドメイン状態を表し、分岐が1箇所に集約されている。
- Interfaceを導入すると、責務よりも配線、type erasure、依存注入の複雑さが目立つ。
- まずテストで現状を固定すべき大きな変更で、設計変更と挙動変更が混ざる危険が高い。

ただし、同じ条件分岐が複数の値やメソッドに重複している場合は、単純化を理由に放置しない。修正漏れが起きる構造を先に解消する。

## Review Output

レビューでは、重要度順に短く書く。

- 重複している条件分岐と、それが追加モード時に壊れる理由
- 推奨するInterface、具象Strategy、Strategy選択境界
- 触るべき呼び出し側と、触らずに済むようになる箇所
- テストまたは確認すべきモード別の出力
