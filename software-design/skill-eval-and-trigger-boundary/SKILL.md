---
name: skill-eval-and-trigger-boundary
description: >
  Use when testing and improving Skill trigger boundaries, should-trigger prompts, should-not-trigger prompts, competing Skill descriptions, output quality checks, regression cases, baseline comparison, and selection policy.
---

# Skill Eval and Trigger Boundary

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Evaluate whether a Skill fires for the right prompts and stays silent for adjacent prompts.
- Improve descriptions and evals based on failures.
- Protect against specialist skills competing with broad entrypoint or hub skills.

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
- Whether a skill should be a broad entrypoint, narrow specialist, merged, or split.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `software-design-skill-forge`
