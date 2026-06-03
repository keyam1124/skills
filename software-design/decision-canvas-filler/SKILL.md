---
name: decision-canvas-filler
description: >
  Use when filling structured design canvases such as Bounded Context Canvas, Aggregate Design Canvas, Context Map, Domain Message Flow, Architecture Trade-off Matrix, human confirmation list, or design review report from available evidence.
---

# Decision Canvas Filler

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Turn design evidence into a structured canvas.
- Leave unknown cells explicit instead of inventing details.
- Use canvas output as a collaboration artifact with humans.

## Inputs to Inspect
- Design notes, code evidence, domain terms, diagrams, ADRs, and chosen canvas type

## Workflow
1. Select the canvas type or ask the router-provided default.
2. Fill cells only from evidence or clearly marked inference.
3. Add alternatives and human confirmation cells.
4. Link source evidence where useful.
5. Return a canvas ready to paste into an ADR or design memo.

## Output Contract
- Selected canvas
- Filled sections
- Unknowns
- Human confirmation items
- Evidence notes

## Human Confirmation
- Any canvas cell about business rules, ownership, and strategic priority without evidence.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `aggregate-design`
- `bounded-context-design`
- `architecture-style-decision`
- `design-memo-writer`
