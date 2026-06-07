# Refactoring Patterns

## Pattern Matrix

| Symptom | Prefer | Avoid |
| --- | --- | --- |
| One branch is the only valid domain case | Remove the invalid state from construction and parsing | Keep `if flag` with a dead `else` |
| Repeated `switch kind` decides behavior | Move behavior to each kind or to a closed variant type | Add another helper with the same switch |
| New variants should be added by plugins or outside modules | Strategy, State, Policy, command handler | Closed enum that every extension must edit |
| Variants are fixed by the domain | Sealed type, enum with behavior, ADT, exhaustive match | Open registry that hides missing cases |
| Same collection filters/calculations repeat | First Class Collection with domain-named methods | Raw list traversal in callers |
| A shared utility grows flags | Split by intention and change reason | Keep DRY by adding more booleans |

## Replace Boolean With Domain State

Before:

```text
if inTargetState {
  buildMessage()
} else {
  // unreachable or unsupported
}
```

After:

```text
state = DomainState.current(...)
state.buildMessage()
```

If the non-target state is not supported by the product, remove it from the domain model. If it can arrive from storage or outside input, parse it into an error, migration path, or explicit external-data state before business logic runs.

## Replace Type Code With Polymorphic Behavior

Before:

```text
switch memo.kind:
  case bringItem: title = bringItemTitle(memo)
  case temperature: title = temperatureTitle(memo)
  case unknown: title = fallbackTitle(memo)
```

After:

```text
memo.title()
```

Possible implementations:

- Object-oriented: each subtype implements `title`.
- Functional: each ADT case carries only valid fields, and an exhaustive match lives in one module.
- Data-oriented: a table maps each known variant to a named behavior object, and missing mappings fail at startup or compile time.

## Boundary Mapping

Keep persistence and transport representations separate from domain behavior.

```text
rawKind -> parse -> DomainMemoKind -> behavior
```

Do not let `rawKind` or `unknown` flow through UI, validation, date rules, or domain services unless the user-facing behavior for unknown input is explicitly specified.

## Characterization Tests

Before refactoring, write tests from the branch table:

- one case for each existing variant and behavior column;
- one case for unsupported or migrated raw input if it can appear;
- one regression test proving a newly added variant cannot silently hit a default branch.

After refactoring, the same table should be represented by type-level exhaustiveness, variant-specific tests, or contract tests for each strategy/state object.

## Review Heuristics

- Prefer behavior names over type names: `scheduleDate()` is better than `handleKind()`.
- Prefer domain verbs over framework verbs: `requestFamilyToBring()` is better than `buildSentRecordForBringItem()`.
- Keep DTOs simple, but do not copy DTO-style getters into domain models.
- Do not introduce polymorphism for a local, stable, two-line display branch unless it removes a real duplicated decision or invalid state.
