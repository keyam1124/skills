---
name: ports-and-adapters-boundary
description: >
  Use when reviewing Hexagonal Architecture or Ports and Adapters boundaries: inward ports, outward ports, adapters, SDK leakage, controller thickness, repository adapters, external API gateways, and keeping domain or use cases independent from infrastructure details.
---

# Ports and Adapters Boundary

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Review port and adapter boundaries without confusing them with Clean Architecture enforcement.
- Keep external SDKs and framework details outside core use cases.
- Clarify inbound and outbound port ownership.

## Inputs to Inspect
- Controllers, handlers, ports, adapters, gateways, repositories, SDK clients, use cases, and tests

## Workflow
1. Map inbound adapters, application ports, outbound ports, and outbound adapters.
2. Check direction of dependencies and data translation.
3. Find SDK/framework leakage into core logic.
4. Assess whether controllers/adapters are thin enough.
5. Recommend boundary repairs and tests.

## Output Contract
- Port/adapters map
- Boundary leaks
- Dependency direction
- Data translation
- Repair steps
- Tests
- Human confirmation items

## Human Confirmation
- Which external contracts are stable enough to expose and how much abstraction the team wants.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `architecture-style-decision`
- `clean-architecture-review`
- `repository-design-and-placement`
- `dependency-direction-check`
