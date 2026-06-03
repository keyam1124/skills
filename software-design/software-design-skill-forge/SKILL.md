---
name: software-design-skill-forge
description: >
  Use when creating, splitting, improving, or evaluating Software Design Skills, including trigger descriptions, references, templates, examples, evals, selection policy, and skill-map updates. Always use the Skill-Creator skill first and follow its init_skill.py and quick_validate.py workflow.
---

# Software Design Skill Forge

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Create or improve Software Design Skills using Skill-Creator as the governing workflow.
- Keep SKILL.md lean and move details into references or templates.
- Maintain trigger boundaries and selection policy.

## Inputs to Inspect
- Requested design skill behavior, concrete trigger examples, current skill-map, existing related skills, and desired outputs
- Skill-Creator instructions and validation scripts

## Workflow
1. Read /Users/keisuke-yamasaki/.codex/skills/.system/skill-creator/SKILL.md before creating or updating a skill.
2. Capture concrete use examples and non-trigger examples.
3. Run Skill-Creator init_skill.py for new skills unless the skill already exists.
4. Write SKILL.md with only name and description in frontmatter.
5. Add references, templates, and evals only when they directly support use.
6. Validate with quick_validate.py and trigger/output evals.

## Output Contract
- Skill directory
- SKILL.md
- agents/openai.yaml
- references/templates/evals as needed
- Validation results

## Human Confirmation
- Whether a new skill should be a broad entrypoint, narrow specialist, or folded into an existing hub skill.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `skill-eval-and-trigger-boundary`
- `decision-canvas-filler`
