---
name: oo-design-principles
description: >
  Use when explicitly invoked or routed to review object-oriented design principles such as SOLID, GRASP, cohesion, coupling, Tell Dont Ask, Law of Demeter, encapsulation, polymorphism, responsibility assignment, and avoiding procedural service objects.
---

# OO Design Principles

Software Design Skill System の一部として、設計判断を evidence-driven に進める。
通常は `software-design-router` または領域hubから呼び出す。明示的に `$oo-design-principles` と指定された場合も使う。

## Scope
- Apply OO principles as practical checks, not slogans.
- Tie each principle finding to concrete behavior or change risk.
- Route deeper repeated conditional work to polymorphic-branch-refactoring.

## Inputs to Inspect
- Classes, structs, services, methods, collaborators, conditionals, data access, and tests

## Workflow
1. Identify responsibilities and reasons to change.
2. Check cohesion, coupling, data exposure, and message chains.
3. Look for Tell Dont Ask and Law of Demeter violations that cause change amplification.
4. Recommend the smallest design move that reduces risk.
5. Add tests before behavior-moving refactors.

## Output Contract
- Principle finding
- Evidence
- Change risk
- Recommended move
- Tests
- Do not over-abstract note

## Human Confirmation
- Acceptable abstraction cost and team idioms for the language/framework.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `information-hiding-deep-modules`
- `polymorphic-branch-refactoring`
- `refactoring-planner`
