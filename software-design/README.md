# Software Design Skills

Software design skills are grouped here to keep the repository root readable.

Start with `software-design-router` for broad or ambiguous design requests. Its routing map is in `software-design-router/references/skill-map.md`, and a graphical relationship map is in `relationship-map.md`.

## Invocation Groups

- Implicit skills handle direct user intent, such as design review, codebase audit, aggregate design, API design, refactoring planning, ADR writing, and skill authoring.
- Routed or explicit specialist skills set `policy.allow_implicit_invocation: false` in `agents/openai.yaml` and should usually be selected by `software-design-router` or a hub skill.

## Authoring

Before creating or updating any skill in this directory, read `/Users/keisuke-yamasaki/.codex/skills/.system/skill-creator/SKILL.md` and validate with Skill-Creator's `quick_validate.py`.
