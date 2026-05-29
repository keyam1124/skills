---
name: domain-primitive-design
description: >
  Use when explicitly invoked or routed to replace primitive obsession with domain primitives or value objects such as Email, Money, Quantity, DateRange, UserId, OrderId, status, typed IDs, parse dont validate boundaries, and always-valid domain modeling.
---

# Domain Primitive Design

Software Design Skill System の一部として、設計判断を evidence-driven に進める。
通常は `software-design-router` または領域hubから呼び出す。明示的に `$domain-primitive-design` と指定された場合も使う。

## Scope
- Make invalid states harder to represent with typed values.
- Separate parsing/validation at boundaries from always-valid domain objects.
- Avoid wrapping primitives without domain behavior or constraints.

## Inputs to Inspect
- Primitive fields, validators, parsing code, domain constraints, API/DB boundaries, and tests

## Workflow
1. Find primitives carrying domain meaning or constraints.
2. Define invariant and construction boundary.
3. Choose value object, typed ID, enum/tagged union, or leave primitive.
4. Plan parsing from external inputs separately from internal domain use.
5. Add tests for valid, invalid, equality, formatting, and serialization behavior.

## Output Contract
- Primitive smell
- Proposed domain primitive
- Invariant
- Construction/parsing boundary
- Serialization notes
- Tests
- Human confirmation items

## Human Confirmation
- Exact business constraints, formatting rules, and compatibility of wire/storage formats.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `domain-building-blocks`
- `api-interface-design`
- `test-strategy-for-design`
