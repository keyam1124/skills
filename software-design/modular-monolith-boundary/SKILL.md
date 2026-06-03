---
name: modular-monolith-boundary
description: >
  Use when designing Modular Monolith module boundaries, module data ownership, public module APIs, internal package hiding, inter-module communication, shared kernel scope, and whether boundaries could later support service extraction or should remain in-process.
---

# Modular Monolith Boundary

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Design modules inside a monolith with clear ownership and APIs.
- Avoid premature microservice extraction.
- Define what is public, internal, shared, and owned by each module.

## Inputs to Inspect
- Feature/module map, data ownership, public APIs, internal packages, calls/events between modules, deployment constraints

## Workflow
1. Identify candidate modules and owned data.
2. Define public module API and hidden internals.
3. Classify shared kernel and integration points.
4. Check coupling, transaction needs, and future extraction pressure.
5. Recommend boundaries and tests/checks.

## Output Contract
- Module card
- Owned data
- Public API
- Internal implementation
- Inter-module communication
- Shared kernel
- Extraction risk
- Human confirmation items

## Human Confirmation
- Ownership, future deployment ambitions, and acceptable shared kernel scope.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `package-module-design`
- `bounded-context-design`
- `context-map-design`
- `dependency-direction-check`
