---
name: swift-design-practices
description: Swift code design guidance for implementation, refactoring, and review. Use when Codex edits or evaluates Swift, SwiftUI, or SwiftData code and should check domain modeling, value objects, type safety, dependencies, state ownership, error handling, concurrency, testability, naming, file/type size, and behavior-preserving refactoring risks.
---

# Swift Design Practices

Swiftの実装・リファクタリング時に、動作を守りながら設計の歪みを小さくするためのSkill。

## Workflow

1. 依頼範囲、対象ファイル、既存テスト、周辺の命名・分割・状態管理の流儀を先に読む。
2. Swiftファイルが多い場合は `scripts/swift_design_scan.py <repo-or-dir>` を実行し、候補を拾う。出力は設計判断の入口であり、機械的な修正理由にしない。
3. 実装・レビューでは `references/swift-design-checklist.md` を必要箇所だけ読む。
4. リファクタリング依頼では `references/refactoring-playbook.md` を読み、ふるまいを固定してから小さく変える。
5. 変更後は、影響範囲に合うテスト、`swift test`、`xcodebuild test`、既存検証スクリプトのいずれかを実行する。実行できない場合は理由を明記する。

## Design Gate

実装前と完了前に次を確認する。

- ドメインの不正状態を `String`、`Int`、`Bool`、Optional の組み合わせだけで表していないか。
- 変更の中心ロジックがSwiftUI View、SwiftData Model、永続化、通信、日付・時刻、通知などの外部事情に埋もれていないか。
- 値の検証、変換、表示文言生成、状態遷移が複数箇所に重複していないか。
- `force unwrap`、`try!`、`as!`、隠れたグローバル状態、巨大な `body`、巨大な型を増やしていないか。
- テストしにくい副作用を直接呼ばず、境界で注入・分離できているか。
- 抽象化の名前が実際の責務を説明しているか。パターン名や汎用名で責務を隠していないか。

## Implementation Rules

- 既存アーキテクチャを優先する。新しい層、Protocol、Service、ViewModelは、責務分離またはテスト容易性が明確に改善する場合だけ追加する。
- 小さな変更では、局所的な型・関数・テスト追加を優先する。広域リネームやディレクトリ再編は、依頼範囲に含まれる場合だけ行う。
- SwiftUIでは、Viewを単に短くするためだけに分割しない。状態所有、表示部品、入力部品、純粋な整形処理など、理由のある境界で分ける。
- SwiftDataや永続化モデルにUI表示ロジックを寄せない。保存形式、ドメイン規則、表示整形を混ぜない。
- 設計改善で動作が変わる可能性がある場合は、先にテストまたは現状確認を置く。

## Review Output

レビューや実装後の説明では、重要な順に短く書く。

- 変更した設計境界
- 残したリスクまたは意図的に触らなかった箇所
- 実行した検証
- 追加で見るべきテストや次のリファクタ候補
