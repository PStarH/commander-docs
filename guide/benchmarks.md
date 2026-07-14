# Benchmarks

Commander is benchmarked across reliability, performance, chaos resilience, and topology efficiency. This page documents our benchmark methodology and results.

## Reliability SLO Targets

Design goals for v0.2.0. Implementation is complete; CI timing enforcement is scheduled for v0.3.0.

| Target | Goal | Implementation | CI-Measured |
|--------|------|----------------|:-----------:|
| **Checkpoint Recovery** | <5 seconds | SQLite WAL + in-memory cache layer | ❌ |
| **Failover** | <10 seconds | Provider fallback chain + circuit breaker | ❌ |
| **Compensation** | <30 seconds | Saga compensation scheduler | ❌ |
| **DLQ Processing** | <60 seconds | Append-only ndjson + replay | ❌ |

### Measurement Status

| Component | Module | Status |
|-----------|--------|--------|
| Checkpoint Recovery | `runtime/checkpointStore.ts` | ✅ Implemented, manual verification |
| Failover | `runtime/modelRouter.ts` + `saga/circuitBreakerRegistry.ts` | ✅ Implemented, manual verification |
| Compensation | `saga/compensationScheduler.ts` | ✅ Implemented, unit-tested |
| DLQ Processing | `runtime/deadLetterQueue.ts` | ✅ Implemented, unit-tested |

## Health Check Components

The `/health/detailed` endpoint monitors 8 components:

| Component | What it checks | Degraded when |
|-----------|---------------|---------------|
| **Memory** | Heap usage | >80% of available |
| **Circuit Breaker** | Open breakers | Any breaker in OPEN state |
| **Dead Letter Queue** | Queue size | >100 pending entries |
| **Checkpoint** | Staleness | Last checkpoint >60s ago |
| **Compensation** | Pending count | >10 pending compensations |
| **Event Bus** | Backlog | >1000 unprocessed events |
| **Providers** | Availability | Any provider unreachable |
| **Disk Space** | Free space | <1GB available |

## Chaos Engineering Benchmark

Commander's chaos benchmark validates resilience across 255 test cases covering 6 business domains and 3 mutation axes.

### Benchmark Overview

| Metric | Value |
|--------|-------|
| Total test cases | 255 |
| Synthetic scenarios | 200 |
| Real-world mutation cases | 55 |
| Real-world anchors | 47 |
| Anchor coverage | 74.5% |

### Business Domains

| Domain | Description |
|--------|-------------|
| **A: Leaderboard** | Real-time ranking with concurrent updates |
| **B: Matchmaking** | Multi-party matching with availability constraints |
| **C: UGC Pipeline** | User-generated content processing with moderation |
| **D: Push/Broadcast** | Notification delivery with rate limiting |
| **E: Virtual Currency** | Transaction processing with balance consistency |
| **F: Live Streaming** | Real-time streaming with adaptive bitrate |

### Mutation Axes

| Axis | What it tests |
|------|--------------|
| **Telemetry Gap (Fog of War)** | Missing observability data, blind spots in monitoring |
| **Stochastic/Gray Failure** | Intermittent failures, partial degradation |
| **Security-Stability Convergence** | Attacks that degrade stability, security-stability tradeoffs |

### Chaos Layers

| Layer | Fault Types | Recovery Mechanisms |
|-------|------------|---------------------|
| **L1: LLM** | Rate limits, timeouts, context overflow, malformed responses | Provider fallback chain |
| **L2: Tool** | http_5xx, http_4xx, disk_full, oom, process_crash, state_corrupt, dependency_unavailable, time_drift, auth_expired, http_timeout | Circuit breaker, DLQ, compensation |
| **L3: System** | CPU throttle, memory pressure, disk full | Checkpoint recovery, graceful degradation |
| **L4: Tenant** | Cross-tenant access, resource exhaustion | Tenant isolation, blast radius enforcement |

### Running the Benchmark

```bash
# Run full 255-case benchmark
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3,L4 --tenant=bench --duration=300

# Run specific domain
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2 --tenant=bench --fault-types=payment_timeout,rate_limit
```

## Topology Performance

Commander's 5 canonical topologies are optimized for different task profiles:

| Topology | Best For | Typical Latency | Agent Count |
|----------|----------|-----------------|-------------|
| **SINGLE** | Simple, well-defined tasks | <5s | 1 |
| **CHAIN** | Multi-step sequential transformations | 10–30s | 2–3 |
| **DISPATCH** | Independent parallel subtasks | 15–45s | 2–10 |
| **ORCHESTRATOR** | Complex decomposition with specialists | 30–120s | 3–8 |
| **REVIEW** | High-risk decisions needing validation | 30–120s | 2–5 |

### Topology Selection Criteria

The deliberation engine scores topologies based on:

| Factor | Weight | Impact |
|--------|--------|--------|
| Task type (CODING, RESEARCH, etc.) | High | Maps to topology strengths |
| DAG width (parallelism potential) | Medium | Favors DISPATCH |
| Critical path length | Medium | Favors CHAIN or ORCHESTRATOR |
| Coupling between subtasks | Medium | Favors SINGLE or CHAIN |
| Cost constraints | Low | Falls back to cheaper topology |

## Provider Latency

Typical latency characteristics (varies by region and load):

| Provider | Tier | Input Latency | Output Latency | Context Window |
|----------|------|---------------|----------------|----------------|
| OpenAI GPT-4o | Power | 200–500ms | 30–80ms/token | 128K |
| Anthropic Claude Sonnet | Power | 300–600ms | 40–90ms/token | 200K |
| DeepSeek Chat | Eco | 150–400ms | 20–60ms/token | 64K |
| Groq Llama 3 | Eco | 50–150ms | 10–30ms/token | 8K |
| Google Gemini 1.5 | Standard | 200–500ms | 30–70ms/token | 1M |

### Failover Chain

When a provider fails, Commander automatically falls through the configured chain:

```
Primary Provider → Timeout/Error → Circuit Breaker OPEN → Next Provider → ...
```

Failover time: typically <10 seconds (SLO target).

## Test Suite

| Category | Count | Command |
|----------|-------|---------|
| **Unit** | ~3000 | `pnpm --filter @commander/core test:quick` |
| **Core** | ~2000 | `pnpm --filter @commander/core test` |
| **Full** | 6700+ | `cd packages/core && npx vitest run --no-cache` |
| **Security** | 89 | `pnpm --filter @commander/core test:security` |
| **Integration** | 81 | `pnpm --filter @commander/core test:node:pathsec` |
| **Chaos** | 255 | `npx tsx packages/core/src/cli/commands/chaos.ts` |

### Coverage Thresholds

| Metric | Threshold |
|--------|-----------|
| Statements | 60% |
| Functions | 70% |
| Lines | 60% |

## Reproducing Benchmarks

```bash
# Clone and install
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install

# Run core tests
pnpm --filter @commander/core test

# Run chaos benchmark
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3,L4 --tenant=bench

# Run type check
cd packages/core && npx tsc --noEmit
```
