---
name: information-hiding-deep-modules
description: >
  Use when reviewing information hiding, deep modules, shallow modules, information leakage, temporal decomposition, pass-through methods, excessive configuration, implementation details in APIs, change amplification, cognitive load, or unclear module responsibilities.
---

# Information Hiding Deep Modules

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Evaluate modules by interface simplicity versus implementation depth.
- Find information leakage and shallow wrappers.
- Reduce change amplification and cognitive load.

## Inputs to Inspect
- Module APIs, public methods, configuration, call chains, package boundaries, docs, and tests

## Workflow
1. Identify module purpose and public interface.
2. Check whether interface exposes implementation details or ordering requirements.
3. Find pass-through methods, temporal decomposition, and excessive knobs.
4. Propose deeper boundaries or API simplification.
5. Define compatibility and tests.

## Output Contract
- Module/API
- Information leak
- Change amplification
- Cognitive load
- Deeper interface proposal
- Tests
- Human confirmation items

## Human Confirmation
- Compatibility constraints and whether callers rely on exposed details.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `package-module-design`
- `api-interface-design`
- `oo-design-principles`
