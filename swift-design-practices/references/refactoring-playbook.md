# Swift Refactoring Playbook

リファクタリングでは「動作を固定してから小さく変える」を優先する。

## Process

1. 変更前のふるまいを読む。UI、テスト、保存データ、公開API、既存バグの有無を区別する。
2. 可能なら先に characterization test を追加する。難しい場合は、既存テストや手動確認ポイントを明記する。
3. 1回の編集で1種類の改善だけ行う。rename、extract、move、behavior changeを混ぜない。
4. 各ステップでビルドまたは対象テストを回せる粒度にする。
5. 最後に差分を読み、設計改善が依頼範囲を超えていないか確認する。

## Common Moves

### Replace Primitive With Domain Type

Use when raw values carry domain rules.

- `String` ID -> small `struct` or typealias only if constraints are light.
- range-limited `Int` / `Double` -> initializer that validates range.
- status flags -> `enum`.
- loose tuple -> named `struct`.

### Replace Boolean State Matrix With Enum

Use when several Bool or Optional values represent one conceptual state.

- Identify valid states.
- Name each state from the user/domain perspective.
- Move derived flags to computed properties.
- Delete impossible combinations from call sites.

### Move Behavior To The Type That Owns The Rule

Use when the same branch is repeated.

- Put display-independent business decisions on domain types.
- Put UI wording and formatting in presentation helpers.
- Keep persistence conversion near the storage boundary.

### Extract Pure Function Before Extracting Service

Use when a method mixes calculation and side effects.

- Extract validation, formatting, filtering, sorting, or message composition as pure functions first.
- Add a service object only when external dependencies or shared orchestration justify it.
- Inject clock, UUID, persistence, notification, or clipboard dependencies only at the boundary that needs them.

### Split SwiftUI View By Responsibility

Use when a View is hard to read because it owns too many jobs.

- Extract subviews for repeated UI groups or independent input sections.
- Extract computed properties for readable conditional UI.
- Extract formatting and validation from `body`.
- Keep state ownership clear after splitting; do not pass large bags of Binding to hide coupling.

### Separate SwiftData Storage From Domain Rules

Use when persistence classes start to own app behavior.

- Keep SwiftData model fields close to what is stored.
- Map to domain values or helper types when enforcing invariants.
- Keep UI copy and sharing text outside the persistence model unless the model truly owns that language.

## Stop Conditions

Stop the refactor and report the boundary when:

- behavior change becomes necessary to continue,
- tests fail in a way unrelated to the intended refactor,
- the next step requires broad directory or architecture changes not requested,
- the code smell is real but outside the touched workflow,
- the repo's existing pattern intentionally differs from the generic best practice.

## Review Checklist

- Can a future reader explain where the rule lives?
- Did the refactor remove an impossible state, duplicate rule, hidden side effect, or oversized responsibility?
- Did test coverage move closer to user-visible behavior?
- Are new abstractions named after domain responsibilities rather than implementation mechanics?
- Is there a clear reason for any new Protocol, Service, ViewModel, or shared helper?
