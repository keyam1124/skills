---
name: architecture-drift-review
description: >
  Use when comparing ADRs, design notes, architecture docs, or earlier design intent with the current implementation to detect drift. Use for prompts about whether Clean Architecture, bounded contexts, dependency rules, repository boundaries, gateways, or module ownership have diverged from documented decisions.
---

# Architecture Drift Review

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Compare documented intent with current code behavior.
- Separate intentional evolution from accidental erosion.
- Recommend whether to update docs, repair code, or record a new decision.

## Inputs to Inspect
- ADRs, design memos, architecture docs, README, diagrams
- Current code, package layout, imports, tests, and runtime boundaries
- Change history if relevant and available

## Workflow
1. Extract original design decisions and constraints.
2. Inspect current implementation evidence.
3. Map each divergence to impact and likely intent.
4. Classify as acceptable evolution, documentation drift, or implementation drift.
5. Recommend ADR update, design memo, code repair, or follow-up investigation.

## Output Contract
- 元の設計判断
- 現在の実装
- 乖離している箇所
- 意図的変更か偶発的劣化か
- ADR更新かコード修正か
- 人間確認事項

## Human Confirmation
- Whether drift reflects a valid product or team decision and whether backward compatibility matters.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `adr-writer`
- `design-memo-writer`
- `dependency-direction-check`
- `clean-architecture-review`
