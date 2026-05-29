---
name: package-module-design
description: >
  Use when designing or reviewing package, module, folder, namespace, feature, or library boundaries. Use for dependency cycles, co-change across packages, information hiding, public API leakage, shared module bloat, framework imports in domain modules, or package refactoring plans.
---

# Package Module Design

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Improve package and module boundaries based on change reasons and ownership.
- Expose hidden coupling and public API leakage.
- Avoid large directory reshuffles without behavior protection.

## Inputs to Inspect
- Package layout, imports, public exports, tests, git co-change clues, and build boundaries
- Domain and feature ownership if known

## Workflow
1. Identify current modules and their intended responsibilities.
2. Look for cycles, shared buckets, leaky public APIs, and framework dependencies in inner modules.
3. Group files by reason-to-change and collaboration frequency.
4. Define proposed boundaries and migration order.
5. Name tests or architecture checks to protect the split.

## Output Contract
- Current module map
- Boundary problems
- Evidence
- Proposed module API
- Migration steps
- Tests or checks
- Human confirmation items

## Human Confirmation
- Ownership boundaries, acceptable churn, and whether public API breakage is allowed.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `dependency-direction-check`
- `information-hiding-deep-modules`
- `modular-monolith-boundary`
- `refactoring-planner`
