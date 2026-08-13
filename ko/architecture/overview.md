# 아키텍처 개요

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/architecture/overview)



Commander is a multi-agent orchestration engine that transforms a single task description into a structured execution plan across multiple agents, tools, and LLM providers.

## 먼저 이 다섯 페이지


If you are new, this is enough to understand the system:

1. **This page** — high-level flow and package map  
2. [Core Call Chain](/ko/architecture/core-call-chain) — request → result path  
3. [Multi-Agent Orchestration](/ko/architecture/multi-agent) — topologies and coordination  
4. [Agent Runtime](/ko/architecture/agent-runtime) — LLM → tools → verify → retry  
5. [Verification Pipeline](/ko/architecture/verification) — five quality gates  

Everything else (reliability, security, systems) is optional depth — collapsed in the sidebar.

## 고수준 흐름


```
CLI / HTTP / SDK
  │
  ├─ deliberation.ts         Task analysis & topology selection
  ├─ effortScaler.ts         Scale agents (1-20) by complexity
  ├─ topologyRouter.ts       Route to optimal topology (5 canonical + 9 legacy)
  ├─ atomizer.ts             ROMA task decomposition
  │
  ├─ agentRuntime.ts         LLM → tools → verification → retry
  │   ├─ providers/          25 LLM providers with fallback chains
  │   ├─ toolResultCache.ts  SHA-256 caching per tenant
  │   ├─ stateCheckpointer.ts Crash-safe snapshots (SQLite WAL)
  │   ├─ circuitBreaker.ts   Failure threshold → open circuit
  │   ├─ deadLetterQueue.ts  7 categories, 15 failure modes, replay support
  │   ├─ compensationRegistry.ts Mutation tool rollback
  │   ├─ contextCompactor.ts Token-aware message compaction
  │   ├─ tokenGovernor.ts    Token budget enforcement
  │   ├─ verificationLoop.ts Quality gates (5-stage)
  │   ├─ eventSourcingEngine.ts WAL + hash chain event log
  │   └─ qualityGater.ts    Agent Capsules degradation detection
  │
  ├─ enterpriseSecurityGateway.ts  7-layer defense-in-depth
  │   ├─ dataLossPrevention.ts  DLP with 12+ sensitive patterns
  │   ├─ capabilityToken.ts   Short-lived HMAC auth tokens
  │   ├─ auditChainLedger.ts  Tamper-proof hash chain audit
  │   └─ agentLineage.ts      Immutable parent-child agent tracking
  │
  ├─ agentHandoff.ts         Agent-to-agent handoff with inbox
  ├─ messageBus.ts           Pub/sub for inter-agent + system events
  ├─ metricsCollector.ts     Unified metrics (Prometheus + adapters)
  ├─ threeLayerMemory.ts     Working/Episodic/Long-term with embedding
  ├─ hallucinationDetector.ts Signal-based hallucination detection
  ├─ reflectionEngine.ts     Post-execution self-evaluation
  ├─ metaLearner.ts          Thompson Sampling + Reflexion
  │
  ├─ recoveryBootstrapper.ts Zombie run detection & recovery on startup
  ├─ unifiedAuditLog.ts      Cross-source audit aggregation
  │
  └─ pluginManager.ts        19 hook points, sandboxed load context
```

## 패키지 구조


```
packages/core/src/
├── runtime/             ← Execution engine (190+ files)
├── ultimate/            ← Orchestration engine (44+ files)
├── security/            ← Enterprise security gateway (70+ files)
├── tools/               ← 18 built-in tools
├── sandbox/             ← Security profiles, TEE, seccomp, Petri net
├── atr/                 ← Agent Task Recovery system
├── selfEvolution/       ← Meta-learning
├── saga/                ← Distributed compensation transactions
├── mcp/                 ← Model Context Protocol + A2A
├── plugins/builtin/     ← RAG knowledge base plugin
└── ... core modules
```

## 핵심 설계 원칙


1. **Topology-first** — Commander analyzes the task structure before choosing how to execute it
2. **Provider-agnostic** — All 25 LLM providers share a unified interface with automatic fallback
3. **Crash-safe** — Every step is checkpointed atomically (SQLite WAL); resume from any failure via event sourcing replay
4. **Observable by default** — Metrics, traces, SSE event streams, and Grafana dashboards on every execution
5. **Multi-tenant by design** — Isolation at every layer: storage, memory, rate limits, concurrency, cache
6. **Secure by default** — 7-layer enterprise security gateway, DLP, capability tokens, plugin sandboxing
7. **Reversible by design** — Event sourcing with hash chain, compensation registry, DLQ replay, and RecoveryBootstrapper
