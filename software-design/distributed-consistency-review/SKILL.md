---
name: distributed-consistency-review
description: >
  Use when explicitly invoked or routed to review distributed consistency: exactly-once assumptions, at-least-once delivery, idempotency, ordering, retries, timeouts, duplicate events, outbox, inbox, saga, process manager, compensation, and cross-service failure modes.
---

# Distributed Consistency Review

Software Design Skill System の一部として、設計判断を evidence-driven に進める。
通常は `software-design-router` または領域hubから呼び出す。明示的に `$distributed-consistency-review` と指定された場合も使う。

## Scope
- Design for realistic distributed failure modes.
- Replace exactly-once assumptions with idempotency and recovery plans.
- Clarify ordering, retry, timeout, and compensation semantics.

## Inputs to Inspect
- Services, events, queues, retries, idempotency keys, outbox/inbox, transactions, timeouts, and failure scenarios

## Workflow
1. List each distributed step and failure point.
2. Classify delivery guarantees and duplicate/ordering risks.
3. Define idempotency, retry, timeout, and dead-letter behavior.
4. Choose outbox/inbox, saga, process manager, or compensation where needed.
5. Define monitoring and tests.

## Output Contract
- Flow
- Failure mode
- Delivery assumption
- Idempotency strategy
- Retry/ordering policy
- Compensation
- Tests/monitoring
- Human confirmation items

## Human Confirmation
- Acceptable duplicate behavior, compensation meaning, and operational recovery commitment.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `cross-aggregate-consistency`
- `domain-event-design`
- `observability-operability-review`
- `error-handling-design`
