# Software Design Skill Relationship Map

This document visualizes how the Software Design skills relate to each other.

## Legend

- Solid arrows mean the source skill commonly routes to, supports, or produces input for the target skill.
- Dotted arrows from `software-design-router` mean routed or explicit specialist invocation.
- `software-design-router` is the normal entrypoint for broad or ambiguous design requests.
- Routed or explicit specialist skills usually have `policy.allow_implicit_invocation: false`.

## Category Overview

```mermaid
flowchart LR
  User["User request"] --> Router["software-design-router"]

  Router --> Workflow["Workflow skills"]
  Router --> DDDStrategic["DDD strategic skills"]
  Router --> DDDTactical["DDD tactical skills"]
  Router --> Architecture["Architecture skills"]
  Router --> Quality["Quality skills"]
  Router --> System["System design skills"]
  Router --> Output["Output skills"]
  Router --> Meta["Meta skills"]

  Workflow --> Human["human-decision-separator"]
  DDDStrategic --> Human
  DDDTactical --> Human
  Architecture --> Human
  System --> Human

  Workflow --> Output
  DDDStrategic --> Output
  DDDTactical --> Output
  Architecture --> Output
  Quality --> Output
  System --> Output

  Meta --> Router
```

## Skill Relationship Graph

```mermaid
flowchart LR
  Router["software-design-router"]

  subgraph Workflow["Workflow"]
    PreImpl["pre-implementation-design-review"]
    Audit["codebase-design-audit"]
    Drift["architecture-drift-review"]
    Human["human-decision-separator"]
  end

  subgraph DDDStrategic["DDD strategic"]
    UL["ubiquitous-language-mining"]
    Subdomain["subdomain-classification"]
    Bounded["bounded-context-design"]
    ContextMap["context-map-design"]
    MessageFlow["domain-message-flow-modeling"]
  end

  subgraph DDDTactical["DDD tactical"]
    BuildingBlocks["domain-building-blocks"]
    Primitive["domain-primitive-design"]
    Aggregate["aggregate-design"]
    TxBoundary["aggregate-transaction-boundary"]
    CrossConsistency["cross-aggregate-consistency"]
    Repository["repository-design-and-placement"]
    ServiceSplit["domain-service-vs-application-service"]
    DomainEvent["domain-event-design"]
  end

  subgraph Architecture["Architecture"]
    ArchStyle["architecture-style-decision"]
    Clean["clean-architecture-review"]
    Ports["ports-and-adapters-boundary"]
    Package["package-module-design"]
    Dependency["dependency-direction-check"]
    Modular["modular-monolith-boundary"]
  end

  subgraph Quality["Quality"]
    OO["oo-design-principles"]
    InfoHiding["information-hiding-deep-modules"]
    Error["error-handling-design"]
    API["api-interface-design"]
    Refactor["refactoring-planner"]
    Test["test-strategy-for-design"]
  end

  subgraph System["System design"]
    CQRS["cqrs-decision"]
    EventSourcing["event-sourcing-decision"]
    DataModel["data-modeling-review"]
    Distributed["distributed-consistency-review"]
    Observability["observability-operability-review"]
  end

  subgraph Output["Output"]
    ADR["adr-writer"]
    Memo["design-memo-writer"]
    Canvas["decision-canvas-filler"]
  end

  subgraph Meta["Meta"]
    Forge["software-design-skill-forge"]
    Eval["skill-eval-and-trigger-boundary"]
  end

  Router --> PreImpl
  Router --> Audit
  Router --> Drift
  Router --> BuildingBlocks
  Router --> Aggregate
  Router --> Bounded
  Router --> ArchStyle
  Router --> Clean
  Router --> Package
  Router --> Error
  Router --> API
  Router --> Refactor
  Router --> CQRS
  Router --> EventSourcing
  Router --> ADR
  Router --> Memo
  Router --> Forge

  Router -.-> Human
  Router -.-> UL
  Router -.-> Subdomain
  Router -.-> ContextMap
  Router -.-> MessageFlow
  Router -.-> Primitive
  Router -.-> TxBoundary
  Router -.-> CrossConsistency
  Router -.-> Repository
  Router -.-> ServiceSplit
  Router -.-> DomainEvent
  Router -.-> Ports
  Router -.-> Dependency
  Router -.-> Modular
  Router -.-> OO
  Router -.-> InfoHiding
  Router -.-> Test
  Router -.-> DataModel
  Router -.-> Distributed
  Router -.-> Observability
  Router -.-> Canvas
  Router -.-> Eval

  PreImpl --> API
  PreImpl --> Test
  PreImpl --> Human
  PreImpl --> Memo

  Audit --> Package
  Audit --> Dependency
  Audit --> Error
  Audit --> Refactor

  Drift --> Dependency
  Drift --> Clean
  Drift --> ADR

  Bounded --> UL
  Bounded --> Subdomain
  Bounded --> ContextMap
  Bounded --> MessageFlow
  Bounded --> Canvas

  BuildingBlocks --> Primitive
  BuildingBlocks --> Aggregate
  BuildingBlocks --> Repository
  BuildingBlocks --> ServiceSplit
  BuildingBlocks --> DomainEvent

  Aggregate --> TxBoundary
  Aggregate --> CrossConsistency
  Aggregate --> Repository
  Aggregate --> DomainEvent
  Aggregate --> Canvas

  ArchStyle --> Clean
  ArchStyle --> Ports
  ArchStyle --> Modular
  ArchStyle --> Memo

  Package --> Dependency
  Package --> InfoHiding
  Package --> Modular
  Package --> Refactor

  Error --> API
  Error --> Distributed
  Error --> Observability
  Error --> Test

  API --> DataModel
  API --> Test
  Refactor --> Test
  Refactor --> Package
  Refactor --> OO

  CQRS --> DataModel
  CQRS --> Distributed
  CQRS --> EventSourcing
  CQRS --> Test

  EventSourcing --> DomainEvent
  EventSourcing --> Distributed
  EventSourcing --> Observability

  DomainEvent --> MessageFlow
  DomainEvent --> Distributed

  Distributed --> Observability
  Distributed --> Error

  ADR --> Drift
  Memo --> PreImpl
  Canvas --> Aggregate
  Canvas --> Bounded

  Forge --> Eval
  Forge --> Router
  Eval --> Router
```

