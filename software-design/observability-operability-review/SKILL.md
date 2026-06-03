---
name: observability-operability-review
description: >
  Use when reviewing design-time operability: logs, metrics, traces, business events, SLOs, SLAs, alerts, dashboards, runbooks, audit logs, failure modes, backfills, replay, support workflows, and how maintainers will detect and recover from problems.
---

# Observability Operability Review

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Review whether a design can be operated after release.
- Define observable signals for business and technical failure modes.
- Avoid adding noisy telemetry without ownership or action.

## Inputs to Inspect
- Design proposal, critical flows, failure modes, logs, metrics, traces, audit needs, runbooks, SLOs, and support requirements

## Workflow
1. Identify critical user/business flows and failure modes.
2. Define logs, metrics, traces, audit events, and alerts tied to action.
3. Check dashboard and runbook needs.
4. Assess backfill/replay/recovery operations.
5. List owner and human decisions.

## Output Contract
- Failure mode
- Signal
- Alert/action
- Dashboard/runbook
- Audit needs
- Recovery path
- Human confirmation items

## Human Confirmation
- SLO/SLA targets, alert ownership, audit requirements, and operational budget.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `distributed-consistency-review`
- `event-sourcing-decision`
- `error-handling-design`
