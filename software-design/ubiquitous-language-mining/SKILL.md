---
name: ubiquitous-language-mining
description: >
  Use when extracting ubiquitous language candidates from requirements, conversations, issues, docs, code, APIs, database names, or tests. Detect term drift, synonyms, homonyms, mismatches between business terms and code names, and words that require domain expert confirmation.
---

# Ubiquitous Language Mining

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Extract domain vocabulary grounded in source artifacts.
- Find ambiguity and mismatches between business language and implementation names.
- Prepare glossary candidates for bounded context or domain modeling work.

## Inputs to Inspect
- Requirements, issues, docs, UI copy, class names, API names, DB names, tests, and conversations

## Workflow
1. Collect terms and exact usage locations.
2. Group synonyms and detect same-word different-meaning cases.
3. Compare business terms to code and storage names.
4. Mark ambiguity and confirmation owner.
5. Feed confirmed language into bounded-context-design or domain-building-blocks.

## Output Contract
- 用語
- 意味候補
- 使用箇所
- 曖昧さ
- 確認すべき相手
- 命名への影響

## Human Confirmation
- Final meaning of ambiguous terms and preferred domain language.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `bounded-context-design`
- `subdomain-classification`
- `domain-building-blocks`