## Common Usage Flows

### New Feature Design

```mermaid
flowchart LR
  Request["New feature request"] --> Router["software-design-router"]
  Router --> PreImpl["pre-implementation-design-review"]
  PreImpl --> API["api-interface-design"]
  PreImpl --> Test["test-strategy-for-design"]
  PreImpl --> Human["human-decision-separator"]
  PreImpl --> Memo["design-memo-writer"]
```

### Existing Codebase Audit

```mermaid
flowchart LR
  Request["Existing codebase"] --> Router["software-design-router"]
  Router --> Audit["codebase-design-audit"]
  Audit --> Package["package-module-design"]
  Audit --> Dependency["dependency-direction-check"]
  Audit --> Error["error-handling-design"]
  Audit --> Refactor["refactoring-planner"]
```

### DDD Aggregate Work

```mermaid
flowchart LR
  Request["Aggregate or invariant question"] --> Router["software-design-router"]
  Router --> Aggregate["aggregate-design"]
  Aggregate --> Tx["aggregate-transaction-boundary"]
  Aggregate --> Cross["cross-aggregate-consistency"]
  Aggregate --> Event["domain-event-design"]
  Aggregate --> Canvas["decision-canvas-filler"]
```

### Context Design

```mermaid
flowchart LR
  Request["Context boundary question"] --> Router["software-design-router"]
  Router --> Bounded["bounded-context-design"]
  Bounded --> UL["ubiquitous-language-mining"]
  Bounded --> Subdomain["subdomain-classification"]
  Bounded --> ContextMap["context-map-design"]
  Bounded --> Flow["domain-message-flow-modeling"]
```

### Skill Authoring

```mermaid
flowchart LR
  Request["Create or improve a design skill"] --> Forge["software-design-skill-forge"]
  Forge --> SkillCreator["Skill-Creator SKILL"]
  Forge --> Eval["skill-eval-and-trigger-boundary"]
  Eval --> Trigger["trigger-evals.json"]
  Eval --> Output["output-evals.json"]
  Eval --> Regression["regression-cases.md"]
```
