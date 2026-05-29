---
name: human-decision-separator
description: >
  Use when explicitly invoked or routed by software-design-router to separate decisions an AI agent can infer from evidence from decisions that require human judgment: business invariants, bounded context ownership, eventual consistency tolerance, breaking changes, core domain classification, operational risk priority, or team complexity capacity.
---

# Human Decision Separator

Software Design Skill System の一部として、設計判断を evidence-driven に進める。
通常は `software-design-router` または領域hubから呼び出す。明示的に `$human-decision-separator` と指定された場合も使う。

## Scope
- Prevent the agent from silently deciding product, business, or organizational facts.
- Label evidence, inference, recommendation, and human decision separately.
- Turn uncertainty into specific confirmation questions.

## Inputs to Inspect
- Design proposal, code evidence, docs, constraints, domain claims, and open questions

## Workflow
1. Extract every decision implied by the proposal.
2. Classify each item as evidence-backed, inference, recommendation, or human decision.
3. For each human decision, state why repo evidence is insufficient.
4. Write concise confirmation questions tied to implementation impact.
5. Feed confirmed decisions back to the primary design skill.

## Output Contract
- AI can decide
- AI can recommend
- Human must decide
- Reason
- Impact if wrong
- Question to ask

## Human Confirmation
- All listed human-decision items by definition.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `software-design-router`
- `aggregate-design`
- `bounded-context-design`
- `architecture-style-decision`
