---
name: cross-aggregate-consistency
description: >
  Use when designing consistency across aggregates, such as stock and order, payment and order confirmation, user deletion and related data, strong consistency versus eventual consistency, compensating actions, corrective policies, or cross-aggregate invariants.
---

# Cross Aggregate Consistency

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Clarify whether a cross-aggregate rule is a true invariant or a policy.
- Design compensation and recovery where atomic consistency is not justified.
- Expose high-risk human decisions.

## Inputs to Inspect
- Affected aggregates, business rules, failure cases, timing expectations, events, processes, and data ownership

## Workflow
1. State the cross-aggregate rule and business impact if violated.
2. Classify as invariant, policy, reporting constraint, or operational cleanup.
3. Compare merge aggregates, transaction coordination, events, saga, process manager, and compensation.
4. Define monitoring and reconciliation if eventual.
5. List human confirmations.

## Output Contract
- Constraint
- Classification
- Consistency option
- Compensation/reconciliation
- Failure modes
- Tests/monitoring
- Human confirmation items

## Human Confirmation
- Business tolerance for temporary inconsistency and compensation semantics.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `aggregate-design`
- `aggregate-transaction-boundary`
- `domain-event-design`
- `distributed-consistency-review`
