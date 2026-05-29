---
name: domain-event-design
description: >
  Use when explicitly invoked or routed to design Domain Events, Integration Events, Event Sourcing events, event names, event granularity, past-tense naming, payload fields, outbox, idempotency, retry, ordering, schema evolution, and conversion between internal and published events.
---

# Domain Event Design

Software Design Skill System の一部として、設計判断を evidence-driven に進める。
通常は `software-design-router` または領域hubから呼び出す。明示的に `$domain-event-design` と指定された場合も使う。

## Scope
- Separate domain events from integration and stored events.
- Design event names and payloads around facts, not commands.
- Surface delivery, idempotency, ordering, and schema evolution risks.

## Inputs to Inspect
- State transitions, aggregate commands, event consumers, schemas, queues, outbox/inbox, retries, and tests

## Workflow
1. Identify the fact that happened and the producer boundary.
2. Choose domain event, integration event, or event-sourced record.
3. Name event in past tense and define minimal payload.
4. Define publication timing, outbox, idempotency, retry, and schema versioning.
5. List consumer contracts and tests.

## Output Contract
- Event type
- Name
- Producer
- Payload
- Publication boundary
- Delivery guarantees
- Schema evolution
- Tests
- Human confirmation items

## Human Confirmation
- Published contract commitments and acceptable delivery/ordering guarantees.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `aggregate-design`
- `domain-message-flow-modeling`
- `distributed-consistency-review`
- `event-sourcing-decision`
