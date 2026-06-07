# Value Object Policy

## Evidence

- 既存の `ddd-when-to-wrap-primitives` は、Primitive Obsession と過剰なラップの両方を避け、コスト対効果で判断する方針を取っている。判断軸として、不変条件、取り違えリスク、ドメイン操作、複数値の不可分性、利用範囲を置く。
- Martin Fowler はValue Objectを、同一性ではなく値で等価判定される小さなオブジェクトとして扱い、MoneyやDateRangeのような複合値を例にしている。
- MicrosoftのDDD実装ガイドは、Value Objectの主要特性をidentityを持たないこととimmutableであることとして整理している。
- Alexis Kingの "Parse, don't validate" は、検証した事実を捨てず、型として保持して以後のコードに渡す考え方として境界parse方針に使える。
- Secure by DesignのDomain Primitiveは、不正確、曖昧、誤用されやすいコードを小さなドメイン型で固めることで、セキュリティ上の問題にも効くという文脈で使える。

## Decision

Value Objectは「プリミティブを全部包む」ためではなく、値の意味、不変条件、取り違えリスクを型に移すために導入する。

DDDのValue Objectに必ず豊富な振る舞いを持たせる、と硬く運用しすぎない。不変性、値による等価性、ドメイン上の意味がそろえばValue Object候補とし、振る舞いは自然に置ける場合だけ持たせる。

## Adoption Criteria

必ず導入する値:

- 金額+通貨
- 期間、日付範囲、予約枠
- メールアドレス、URL、電話番号など形式不正がバグになる入力
- 数量、単位付き数値、測定値
- 権限スコープ、認可対象、状態遷移に関わる値
- セキュリティ、決済、医療、法務、監査などの高リスク値

軽量に導入する値:

- `UserId`、`OrderId`、`AccountId` など同じプリミティブ型同士で取り違えやすいID
- 検証ロジックは薄いが、関数シグネチャ上の意味を強くしたい値
- migration中でフルValue Object化のコストが高いが、誤用防止の効果が高い値

原則プリミティブのままにする値:

- 一時変数、ループカウンタ、局所的な計算値
- 単なる表示文言、ログメッセージ、変換途中の作業用文字列
- 1つの関数内でしか使わず、不変条件もドメイン操作もない値
- 型変換のボイラープレートが、守りたい不変条件より大きい値

複合値としてまとめる値:

- `amount` と `currency`
- `startDate` と `endDate`
- `quantity` と `unit`
- `latitude` と `longitude`
- `scope` と `resource`

## Implementation Levels

Level 1: typed id、newtype、branded type

- 目的: 取り違え防止、意図の可視化。
- 条件: 不変条件は薄いが、同型引数の誤用が起きやすい。
- 例: `UserId`、`OrderId`、`TenantId`。

Level 2: smart constructor、factory、parser

- 目的: 無効値を作れないようにする。
- 条件: null、empty、形式、範囲、桁数、単位などの不変条件がある。
- 例: `EmailAddress.parse(raw)`、`Quantity.of(value, unit)`。

Level 3: 振る舞い付きValue Object

- 目的: 値に属するドメイン操作を集約する。
- 条件: 加算、比較、重複判定、包含判定、遷移可否などが自然に値へ属する。
- 例: `Money.add`、`DateRange.overlaps`、`PermissionScope.includes`。

## Interface Policy

- ドメイン層の関数やメソッドは、意味のある値をprimitiveではなくValue Objectまたはtyped idで受け取る。
- アプリケーション層はDTOからValue Objectを生成し、生成失敗を明示的なエラーとして扱う。
- HTTP API、DB schema、メッセージング、JSONでは安定したDTO/primitive表現を使い、アプリケーション層で相互変換する。
- コンストラクタは無効値を作れない形にする。直接生成を禁止できる言語ではprivate constructorとfactory/parserに寄せる。
- 永続化フレームワークの都合で完全な不変性が難しい場合でも、ドメインコードからは変更不能に見える設計にする。

## Test Plan

- 生成テスト: 正常値、境界値、不正値、null、empty、桁数、単位、範囲違反。
- 等価性テスト: 同じ値なら等価、異なる値なら非等価、hash/equalityの整合性。
- ドメイン操作テスト: `Money.add`、`DateRange.overlaps` などの成功ケースと失敗ケース。
- 境界変換テスト: DTO/API/DB値からのparse失敗が握りつぶされないこと。
- リグレッションテスト: 既存のプリミティブ引数取り違えがコンパイル時またはテストで検出されること。

## Source Links

- ddd-when-to-wrap-primitives: https://github.com/j5ik2o/ai-tools/blob/main/plugins/software-design/skills/ddd-when-to-wrap-primitives/SKILL.md
- Martin Fowler, PofEAA Value Object: https://martinfowler.com/eaaCatalog/valueObject.html
- Martin Fowler, Value Object bliki: https://martinfowler.com/bliki/ValueObject.html
- Microsoft, Implementing value objects: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/implement-value-objects
- Alexis King, Parse, don't validate: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/
- Secure by Design, Domain primitives: https://livebook.manning.com/book/secure-by-design/chapter-5/
