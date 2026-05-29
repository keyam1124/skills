---
name: aggregate-design
description: >
  Use when designing or reviewing DDD Aggregates, aggregate boundaries, invariants, aggregate root access, transaction consistency, cross-aggregate references, eventual consistency, domain events, or aggregate refactoring. Use for Japanese prompts mentioning 集約, 集約境界, 不変条件, トランザクション境界, or 結果整合性.
---

# Aggregate Design

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Design aggregates as consistency boundaries, not table groups.
- Make invariants, commands, events, and corrective policies explicit.
- Surface transaction and cross-aggregate questions for human confirmation.

## Inputs to Inspect
- Business invariants, commands, events, lifecycle, and conflict frequency
- Current entities, tables, repositories, services, and transactions
- Known consistency requirements and user-visible failure modes

## Workflow
1. Name the aggregate and its responsibility.
2. List lifecycle states, commands, and events.
3. Separate true invariants from policies that can be corrected later.
4. Check references to other aggregates and transaction boundaries.
5. Compare boundary alternatives and fill templates/aggregate-design-canvas.md.

## Bundled Resources
- `templates/aggregate-design-canvas.md`

## Output Contract
- Aggregate name
- Responsibility
- Lifecycle and state transitions
- Enforced invariants
- Corrective policies
- Commands handled
- Events created
- Throughput and conflict risk
- Boundary alternatives
- Human confirmation items

## Human Confirmation
- Which invariants are truly mandatory, acceptable eventual consistency, and operational tolerance for conflicts.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `aggregate-transaction-boundary`
- `cross-aggregate-consistency`
- `repository-design-and-placement`
- `domain-event-design`
