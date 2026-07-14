# Resilience

Commander includes a multi-layer resilience infrastructure that ensures availability, data safety, and recoverability in production.

## Circuit Breaker

Each LLM provider has its own circuit breaker with three states:

| State | Behavior |
|-------|----------|
| **CLOSED** | Normal operation. Requests pass through. |
| **OPEN** | After 5 consecutive failures. All requests are rejected immediately. Cooldown: 30 seconds. |
| **HALF-OPEN** | After cooldown. One test request is allowed. Success → CLOSED, failure → OPEN again. |

```typescript
const breaker = new CircuitBreaker({ threshold: 5, cooldownMs: 30000 });
breaker.onSuccess();    // Resets failure count
breaker.onFailure();    // Increments; opens circuit at threshold
breaker.isAvailable();  // false when OPEN
```

The `CircuitBreakerRegistry` manages breakers for all active providers, providing a single access point for health checks and metrics.

## Provider Fallback Chain

When a provider fails (circuit open, rate limited, or network error), Commander automatically falls through a configurable chain:

```typescript
const chain = new ProviderFallbackChain({
  providers: ['openai', 'anthropic', 'deepseek', 'groq'],
  timeoutMs: 30000,
});

const result = await chain.tryProviders(task);
// Tries OpenAI → Anthropic → DeepSeek → Groq
// Throws FallbackChainExhaustedError if all fail
```

The `llmRetry.ts` module classifies each error as retryable (rate limit, timeout) or permanent (auth failure, invalid request) to drive retry and fallback decisions.

## Crash-Safe Checkpoints

The `StateCheckpointer` saves execution state after every step using SQLite with WAL mode:

- SQLite WAL mode with `synchronous=NORMAL` and `busy_timeout=5000`
- Atomic write protocol via transactions
- Per-tenant isolation: each tenant has its own checkpoint directory
- Checkpoint manager tracks staleness for health monitoring

```typescript
const checkpointer = new StateCheckpointer({ basePath: '/data/checkpoints' });
await checkpointer.checkpoint({ runId, phase, stepNumber, messages, tokenUsage });
```

## Dead Letter Queue

Unrecoverable errors are persisted across **7 categories** with **15 standardized failure modes**:

| Category | Description |
|----------|-------------|
| `llm` | LLM call failures |
| `tool` | Tool execution failures |
| `execution` | Agent execution failures |
| `verification` | Quality gate failures |
| `circuit_breaker` | Circuit breaker trips |
| `compensation` | Compensation failures |
| `semantic_drift` | Semantic degradation detected |

```typescript
dlq.enqueue({
  error: new PermanentProviderError('Invalid API key'),
  context: { runId, provider, step },
  timestamp: Date.now(),
});

// Read methods call flush() first to ensure memory buffer is written to disk
const entries = dlq.readEntries();  // Review all entries
dlq.flush();                        // Clear processed entries
```

The DLQ supports replay: entries can be re-queued after the root cause is fixed. `listUnrecoveredEntries()` returns all retryable but unrecovered entries. A global singleton (`DeadLetterQueueSingleton`) provides application-wide access.

## Compensation Registry

Mutation tools (file writes, API calls) register compensation actions that undo their side effects. If a step fails, the registry executes all registered compensations:

```typescript
registry.register('file-write', {
  undo: async (ctx) => { await fs.unlink(ctx.filePath); },
});

// On failure: registry.compensate(runId) rolls back all mutations
```

Integrated with the Saga coordinator for distributed multi-step transactions.

## Event Sourcing Recovery

The `EventSourcingEngine` provides Write-Ahead Log (WAL) with SHA-256 hash chain for tamper-proof event logging:

- All non-deterministic inputs (timestamps, random values, LLM responses, tool results) are recorded
- Replay uses recorded values rather than recomputing
- Snapshot-based fast recovery with log compaction
- Hash chain integrity verification

### Recovery Strategy Priority

1. **Event replay recovery** — Full event log replay for complete state restoration
2. **Checkpoint recovery** — Resume from last valid checkpoint
3. **Abort + compensate** — Degrade gracefully with compensation

## Recovery Bootstrapper

On process startup, `RecoveryBootstrapper.bootstrap()` scans for zombie runs:

1. Scan `RunLedger` for EXECUTING, VERIFYING, PAUSED states
2. Cross-check lease expiry via `LeaseManager`
3. Acquire fencing lease (isolates any surviving zombie processes)
4. Recovery decision:
   - PAUSED + recoverable checkpoint → resume
   - EXECUTING/VERIFYING → abort + compensate (safe default)
   - No lease or already reclaimed → skip
5. Record DLQ entries for recovered runs
6. Publish recovery events to MessageBus

The bootstrapper is idempotent — concurrent process starts are safe.

## ATR System

The Agent Task Recovery (ATR) system provides infrastructure for run lifecycle management:

| Component | Purpose |
|-----------|---------|
| `RunLedger` | Tracks all run states (EXECUTING/VERIFYING/PAUSED/COMPLETED/FAILED) |
| `LeaseManager` | Fencing tokens for exclusive run ownership |
| `IdempotencyStore` | Prevents duplicate execution |
| `CheckpointStore` | SQLite-backed checkpoint persistence |
| `CompensationBridge` | Connects ATR to compensation registry |
| `GitSnapshot` | Git-based state snapshots for rollback |

## SLOs

| Capability | Target |
|------------|--------|
| Circuit breaker cooldown | 30 seconds |
| Provider failover | <10 seconds |
| Checkpoint recovery | <5 seconds |
| Compensation complete | <30 seconds |
| DLQ persistence | <60 seconds |
| Event sourcing replay | <10 seconds |
