---
name: clean-architecture-review
description: >
  Use only when the project explicitly adopts Clean Architecture or the user explicitly asks for Clean Architecture review. Review dependency rule, use cases, entities, interface adapters, gateways, repository implementations, framework boundaries, and layer violations. Do not use for generic architecture advice, Hexagonal Architecture, Onion Architecture, or general DDD review.
---

# Clean Architecture Review

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Review Clean Architecture compliance only when Clean Architecture is explicit.
- Check dependency rule and boundary placement without style evangelism.
- Recommend local repairs that preserve behavior.

## Inputs to Inspect
- Architecture docs, layer names, module layout, imports, use cases, controllers, presenters, gateways, and repository implementations
- Tests and examples that show intended boundaries

## Workflow
1. Confirm the project explicitly claims Clean Architecture or the user asked for it.
2. Identify entities, use cases, interface adapters, frameworks, and external details.
3. Check dependency direction and data shape crossing boundaries.
4. Find framework, ORM, SDK, or UI leaks into inner layers.
5. Recommend minimal repairs and tests.

## Output Contract
- Layer mapping
- Dependency rule findings
- Boundary leaks
- Impact
- Repair proposal
- Tests
- Human confirmation items

## Human Confirmation
- Whether current deviations are intentional and whether the project still wants Clean Architecture as a constraint.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `architecture-style-decision`
- `ports-and-adapters-boundary`
- `dependency-direction-check`
- `codebase-design-audit`
