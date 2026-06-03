---
name: domain-service-vs-application-service
description: >
  Use when deciding whether logic belongs in Entity, Value Object, Domain Service, Application Service, Use Case, handler, controller, or orchestration code. Use when domain rules leak into application services or services become procedural god classes.
---

# Domain Service vs Application Service

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Separate business rules from orchestration and side effects.
- Move behavior to entities/value objects when possible.
- Avoid domain services that hide anemic domain models.

## Inputs to Inspect
- Service methods, use cases, entities, value objects, controllers, side effects, validators, and tests

## Workflow
1. List each behavior and whether it is a business rule, orchestration, IO, validation, or formatting.
2. Check whether the rule belongs on an entity or value object first.
3. Use Domain Service only for domain logic spanning objects without natural ownership.
4. Keep Application Service focused on orchestration and transaction boundaries.
5. Define tests at the domain or use-case level.

## Output Contract
- Behavior
- Current location
- Recommended owner
- Reason
- Refactor step
- Tests
- Human confirmation items

## Human Confirmation
- Meaning of business rules and acceptable service boundaries in the project.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `domain-building-blocks`
- `aggregate-design`
- `refactoring-planner`
