---
name: polymorphic-conditional-refactoring
description: Language-agnostic design and refactoring guidance for replacing repeated conditionals over mode, kind, status, type, role, feature flag, or boolean state with responsibility-bearing models. Use when code review, implementation, or refactoring finds if/switch/match chains, enum dispatch, type-code branching, boolean branches where only one case is valid, duplicated condition matrices, Feature Envy, Tell Don't Ask violations, or classes whose structure is driven by flags instead of domain behavior.
---

# Polymorphic Conditional Refactoring

条件分岐を消すこと自体を目的にせず、分岐軸が表すドメイン責務を特定し、その責務を型、オブジェクト、関数、または代数的データ型へ移す。

## Workflow

1. 対象コードの分岐軸を列挙する。
   - `mode`、`kind`、`status`、`type`、`role`、boolean flag、nullable state、raw string enum を探す。
   - 同じ軸で分岐している呼び出し元、UI、永続化、バリデーション、表示文言、日付処理、共有文生成を横断的に検索する。
2. 分岐表を作る。
   - 行を variant、列を振る舞いにして、各セルに現在の処理を書く。
   - 片方の branch が到達不能、仕様外、常に同じ結果なら、その branch ではなく分岐軸そのものを疑う。
3. 分岐を分類する。
   - 不可能な状態: branch を削るだけでなく、その状態を作れないモデルにする。
   - variant ごとの振る舞い: variant 側へ処理を移す。
   - 外部境界の都合: raw value、DTO、DB schema 変換層に閉じ込める。
   - 横断的な policy: Strategy、Policy、State、Rule など目的名の型へ分離する。
   - 単なる表示・ログ: 過剰な抽象化を避け、読みやすい局所分岐を許容する。
4. 置換パターンを選ぶ。
   - variant 集合が閉じているなら、sealed type、enum with behavior、ADT、sum type、pattern matching の網羅性を使う。
   - variant 集合が拡張されるなら、interface、protocol、trait、Strategy、State、command handler を使う。
   - 分岐がコレクション操作に散在するなら、First Class Collection に集約する。
   - 同形コードの共通化で flag が増えているなら、字面ではなく意図で分け直す。
5. 小さく移行する。
   - 先に現状の振る舞いを characterization test、snapshot、分岐表ベースのテストで固定する。
   - raw enum や flag をすぐ消せない場合は、境界で domain variant に parse して以降は domain variant だけを渡す。
   - 1つの軸を直したら、同じ軸の分岐が残っていないか再検索する。
6. 完了前に設計を検査する。
   - 呼び出し側が `if variant == X` と聞いてから処理していないか。
   - 新しい variant を追加したとき、変更箇所が1つの型または網羅性エラーに集まるか。
   - 不可能な branch、default branch、unknown fallback が仕様外の状態を隠していないか。
   - 抽象化名が `Handler`、`Manager`、`Processor` だけでなく、実際の目的を説明しているか。

## Detection

次を見つけたら、ポリモーフィズム的な解決を検討する。

- 同じ `if`、`switch`、`match`、`case` が複数ファイルにある。
- `kind` や `status` ごとに title、date、validation、permission、serialization が別々の場所で分岐している。
- boolean flag の false 側が仕様上存在しない、または空実装・fallback だけになっている。
- 共通関数に `isX`、`mode`、`type`、`includeY` の引数が増え続けている。
- 呼び出し側が対象の状態を取得し、その値で判断してから対象を更新している。
- `default`、`unknown`、`else` が、本来追加 variant のコンパイルエラーやテスト失敗で気づくべき変更を飲み込んでいる。

## Refactoring Rules

- 分岐先の処理が対象 variant の責務なら、呼び出し側ではなく variant に命じる。
- 到達不能 branch は「コメントで使わない」ではなく、コンストラクタ、型、schema、parse 境界、初期値で作れないようにする。
- raw string、数値 type-code、DB enum は永続化境界の表現として扱い、ドメイン処理へ直接流さない。
- `Unknown` は外部入力の parse 結果としては許容するが、通常の業務処理 variant と同列に扱わない。
- 継承を前提にしない。言語や既存設計に合わせて、interface、trait、protocol、record + function、sealed ADT、enum method、dispatch table を選ぶ。
- 共通化は意図が同じ場合だけ行う。同じ式に見えても、変更理由が違うなら別の型や関数として残す。
- 抽象化で条件分岐を隠すだけの `process(type, data)` や巨大な handler registry を作らない。

## Output Shape

レビューや実装報告では、次を短く明記する。

- 分岐軸: どの `mode`、`kind`、`status`、type-code、flag を扱ったか。
- 判断: 削除した不可能状態、内部化した振る舞い、境界に残した raw 表現。
- 設計: 閉じた variant、開いた Strategy/State、First Class Collection など、選んだ形と理由。
- 検証: 固定した振る舞い、追加した分岐表テスト、残したリスク。

## References

より具体的な置換パターンと疑似コードは `references/refactoring-patterns.md` を読む。
