---
name: event-sourcing-decision
description: >
  Use when deciding whether to adopt Event Sourcing, designing event streams, event schema evolution, rehydration, snapshots, projections, auditability, temporal queries, projection rebuilds, idempotency, migration, or when event sourcing complexity may be unjustified.
---

# Event Sourcing Decision

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Evaluate Event Sourcing based on concrete business and audit needs.
- Expose operational complexity before adoption.
- Separate domain events, integration events, and stored event facts.

## Inputs to Inspect
- Audit and temporal query requirements, current state model, event candidates, retention needs, schema evolution expectations
- Projection and rebuild capacity

## Workflow
1. Identify the business reason for storing events as source of truth.
2. Compare CRUD plus audit log, append-only history, and Event Sourcing.
3. Assess schema evolution, replay, snapshots, idempotency, and debugging cost.
4. Define event stream boundaries if adopted.
5. List migration and operational risks.

## Output Contract
- 採用判断
- Event stream candidates
- Event schema risks
- Projection model
- Operational costs
- Alternatives
- Human confirmation items

## Human Confirmation
- Audit/legal needs, replay value, operational complexity tolerance, and migration budget.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `cqrs-decision`
- `domain-event-design`
- `distributed-consistency-review`
- `observability-operability-review`
