---
name: refactoring-planner
description: >
  Use when planning a design refactor, legacy code cleanup, package split, domain extraction, behavior-preserving migration, strangler pattern, branch by abstraction, characterization test plan, rollback plan, or staged refactoring sequence before editing code.
---

# Refactoring Planner

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Turn design debt into a staged, behavior-preserving refactoring plan.
- Prioritize characterization tests before risky movement.
- Keep scope narrow and reversible.

## Inputs to Inspect
- Current code, tests, design smells, desired outcome, risky behavior, and deployment constraints
- Change history or failing examples if relevant

## Workflow
1. State current design problem and target boundary.
2. Identify behavior that must not change.
3. Add or name characterization tests first.
4. Split work into small steps with validation after each step.
5. Define rollback or stop points and human decisions.

## Bundled Resources
- `templates/refactoring-plan.md`

## Output Contract
- 現状の設計問題
- 変更目標
- 保護すべき振る舞い
- 先に追加するテスト
- 変更単位
- リスク
- ロールバック方法

## Human Confirmation
- Scope, behavior-change tolerance, release timing, and acceptable temporary duplication.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `codebase-design-audit`
- `package-module-design`
- `polymorphic-branch-refactoring`
- `test-strategy-for-design`
