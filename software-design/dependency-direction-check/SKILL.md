---
name: dependency-direction-check
description: >
  Use when explicitly invoked or routed to inspect dependency direction violations: domain depending on infrastructure, use cases depending on controllers, feature modules depending on each other incorrectly, shared module bloat, framework imports leaking into core packages, or forbidden import rules.
---

# Dependency Direction Check

Software Design Skill System の一部として、設計判断を evidence-driven に進める。
通常は `software-design-router` または領域hubから呼び出す。明示的に `$dependency-direction-check` と指定された場合も使う。

## Scope
- Check dependency direction with concrete import or reference evidence.
- Treat violations as candidates until project rules are confirmed.
- Separate mechanical findings from design judgment.

## Inputs to Inspect
- Imports, package manifests, module graph, build targets, architecture docs, forbidden dependency rules, and tests

## Workflow
1. Identify intended dependency rule from docs or existing structure.
2. Collect import/reference evidence.
3. Classify violations by rule, impact, and confidence.
4. Recommend adapter, interface, package split, or dependency inversion repairs.
5. Name architecture tests or static checks to prevent regression.

## Output Contract
- 違反候補
- 根拠
- 影響
- 修正案
- 自動修正可否
- 確認すべきルール

## Human Confirmation
- Whether the inferred rule is real and whether temporary violations are acceptable.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `package-module-design`
- `clean-architecture-review`
- `ports-and-adapters-boundary`
