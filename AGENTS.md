# AGENTS.md

## Common Rules

- 出力は日本語。
- 依頼範囲外の変更はしない。必要なら理由と影響を先に書く。
- 秘密情報をログ、コード、出力に書かない。
- push、merge、release 相当の操作は必ず人に確認する。

## Skill Authoring

- Skill を作成または更新するときは、先に `/Users/keisuke-yamasaki/.codex/skills/.system/skill-creator/SKILL.md` を読む。
- 新規 Skill は原則として Skill-Creator の `init_skill.py` で初期化し、完了時に `quick_validate.py` で検証する。
- `SKILL.md` の frontmatter は `name` と `description` だけにする。
- 発火条件は `description` に書く。本文だけに「いつ使うか」を置かない。
- 長い原則集や詳細例は `references/`、再利用する出力形式は `templates/`、発火検証は `evals/` に分ける。

## Software Design Work

- 実装へ飛ぶ前に、設計上の不確実性を列挙する。
- 設計判断は Evidence、Inference、Decision、Human confirmation に分ける。
- DDD、Clean Architecture、CQRS、Event Sourcing、microservices をプロジェクトが採用していない場合、勝手に前提化しない。
- Clean Architecture レビューは、ユーザーまたは repo が明示的に採用している場合だけ行う。
- 既存コードを変更する前に、責務、依存方向、テスト影響を確認する。
- 重要な設計判断は ADR または Design Memo として残す。
- 自動検出できることと、人間確認が必要なことを分ける。
- 書籍や設計原則を根拠にするときは、プロジェクト制約とのトレードオフを書く。
