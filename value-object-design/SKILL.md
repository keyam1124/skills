---
name: value-object-design
description: Language-agnostic guidance for deciding whether primitive values should become Value Objects, typed IDs, newtypes, branded types, smart constructors, domain primitives, or remain primitives. Use when implementing, refactoring, or reviewing domain models, APIs, DTO boundaries, Primitive Obsession, String/Int IDs, Money, DateRange, Email, URL, quantity/unit, permission scope, state-transition values, or boundary parsing decisions.
---

# Value Object Design

Value Objectはプリミティブを全部包むためではなく、値の意味、不変条件、取り違えリスクを型へ移すために導入する。

## Workflow

1. 候補値と境界を列挙する。
   - API入力、DB読み出し、外部サービス応答、画面入力、コマンド引数、既存ドメイン関数の引数を確認する。
   - 同じプリミティブ型の引数、重複 validation、`amount` + `currency` のような分離された複合値、raw string enum、単位付き数値を探す。
2. 導入理由を分類する。
   - 不変条件: 無効値を作れると業務不整合、セキュリティ事故、境界バグにつながるか。
   - 取り違えリスク: `UserId` と `OrderId` のように同じプリミティブ同士で誤用しやすいか。
   - 複数値の不可分性: 金額と通貨、開始日と終了日など、別々に持つと不整合が生まれるか。
   - ドメイン操作: 加算、比較、重複判定、包含判定、状態遷移判定などを自然に集約できるか。
   - 利用範囲: 複数モジュール、複数レイヤー、複数ユースケースで同じ意味として使うか。
3. 最軽量の表現を選ぶ。
   - 取り違え防止だけなら typed id、newtype、branded type を優先する。
   - 不変条件があるなら smart constructor、factory、parser で無効値を作れない形にする。
   - 不変条件とドメイン操作が自然に集まるなら、振る舞い付きValue Objectにする。
   - 不変条件も取り違えリスクもドメイン操作もない局所値はプリミティブのままにする。
4. 境界でparseする。
   - API、DB、JSON、メッセージング、外部サービスでは安定したDTOまたはprimitive表現を保つ。
   - アプリケーション層でDTOからValue Objectやtyped idへ変換し、失敗を明示的なエラーとして扱う。
   - ドメイン内部では妥当性確認済みの型だけを受け渡す。
5. 実装前に依存方向と移行単位を決める。
   - 既存アーキテクチャを優先し、Value Objectのためだけに新しい層やDDD構造を導入しない。
   - 永続化やシリアライズ都合の可変性が必要でも、ドメインコードからは変更不能に見えるようにする。
   - 既存APIやDB schemaへValue Objectを直接漏らしすぎない。
6. テストで不変条件と境界変換を固定する。
   - 生成、等価性、hash/equality、境界変換、ドメイン操作、取り違え regression を確認する。

## Decision Rules

- 必ず導入する: 金額+通貨、期間、メールアドレス、URL、数量、単位付き数値、権限スコープ、状態遷移に関わる値など、無効値や取り違えが重大な不整合に直結する値。
- 軽量に導入する: `UserId`、`OrderId` など、検証ロジックは薄いが同じプリミティブ型同士で取り違えやすいID。
- 原則プリミティブのままにする: 一時変数、ループカウンタ、単なる表示文言、局所的に1回しか使わない値、不変条件もドメイン操作もない名前文字列。
- 複合値はValue Object化を優先する: `amount` と `currency`、`startDate` と `endDate` のように、別々に持つと不整合が生まれる値。

## Review Output

設計相談、レビュー、実装報告では次を分けて短く書く。

- Evidence: コード上の重複validation、同型引数、不正状態、境界変換、既存テスト、外部根拠。
- Inference: どの値が誤用されやすいか、どの不変条件を型で保持できるか、どの境界にparseを置くべきか。
- Decision: primitive、typed id/newtype/branded type、smart constructor、振る舞い付きValue Object のどれを選ぶか。
- Human confirmation: 仕様不明な範囲、互換性判断、DB/API schema変更、導入コストの許容度。

## References

詳細な判断基準、根拠URL、interface方針、テスト計画が必要な場合は `references/value-object-policy.md` を読む。
