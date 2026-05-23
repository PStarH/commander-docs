# Architecture Overview

Commander is a multi-agent orchestration engine that transforms a single task description into a structured execution plan across multiple agents, tools, and LLM providers.

## High-Level Flow

```
CLI / HTTP / SDK
  │
  ├─ deliberation.ts         Task analysis & topology selection
  ├─ effortScaler.ts         Scale agents (1-20) by complexity
  ├─ topologyRouter.ts       Route to optimal topology
  ├─ atomizer.ts             ROMA task decomposition
  │
  ├─ agentRuntime.ts         LLM → tools → verification → retry
  │   ├─ providers/          18 LLM providers
  │   ├─ toolResultCache.ts  SHA-256 caching per tenant
  │   ├─ stateCheckpointer.ts Crash-safe snapshots
  │   ├─ circuitBreaker.ts   Failure threshold → open circuit
  │   ├─ deadLetterQueue.ts  Unrecoverable error persistence
  │   ├─ compensationRegistry.ts Mutation tool rollback
  │   ├─ contextCompactor.ts Token-aware message compaction
  │   ├─ tokenGovernor.ts    Token budget enforcement
  │   └─ verificationLoop.ts Quality gates (5-stage)
  │
  ├─ agentHandoff.ts         Agent-to-agent handoff with inbox
  ├─ messageBus.ts           Pub/sub for inter-agent + system events
  ├─ metricsCollector.ts     Prometheus counters/gauges/histograms
  ├─ threeLayerMemory.ts     Working/Episodic/Long-term with embedding
  ├─ hallucinationDetector.ts Signal-based hallucination detection
  ├─ reflectionEngine.ts     Post-execution self-evaluation
  ├─ metaLearner.ts          Thompson Sampling + Reflexion
  │
  └─ pluginManager.ts        19 hook points for extensibility
```

## Package Structure

```
packages/core/src/
├── runtime/             ← Execution engine (49 files)
├── ultimate/            ← Orchestration engine (14 files)
├── tools/               ← 25+ built-in tools
├── sandbox/             ← Security profiles
├── selfEvolution/       ← Meta-learning
├── telos/               ← Token-efficient LLM orchestration
├── mcp/                 ← Model Context Protocol
└── ... core modules
```

## Key Design Principles

1. **Topology-first** — Commander analyzes the task structure before choosing how to execute it
2. **Provider-agnostic** — All 18 LLM providers share a unified interface
3. **Crash-safe** — Every step is checkpointed atomically; resume from any failure
4. **Observable by default** — Metrics, traces, and event streams on every execution
5. **Multi-tenant by design** — Isolation at every layer: storage, memory, rate limits, concurrency
