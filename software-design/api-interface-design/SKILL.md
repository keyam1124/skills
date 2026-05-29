---
name: api-interface-design
description: >
  Use when designing or reviewing APIs, public interfaces, module contracts, backward compatibility, versioning, Hyrum Law risk, validation boundaries, DTO versus domain model separation, error responses, pagination, idempotency, or breaking-change impact.
---

# API Interface Design

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Shape stable APIs and module interfaces around explicit contracts.
- Separate external DTOs from internal domain models.
- Surface compatibility and Hyrum Law risks.

## Inputs to Inspect
- API specs, handlers, DTOs, clients, versioning docs, public exports, tests, and consumers if known
- Compatibility and migration constraints

## Workflow
1. Identify consumers, contract, and compatibility expectations.
2. Define input validation, output shape, errors, pagination, and idempotency.
3. Check whether domain model or persistence details leak through the interface.
4. Compare alternative contract shapes and migration costs.
5. Define contract tests or compatibility checks.

## Output Contract
- Contract proposal
- Validation boundary
- Error semantics
- Compatibility risks
- Alternatives
- Tests
- Human confirmation items

## Human Confirmation
- Breaking-change tolerance, public contract promises, and consumer migration windows.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `error-handling-design`
- `data-modeling-review`
- `test-strategy-for-design`
- `design-memo-writer`
