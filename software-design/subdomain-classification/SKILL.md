---
name: subdomain-classification
description: >
  Use when explicitly invoked or routed to classify candidate domains as Core Domain, Supporting Domain, or Generic Domain. Produce evidence-backed candidates only; do not let the agent conclusively decide business strategy without human confirmation.
---

# Subdomain Classification

Software Design Skill System の一部として、設計判断を evidence-driven に進める。
通常は `software-design-router` または領域hubから呼び出す。明示的に `$subdomain-classification` と指定された場合も使う。

## Scope
- Classify subdomain candidates with uncertainty visible.
- Avoid presenting strategic domain classification as an AI fact.
- Connect classification to investment and design complexity choices.

## Inputs to Inspect
- Product goals, revenue or differentiation clues, workflows, team focus, domain language, existing modules, and stakeholder notes

## Workflow
1. List domain areas and business capabilities.
2. Compare each area by differentiation, complexity, change rate, and commodity availability.
3. Classify as candidate Core, Supporting, or Generic with confidence.
4. State investment implications and uncertainty.
5. Ask for human confirmation before using classification as a design premise.

## Output Contract
- 領域
- 分類候補
- 根拠
- 不確実性
- 設計への影響
- 人間確認事項

## Human Confirmation
- Strategic differentiation, investment priority, and business value.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `bounded-context-design`
- `ubiquitous-language-mining`
- `architecture-style-decision`
