---
name: skill-eval-and-trigger-boundary
description: >
  Use when explicitly invoked or routed to test and improve Skill trigger boundaries, should-trigger prompts, should-not-trigger prompts, competing Skill descriptions, output quality checks, regression cases, baseline comparison, and routed versus implicit invocation policy.
---

# Skill Eval and Trigger Boundary

Software Design Skill System の一部として、設計判断を evidence-driven に進める。
通常は `software-design-router` または領域hubから呼び出す。明示的に `$skill-eval-and-trigger-boundary` と指定された場合も使う。

## Scope
- Evaluate whether a Skill fires for the right prompts and stays silent for adjacent prompts.
- Improve descriptions and evals based on failures.
- Protect against specialist skills competing with router or hub skills.

## Inputs to Inspect
- Skill name, SKILL.md description, agents/openai.yaml policy, trigger examples, non-trigger examples, output examples, and regression cases

## Workflow
1. Read the target skill description and related skill descriptions.
2. Create positive and negative trigger cases.
3. Define output quality requirements and rejection criteria.
4. Identify collisions with neighboring skills.
5. Recommend description, policy, or eval updates and validate with quick_validate.py.

## Output Contract
- Trigger evals
- Non-trigger evals
- Output evals
- Collisions
- Description changes
- Policy recommendation
- Regression cases

## Human Confirmation
- Whether a skill should be implicit, routed only, merged, or split.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `software-design-skill-forge`
- `software-design-router`
