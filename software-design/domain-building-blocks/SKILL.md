---
name: domain-building-blocks
description: >
  Use for DDD tactical modeling decisions about Entity, Value Object, Aggregate, Domain Service, Repository, Factory, Specification, or domain model extraction. Use when prompts mention ドメインモデル, Entity, Value Object, 集約, Repository, Domain Service, or where business rules should live.
---

# Domain Building Blocks

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Choose appropriate DDD tactical building blocks without forcing DDD on simple code.
- Move business rules toward explicit domain concepts.
- Identify when a specialist skill should handle deeper aggregate, repository, or event questions.

## Inputs to Inspect
- Business language and invariants
- Current types, services, repositories, and validators
- Persistence and API shapes only as evidence, not as the domain model itself

## Workflow
1. Identify terms, identities, lifecycle, and invariants.
2. Separate value semantics from identity and persistence concerns.
3. Decide candidate Entity, Value Object, Aggregate, Domain Service, Repository, or Factory roles.
4. Check whether rules are duplicated in application/UI/persistence layers.
5. Escalate to aggregate-design or repository-design-and-placement when boundaries are the main question.

## Output Contract
- 候補となるドメイン概念
- Building Block分類
- 根拠
- 代替案
- 人間確認事項
- 実装時の注意

## Human Confirmation
- True business invariants, language meaning, and whether DDD complexity is justified.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `domain-primitive-design`
- `aggregate-design`
- `repository-design-and-placement`
- `domain-service-vs-application-service`
