# 生产就绪

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/architecture/production-readiness)



Commander is designed for production from day one. Every component includes observability, safety, and reliability features.

## Feature Matrix


| Capability | Commander Status |
|------------|-----------------|
| **Type safety** | TypeScript strict mode, **zero** `as any` / `@ts-ignore` (ESLint error) |
| **Error handling** | **Zero** empty catch blocks across 100+ modules |
| **Metrics** | Unified MetricsCollector with Prometheus/OpenMetrics counters, gauges, histograms + tenant labels |
| **Tracing** | Span-based execution with persistent trace store, OpenTelemetry export |
| **Crash safety** | Atomic SQLite WAL checkpoints at every step + event sourcing hash chain |
| **Circuit breaker** | 5 failures → 30s open → half-open recovery, per-provider registry |
| **Dead letter queue** | 7 categories, 15 failure modes, persistent storage with replay support |
| **Multi-tenancy** | Per-tenant rate limits, concurrency quota, storage isolation, cache isolation |
| **Security** | 7-layer EnterpriseSecurityGateway, DLP, capability tokens, Bearer auth, CORS, rate limiting |
| **Observability** | Health check, readiness probe, OpenAPI spec, SSE streaming, Grafana dashboards |
| **Event sourcing** | WAL with SHA-256 hash chain, snapshot recovery, deterministic replay |
| **Plugin sandboxing** | Third-party plugins restricted via sandboxed load context; permissions never exceed main system |

## Safety Mechanisms


### Circuit Breaker

After 5 consecutive failures, the circuit opens for 30 seconds, then transitions to half-open for recovery. The `CircuitBreakerRegistry` manages breakers for all active providers.

### Dead Letter Queue

Unrecoverable errors are persisted across 7 categories (llm, tool, execution, verification, circuit_breaker, compensation, semantic_drift) with 15 standardized failure modes. Supports replay after root cause is fixed.

### Compensation Registry

Failed mutation tools trigger automatic rollback via registered compensation actions. Integrated with Saga coordinator for distributed transactions.

### State Checkpointer

Every step saves an atomic checkpoint using SQLite with WAL mode (synchronous=NORMAL, busy_timeout=5000). Resume from any failure without data loss.

### Event Sourcing Engine

Write-Ahead Log with SHA-256 hash chain provides tamper-proof event logging. All non-deterministic inputs (timestamps, random values, LLM responses, tool results) are recorded for deterministic replay.

### Recovery Bootstrapper

On process startup, scans for zombie runs (EXECUTING/VERIFYING/PAUSED states), acquires fencing lease, and either resumes from checkpoint or aborts with compensation.

## Observability


### Metrics (Prometheus / OpenMetrics)

```typescript
getMetricsCollector().exportOpenMetrics()
// Exports: counters, gauges, histograms with tenant labels
```

### Tracing

Span-based execution traces with persistent storage in `TraceStore`. OpenTelemetry export with PII redaction (auto-strips `gen_ai.prompt`, `gen_ai.completion`, `gen_ai.tool.call.arguments` from spans).

### Health Endpoints

- `/health` — Liveness probe
- `/ready` — Readiness probe
- `/metrics` — Prometheus metrics
- `/health/detailed` — Component-level health (circuit breaker, DLQ, compensation, event bus, provider, event sourcing)

### Grafana Dashboards

Pre-configured dashboards for two audiences:
- **Developer view**: Run success rate, P95 latency, token cost, active runs, tool call success rate
- **Mechanistic view**: WAL write latency, WAL file size, DLQ backlog, circuit breaker state, event backlog ratio, SQLite lock contention, compensation execution rate

## Testing


Commander maintains **zero tolerance for failures**:

- 6700+ tests across unit, integration, chaos, and e2e
- Chaos-monkey tests for fault injection
- Multi-tenant isolation tests (28 scenarios)
- Plugin permission tests (47 scenarios for sandbox enforcement)
- Stress tests: 10K messages, 50 concurrent calls
- Coverage thresholds: statements 60%, functions 70%, lines 60%

```
npx tsx --test tests/*.test.ts   # All green, # fail 0
npx tsc --noEmit                  # Zero type errors
```
