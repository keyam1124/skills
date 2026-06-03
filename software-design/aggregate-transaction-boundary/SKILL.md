---
name: aggregate-transaction-boundary
description: >
  Use when reviewing aggregate transaction boundaries, one transaction one aggregate rules, locking, strong consistency, eventual consistency, sagas, process managers, database constraints, or whether multiple aggregate updates should be split.
---

# Aggregate Transaction Boundary

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Evaluate consistency and transaction boundaries around aggregates.
- Challenge multi-aggregate transactions unless strong consistency is justified.
- Identify eventual consistency, saga, or corrective policy alternatives.

## Inputs to Inspect
- Transaction code, repositories, aggregate candidates, invariants, failure modes, concurrency risks, and DB constraints

## Workflow
1. List data changed in each transaction.
2. Map each changed object to aggregate candidate.
3. Identify invariants requiring atomic enforcement.
4. Compare strong consistency, eventual consistency, DB constraint, saga, or process manager approaches.
5. Define tests for concurrency and failure paths.

## Output Contract
- Transaction boundary
- Aggregates touched
- Strong consistency rationale
- Eventual consistency alternatives
- Saga/process manager need
- Tests
- Human confirmation items

## Human Confirmation
- Acceptable inconsistency window, business failure tolerance, and operational recovery policy.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `aggregate-design`
- `cross-aggregate-consistency`
- `distributed-consistency-review`
