---
name: test-strategy-for-design
description: >
  Use when explicitly invoked or routed to define tests that protect design decisions: domain model unit tests, use case tests, contract tests, integration tests, architecture tests, characterization tests, golden master tests, property-based tests, or event-driven flow tests.
---

# Test Strategy for Design

Software Design Skill System の一部として、設計判断を evidence-driven に進める。
通常は `software-design-router` または領域hubから呼び出す。明示的に `$test-strategy-for-design` と指定された場合も使う。

## Scope
- Connect design choices to concrete verification.
- Avoid beautiful design proposals with no behavior protection.
- Choose the lightest test level that catches the risk.

## Inputs to Inspect
- Design proposal, affected behavior, existing tests, public contracts, architecture rules, event flows, and risk areas

## Workflow
1. List each design decision and failure mode.
2. Choose test level: domain, use case, contract, integration, architecture, characterization, golden master, or property-based.
3. Define minimal scenarios and fixtures.
4. Identify what should not be tested at low value.
5. Return an implementation-ready test plan.

## Output Contract
- Design decision
- Risk
- Test level
- Scenarios
- Fixtures/data
- Regression target
- Human confirmation items

## Human Confirmation
- Acceptable test cost, test environment constraints, and release risk.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `pre-implementation-design-review`
- `refactoring-planner`
- `api-interface-design`
- `aggregate-design`
