---
name: pre-implementation-design-review
description: >
  Use before implementation when a user asks to design a new feature, organize use cases, split responsibilities, shape APIs, draft domain models, check dependency direction, define test strategy, or identify unresolved design decisions before coding. Use for Japanese prompts about 実装前設計, 設計レビュー, 責務分解, API設計, or 実装に入る前.
---

# Pre-Implementation Design Review

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Find design gaps before code changes begin.
- Turn feature intent into implementation-ready boundaries, decisions, and tests.
- Avoid inventing architecture that the project has not adopted.

## Inputs to Inspect
- Feature brief, issue, product requirement, or conversation notes
- Existing docs, APIs, types, tests, and similar implementations
- Known constraints such as compatibility, data ownership, latency, and rollout limits

## Workflow
1. State goal, non-goals, and current constraints.
2. Map the change to use cases, data, APIs, and state transitions.
3. Identify responsibility boundaries and dependency direction.
4. List decisions already supported by evidence and decisions that need a human.
5. Define implementation slices and the tests that protect the design.

## Output Contract
- 目的
- 変更範囲
- 主要な設計判断
- 未確定事項
- 人間が決めるべきこと
- 実装前の確認事項
- テスト方針

## Human Confirmation
- Product trade-offs, breaking changes, user-facing behavior, and domain rules not evidenced in repo docs.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `api-interface-design`
- `domain-building-blocks`
- `test-strategy-for-design`
