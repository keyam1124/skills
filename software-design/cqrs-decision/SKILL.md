---
name: cqrs-decision
description: >
  Use when deciding whether to adopt CQRS or split command and query models. Use for read model design, write model design, projection, stale-read tolerance, reporting needs, eventual consistency, query optimization, or when CQRS complexity may or may not be justified.
---

# CQRS Decision

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Evaluate CQRS as a trade-off, not a default pattern.
- Clarify command model, query model, projection, and staleness expectations.
- Reject CQRS when simpler read paths are enough.

## Inputs to Inspect
- Read/write use cases, query complexity, performance needs, consistency tolerance, reporting needs, current model pain
- Operational capacity for projections and rebuilding

## Workflow
1. Identify whether command and query needs genuinely diverge.
2. Estimate projection, staleness, rebuild, and debugging costs.
3. Compare simple query optimization, read replicas, materialized views, and CQRS.
4. Define minimal CQRS boundary if adopted.
5. List tests and operational checks.

## Output Contract
- 採用判断
- Command model
- Query model
- Consistency expectations
- Projection cost
- Alternatives
- Tests
- Human confirmation items

## Human Confirmation
- Stale-read tolerance, reporting priorities, and operational appetite for projections.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `event-sourcing-decision`
- `data-modeling-review`
- `distributed-consistency-review`
- `test-strategy-for-design`
