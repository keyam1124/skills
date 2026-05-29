---
name: bounded-context-design
description: >
  Use when designing or reviewing DDD Bounded Contexts, context boundaries, model ownership, ubiquitous language boundaries, data ownership, team ownership, external integration boundaries, or model-sharing risks. Use for prompts mentioning Bounded Context, 境界づけられたコンテキスト, コンテキスト境界, or Context Map.
---

# Bounded Context Design

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Design model and language boundaries across a system.
- Clarify ownership of data, APIs, integrations, and teams.
- Avoid assuming bounded contexts where the product is simpler.

## Inputs to Inspect
- Domain areas, user journeys, vocabulary, teams, APIs, databases, and integration points
- Pain points from shared models or inconsistent terms
- Existing docs and module boundaries

## Workflow
1. Mine language differences and model conflicts.
2. Identify candidate contexts and their responsibilities.
3. Assign ownership for data and published interfaces.
4. Map upstream/downstream dependencies and shared kernel risks.
5. Fill templates/bounded-context-canvas.md and route to context-map-design if relationships dominate.

## Bundled Resources
- `templates/bounded-context-canvas.md`

## Output Contract
- Context name
- Purpose
- Ubiquitous language
- Owned model and data
- Inbound and outbound interfaces
- Dependencies
- Risks
- Human confirmation items

## Human Confirmation
- Team ownership, organizational boundaries, context split cost, and acceptable model sharing.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `ubiquitous-language-mining`
- `subdomain-classification`
- `context-map-design`
- `domain-message-flow-modeling`
