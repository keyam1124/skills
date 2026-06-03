---
name: domain-message-flow-modeling
description: >
  Use when modeling command, event, query, domain event, integration event, and cross-context message flow. Decide which context receives commands, which events are published, whether sync calls or events fit, and where query/read models are built.
---

# Domain Message Flow Modeling

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Make domain message flow explicit across contexts or modules.
- Differentiate commands, domain events, integration events, and queries.
- Expose consistency, ordering, and ownership questions.

## Inputs to Inspect
- Use cases, commands, events, queries, context boundaries, APIs, queues, outbox/inbox patterns, and read models

## Workflow
1. List actors and triggering commands.
2. Assign command handling ownership.
3. Name domain events and integration events separately.
4. Map read/query model ownership and freshness expectations.
5. Identify synchronous calls, asynchronous events, idempotency, and human confirmations.

## Output Contract
- Command flow
- Domain events
- Integration events
- Query/read model flow
- Consistency risks
- Human confirmation items

## Human Confirmation
- Freshness tolerance, event publication commitments, and workflow ownership.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `bounded-context-design`
- `context-map-design`
- `domain-event-design`
- `distributed-consistency-review`
