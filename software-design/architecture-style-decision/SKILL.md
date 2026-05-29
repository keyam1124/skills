---
name: architecture-style-decision
description: >
  Use when deciding among architecture styles such as Clean Architecture, Hexagonal Architecture, Onion Architecture, Layered Architecture, Modular Monolith, microservices, or simpler CRUD-oriented designs. Use for trade-off comparison before adopting an architecture, not for enforcing one style already chosen.
---

# Architecture Style Decision

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Compare architecture styles against project constraints.
- Avoid adopting complex patterns for status or aesthetics.
- Produce a decision table and explicit non-goals.

## Inputs to Inspect
- Product complexity, team size, change rate, integration needs, deployment constraints, test needs, and existing code shape
- Known pain points such as coupling, framework lock-in, or module ownership

## Workflow
1. State the forces that matter: domain complexity, data ownership, deployability, testability, and team capacity.
2. List viable styles including a simpler baseline.
3. Compare costs, benefits, risks, and migration path.
4. Reject styles that solve problems the project does not have.
5. Recommend a default and identify human decisions.

## Output Contract
- 候補
- 向いている条件
- 合わない条件
- コスト
- 採用リスク
- 推奨案
- 人間確認事項

## Human Confirmation
- Team maintenance capacity, deployment strategy, and appetite for migration cost.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `clean-architecture-review`
- `ports-and-adapters-boundary`
- `modular-monolith-boundary`
- `design-memo-writer`
