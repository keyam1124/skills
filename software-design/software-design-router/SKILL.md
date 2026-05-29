---
name: software-design-router
description: >
  Use when the user asks for software design review, architecture advice, DDD or Clean Architecture guidance, refactoring direction, codebase design audit, package or dependency review, ADR or design memo generation, or wants to organize design before implementation. Route the task to the right design skill and separate evidence, inference, trade-offs, and human decisions.
---

# Software Design Router

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Classify the user request before selecting design guidance.
- Choose primary and secondary Software Design Skills.
- Separate facts, inference, trade-offs, and decisions that need human confirmation.

## Inputs to Inspect
- User request and explicit constraints
- Relevant code, docs, ADRs, schemas, tests, and task context
- Project architecture already adopted, if discoverable

## Workflow
1. Identify whether the request is design advice, implementation preflight, code audit, ADR writing, drift review, or refactoring planning.
2. Read the smallest evidence set that can justify routing.
3. Choose one primary skill and optional supporting skills from references/skill-map.md.
4. Name skills that should not be used, especially Clean Architecture or DDD skills when the project has not adopted them.
5. Return the selected output form and list human decisions separately.

## Bundled Resources
- `references/skill-map.md`

## Output Contract
- 目的
- 根拠
- 推論
- 使うSkill
- 使わないSkill
- 人間確認事項
- 推奨出力形式

## Human Confirmation
- Business invariants, organizational boundaries, breaking-change tolerance, and acceptable operational complexity.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `pre-implementation-design-review`
- `codebase-design-audit`
- `adr-writer`
- `design-memo-writer`
