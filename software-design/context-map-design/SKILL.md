---
name: context-map-design
description: >
  Use when explicitly invoked or routed to design a DDD Context Map and relationships such as Partnership, Shared Kernel, Customer/Supplier, Conformist, Anti-Corruption Layer, Open Host Service, Published Language, or Separate Ways. Produce Mermaid plus a relationship table.
---

# Context Map Design

Software Design Skill System の一部として、設計判断を evidence-driven に進める。
通常は `software-design-router` または領域hubから呼び出す。明示的に `$context-map-design` と指定された場合も使う。

## Scope
- Map relationships between bounded contexts and external systems.
- Identify integration patterns and dependency risks.
- Make upstream/downstream assumptions visible.

## Inputs to Inspect
- Candidate contexts, teams, APIs, events, databases, external systems, and ownership boundaries

## Workflow
1. List contexts and external systems.
2. Identify upstream/downstream direction and integration contracts.
3. Choose relationship type and explain why.
4. Draw a Mermaid context map.
5. List risks, ACL needs, published language, and human confirmations.

## Output Contract
- Mermaid Context Map
- Relationship table
- Integration risks
- ACL or published language needs
- Human confirmation items

## Human Confirmation
- Team relationship, ownership, integration commitments, and relationship type acceptance.

## Do Not
- Do not present unevidenced business rules, organizational boundaries, or strategy as facts.
- Do not force DDD, Clean Architecture, CQRS, Event Sourcing, or microservice patterns when the project context does not justify them.
- Do not hide uncertainty inside confident recommendations; list human confirmation items instead.

## Related Skills
- `bounded-context-design`
- `domain-message-flow-modeling`
- `ports-and-adapters-boundary`
