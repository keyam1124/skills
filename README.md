# skills

Agent Skills for Codex.

## Start Here

This repository contains personal Codex skills. Standalone skills live in a top-level `skill-name/` directory. Related skill systems may live under a grouping directory such as `software-design/skill-name/`. Every skill directory still contains a required `SKILL.md` and recommended `agents/openai.yaml`.

Use `/Users/keisuke-yamasaki/.codex/skills/.system/skill-creator/SKILL.md` before creating or updating any skill. New skills should be initialized with Skill-Creator's `init_skill.py`, edited to remove scaffolding, then validated with `quick_validate.py`.

## Software Design Skill System

The Software Design Skill System is grouped under `software-design/` and is organized as a router plus implicit skills and routed specialists.

If a Codex harness only scans direct children of a configured skills directory, configure `software-design/` as an additional skills root or flatten it during installation. The grouped layout is for repository organization; each nested `software-design/<skill-name>/` directory remains a normal skill directory.

Implicit Software Design skills:

- `software-design-router`
- `pre-implementation-design-review`
- `codebase-design-audit`
- `architecture-drift-review`
- `domain-building-blocks`
- `aggregate-design`
- `bounded-context-design`
- `architecture-style-decision`
- `clean-architecture-review`
- `package-module-design`
- `error-handling-design`
- `api-interface-design`
- `refactoring-planner`
- `cqrs-decision`
- `event-sourcing-decision`
- `adr-writer`
- `design-memo-writer`
- `software-design-skill-forge`

Routed or explicit specialist skills set `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. Start with `software-design/software-design-router/references/skill-map.md` when choosing among them.

## Existing Non-Software-Design Skills

- `swift-design-practices`
- `polymorphic-branch-refactoring`
- `polishing-documents`

These are intentionally left independent. Software Design skills may reference them, but should not duplicate their detailed guidance.

## Validation

Run the Skill-Creator validator for each skill:

```bash
find . -name SKILL.md -exec dirname {} \; | while read -r skill; do
  python3 /Users/keisuke-yamasaki/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill"
done
```

If `python3` cannot import `yaml`, use a temporary venv with PyYAML. Do not vendor validation dependencies into this repo.

Check for scaffold leftovers:

```bash
rg -n '(TO)(DO)|\[(TO)(DO)|(template) (placeholder)' . --glob '!swift-design-practices/scripts/swift_design_scan.py'
```

Check generated metadata:

```bash
find . -path "*/agents/openai.yaml" -print -exec rg -n "default_prompt|allow_implicit_invocation|short_description" {} \;
```

## Skill Authoring Rules

- Keep `SKILL.md` concise and procedural.
- Put trigger conditions in frontmatter `description`, not only in the body.
- Keep `SKILL.md` frontmatter to `name` and `description`.
- Move long principles, examples, and background into `references/`.
- Put reusable output forms in `templates/`.
- Add `evals/trigger-evals.json`, `evals/output-evals.json`, and `evals/regression-cases.md` for trigger and output boundaries.
- Preserve `$skill-name` literally in `agents/openai.yaml` default prompts.
