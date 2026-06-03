---
name: data-modeling-review
description: >
  Use when reviewing how domain models connect to RDB schemas, document models, event schemas, read models, indexes, data ownership, migrations, consistency, reporting requirements, and persistence shapes without letting storage structure dictate the domain model.
---

# Data Modeling Review

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Review persistence and read models against domain ownership and use cases.
- Separate domain model, storage model, event schema, and read model.
- Surface migration and reporting implications.

## Inputs to Inspect
- Domain model, tables, documents, events, read models, indexes, migrations, queries, reports, and ownership docs

## Workflow
1. Identify each model and its purpose.
2. Check ownership, normalization/denormalization, indexes, and migration risks.
3. Find domain/storage leakage and reporting-driven distortions.
4. Compare alternatives for read/write and history needs.
5. Define tests and migration checks.

## Output Contract
- Model type
- Ownership
- Mismatch or leakage
- Query/report needs
- Migration risk
- Recommendation
- Tests
- Human confirmation items

## Human Confirmation
- Reporting priorities, migration downtime, retention, and data ownership.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `repository-design-and-placement`
- `api-interface-design`
- `cqrs-decision`
- `event-sourcing-decision`
