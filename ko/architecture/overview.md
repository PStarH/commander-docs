# Architecture Overview

**Architecture Overview.** Commander monorepo 구성 요소에 대한 한국어 운영 문서입니다. 코드·식별자는 영어를 유지하며, CLI는 `npx tsx packages/core/src/cliEntry.ts` 를 우선합니다. 제품 지표: 25 프로바이더 · 5 토폴로지 · 18 tools · 6700+ 테스트.

## 주요 섹션

### Read these five first

**Read these five first** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### High-Level Flow

**High-Level Flow** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Package Structure

**Package Structure** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Key Design Principles

**Key Design Principles** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

## 예제

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

## 운영 체크

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 관련

- [아키텍처 개요](/ko/architecture/overview)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [보안](/ko/guide/security)
- [빠른 시작](/ko/guide/getting-started)
