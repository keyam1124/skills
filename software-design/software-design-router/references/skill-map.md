# Software Design Skill Map

Use this map from `software-design-router` before loading specialist skills. Prefer one primary skill and at most two supporting skills. For a graphical overview, see `../../relationship-map.md`.

## Routing Rules

- Start with `software-design-router` for broad or ambiguous design requests.
- Use implicit skills for direct user intent and routed skills for deeper specialist checks.
- Do not use `clean-architecture-review` unless the user or repo explicitly says Clean Architecture.
- Do not use DDD tactical skills for CRUD, scripting, UI-only, or data-pipeline tasks unless domain modeling is the real problem.
- Always separate Evidence, Inference, Decision, and Human confirmation for business or organizational choices.

## Skills

| Category | Skill | Invocation | Primary use | Avoid when |
| --- | --- | --- | --- | --- |
| 入口 | `software-design-router` | implicit | Classify the user request before selecting design guidance. | この文章の日本語だけ校正して。 |
| 入口 | `pre-implementation-design-review` | implicit | Find design gaps before code changes begin. | 既存PRの日本語説明だけ直して。 |
| 入口 | `codebase-design-audit` | implicit | Audit existing code for design issues grounded in concrete files. | 新機能をまだコードなしで設計したい。 |
| 入口 | `architecture-drift-review` | implicit | Compare documented intent with current code behavior. | ADRをゼロから作って。 |
| 入口 | `human-decision-separator` | routed/explicit | Prevent the agent from silently deciding product, business, or organizational facts. | 単純なtypoを直して。 |
| DDD戦略 | `ubiquitous-language-mining` | routed/explicit | Extract domain vocabulary grounded in source artifacts. | 集約のトランザクション境界だけ判断して。 |
| DDD戦略 | `subdomain-classification` | routed/explicit | Classify subdomain candidates with uncertainty visible. | Domain Eventのpayloadだけ決めたい。 |
| DDD戦略 | `bounded-context-design` | implicit | Design model and language boundaries across a system. | 単一Value Objectの型設計だけ見て。 |
| DDD戦略 | `context-map-design` | routed/explicit | Map relationships between bounded contexts and external systems. | 単一Aggregateの不変条件だけレビューして。 |
| DDD戦略 | `domain-message-flow-modeling` | routed/explicit | Make domain message flow explicit across contexts or modules. | Value Objectの型だけ決めたい。 |
| DDD戦術 | `domain-building-blocks` | implicit | Choose appropriate DDD tactical building blocks without forcing DDD on simple code. | システム全体をマイクロサービスにすべきか相談したい。 |
| DDD戦術 | `domain-primitive-design` | routed/explicit | Make invalid states harder to represent with typed values. | Context Mapを作りたい。 |
| DDD戦術 | `aggregate-design` | implicit | Design aggregates as consistency boundaries, not table groups. | Clean Architecture の層構造だけ見て。 |
| DDD戦術 | `aggregate-transaction-boundary` | routed/explicit | Evaluate consistency and transaction boundaries around aggregates. | APIのversioningだけ相談したい。 |
| DDD戦術 | `cross-aggregate-consistency` | routed/explicit | Clarify whether a cross-aggregate rule is a true invariant or a policy. | Repositoryをどの層に置くかだけ決めたい。 |
| DDD戦術 | `repository-design-and-placement` | routed/explicit | Design repository contracts around aggregate or use-case needs. | Context Mapを作って。 |
| DDD戦術 | `domain-service-vs-application-service` | routed/explicit | Separate business rules from orchestration and side effects. | APIの互換性だけレビューして。 |
| DDD戦術 | `domain-event-design` | routed/explicit | Separate domain events from integration and stored events. | Package分割をレビューして。 |
| Architecture | `architecture-style-decision` | implicit | Compare architecture styles against project constraints. | Clean Architecture 採用済みなので層違反だけ見て。 |
| Architecture | `clean-architecture-review` | implicit | Review Clean Architecture compliance only when Clean Architecture is explicit. | 一般的にどのアーキテクチャが良いか相談したい。 |
| Architecture | `ports-and-adapters-boundary` | routed/explicit | Review port and adapter boundaries without confusing them with Clean Architecture enforcement. | Clean Architecture採用済みの層だけ見て。 |
| Architecture | `package-module-design` | implicit | Improve package and module boundaries based on change reasons and ownership. | ドメインイベントのpayloadだけ決めたい。 |
| Architecture | `dependency-direction-check` | routed/explicit | Check dependency direction with concrete import or reference evidence. | API contractを設計して。 |
| Architecture | `modular-monolith-boundary` | routed/explicit | Design modules inside a monolith with clear ownership and APIs. | CQRS採用判断だけしたい。 |
| Quality | `oo-design-principles` | routed/explicit | Apply OO principles as practical checks, not slogans. | Context Mapを作りたい。 |
| Quality | `information-hiding-deep-modules` | routed/explicit | Evaluate modules by interface simplicity versus implementation depth. | 集約境界を設計したい。 |
| Quality | `error-handling-design` | implicit | Design consistent error semantics across layers and interfaces. | 集約境界の不変条件だけ見て。 |
| Quality | `api-interface-design` | implicit | Shape stable APIs and module interfaces around explicit contracts. | packageの循環依存だけ検出して。 |
| Quality | `refactoring-planner` | implicit | Turn design debt into a staged, behavior-preserving refactoring plan. | 新規機能のAPIをゼロから設計したい。 |
| Quality | `test-strategy-for-design` | routed/explicit | Connect design choices to concrete verification. | ADR本文だけ生成して。 |
| System | `cqrs-decision` | implicit | Evaluate CQRS as a trade-off, not a default pattern. | Aggregateの不変条件だけ整理したい。 |
| System | `event-sourcing-decision` | implicit | Evaluate Event Sourcing based on concrete business and audit needs. | APIのDTO設計だけしたい。 |
| System | `data-modeling-review` | routed/explicit | Review persistence and read models against domain ownership and use cases. | OO原則だけでクラスレビューして。 |
| System | `distributed-consistency-review` | routed/explicit | Design for realistic distributed failure modes. | 単一Value Objectの設計だけ見たい。 |
| System | `observability-operability-review` | routed/explicit | Review whether a design can be operated after release. | DDD用語だけ抽出したい。 |
| Output | `adr-writer` | implicit | Turn a design decision into a durable ADR. | 実装前の設計レビューだけして。 |
| Output | `design-memo-writer` | implicit | Create a practical design memo for near-term implementation. | 正式なADRとして番号付きで残したい。 |
| Output | `decision-canvas-filler` | routed/explicit | Turn design evidence into a structured canvas. | 発火境界のevalだけ作りたい。 |
| Meta | `software-design-skill-forge` | implicit | Create or improve Software Design Skills using Skill-Creator as the governing workflow. | アプリの設計自体をレビューして。 |
| Meta | `skill-eval-and-trigger-boundary` | routed/explicit | Evaluate whether a Skill fires for the right prompts and stays silent for adjacent prompts. | アプリのDDD設計をレビューして。 |

## Common Combinations

- New feature preflight: `pre-implementation-design-review` + `api-interface-design` + `test-strategy-for-design`.
- Existing code audit: `codebase-design-audit` + `package-module-design` + `error-handling-design`.
- DDD aggregate work: `aggregate-design` + `aggregate-transaction-boundary` + `cross-aggregate-consistency`.
- Context design: `bounded-context-design` + `ubiquitous-language-mining` + `context-map-design`.
- Refactoring: `refactoring-planner` + `test-strategy-for-design` + the relevant boundary skill.
- Skill authoring: `software-design-skill-forge` + Skill-Creator + `skill-eval-and-trigger-boundary`.
