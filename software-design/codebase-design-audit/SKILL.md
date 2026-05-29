---
name: codebase-design-audit
description: >
  Use when reading an existing codebase to find design problems: leaked domain logic, oversized controllers or handlers, application service overreach, misplaced repositories, layer violations, package or module cycles, aggregate boundary candidates, inconsistent error handling, or structures that make testing hard.
---

# Codebase Design Audit

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Audit existing code for design issues grounded in concrete files.
- Prioritize findings by behavior risk and change cost.
- Distinguish evidence from architectural preference.

## Inputs to Inspect
- Repository files, dependency graph clues, tests, docs, ADRs, and naming conventions
- Hot paths, high-churn areas, or files named by the user
- Existing architecture rules, if present

## Workflow
1. Inspect entrypoints, domain/application boundaries, persistence, API, and tests.
2. Trace where business rules, validation, and side effects live.
3. Look for cycles, framework leaks, shared-module growth, and duplicated decisions.
4. Group findings by design boundary instead of file inventory.
5. Recommend small repair paths and tests before broad refactors.

## Output Contract
- Design Audit Findings
- Evidence
- Impact
- Repair Direction
- Human Confirmation
- Tests to Add

## Human Confirmation
- Whether observed design drift is intentional, acceptable complexity, and prioritization of repair work.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `package-module-design`
- `dependency-direction-check`
- `error-handling-design`
- `refactoring-planner`
