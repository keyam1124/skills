---
name: error-handling-design
description: >
  Use when designing or reviewing error handling: recoverable versus unrecoverable errors, domain errors, application errors, infrastructure errors, validation errors, invariant violations, retryable failures, Result or Either or exception choices, user-facing error messages, API error semantics, or logging boundaries.
---

# Error Handling Design

Software Design Skill System の一部として、設計判断を evidence-driven に進める。

## Scope
- Design consistent error semantics across layers and interfaces.
- Separate validation, invariant violations, infrastructure failures, and user-facing messages.
- Prevent retry, logging, and exception policy from leaking everywhere.

## Inputs to Inspect
- Current error types, exceptions, API responses, validation paths, retries, logs, and tests
- User-facing behavior and operational needs

## Workflow
1. Classify each error by source, recoverability, retryability, and audience.
2. Define where errors are created, translated, logged, and surfaced.
3. Choose language-appropriate representation without mixing concerns.
4. Check API and UI semantics for compatibility.
5. Add tests for representative failure paths.

## Output Contract
- Error categories
- Representation choice
- Boundary translation
- Retry and logging policy
- User-facing semantics
- Tests
- Human confirmation items

## Human Confirmation
- What users should see, compliance/audit needs, and compatibility expectations.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `api-interface-design`
- `distributed-consistency-review`
- `observability-operability-review`
- `test-strategy-for-design`
