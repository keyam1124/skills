---
name: repository-design-and-placement
description: >
  Use when designing repositories: aggregate-root repositories, repository interface placement, ORM leakage, query read models, command repositories, save semantics, insert/update/upsert ambiguity, transaction ownership, and domain versus application layer boundaries.
---

# Repository Design and Placement

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Design repository contracts around aggregate or use-case needs.
- Prevent persistence and ORM types from leaking into domain logic.
- Clarify command/query split and transaction ownership.

## Inputs to Inspect
- Repository interfaces, implementations, ORM models, aggregate roots, use cases, queries, transactions, and tests

## Workflow
1. Identify whether the repository represents aggregate persistence, query access, or infrastructure gateway.
2. Define interface ownership and save semantics.
3. Check for ORM/data model leakage across boundaries.
4. Separate command repository from read model queries when needed.
5. Define transaction and tests.

## Output Contract
- Repository responsibility
- Placement
- Interface shape
- Save/query semantics
- Transaction owner
- Leakage risks
- Tests
- Human confirmation items

## Human Confirmation
- Persistence ownership, query performance requirements, and transaction boundaries.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `aggregate-design`
- `data-modeling-review`
- `ports-and-adapters-boundary`
- `clean-architecture-review`
