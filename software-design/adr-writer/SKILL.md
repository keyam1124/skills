---
name: adr-writer
description: >
  Use when creating, rewriting, or reviewing an Architecture Decision Record for architecture, design, dependency, data, API, migration, or operational decisions. Capture context, decision, alternatives, consequences, rejected options, owner, date, status, follow-up, evidence, and human decisions.
---

# ADR Writer

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Turn a design decision into a durable ADR.
- Separate accepted decision, rejected alternatives, consequences, and open follow-up.
- Avoid adding facts not present in evidence.

## Inputs to Inspect
- Decision context, options, constraints, evidence, affected systems, and previous ADRs
- Date, status, and owner if known

## Workflow
1. Extract decision context and forces.
2. State the accepted decision clearly.
3. List alternatives and why they were rejected.
4. Document consequences, risks, and follow-up.
5. Use templates/adr.md and mark unknowns instead of inventing.

## Bundled Resources
- `templates/adr.md`

## Output Contract
- ADR markdown using templates/adr.md
- Open questions if evidence is missing

## Human Confirmation
- Decision ownership, final status, and unresolved trade-offs.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `design-memo-writer`
- `architecture-drift-review`
- `architecture-style-decision`
- `software-design-router`
