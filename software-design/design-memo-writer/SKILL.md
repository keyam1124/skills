---
name: design-memo-writer
description: >
  Use when writing a lightweight design memo for implementation planning, pull request design explanation, trade-off notes, unresolved design questions, or a decision that is not heavy enough for a full ADR. Capture context, goal, non-goals, constraints, proposed design, alternatives, risks, human decisions, and test strategy.
---

# Design Memo Writer

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Create a practical design memo for near-term implementation.
- Keep the memo lighter than an ADR but still decision-oriented.
- Make risks, assumptions, and tests explicit.

## Inputs to Inspect
- Feature brief, design conversation, code context, constraints, alternatives, and tests
- Audience: implementer, reviewer, maintainer, or future self

## Workflow
1. State context, goal, and non-goals.
2. Summarize current constraints and proposed design.
3. Compare alternatives briefly.
4. List risks, human decisions, and test strategy.
5. Use templates/design-memo.md and mark unknowns explicitly.

## Bundled Resources
- `templates/design-memo.md`

## Output Contract
- Design memo markdown using templates/design-memo.md

## Human Confirmation
- Product choices, trade-off acceptance, and unresolved business rules.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `adr-writer`
- `pre-implementation-design-review`
- `refactoring-planner`
- `software-design-router`
