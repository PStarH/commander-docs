# 이벤트 소싱 및 복구

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/architecture/event-sourcing)



Commander's event sourcing system provides crash-safe execution with tamper-proof audit trails, deterministic replay, and automatic zombie run recovery.

## EventSourcingEngine


The `EventSourcingEngine` implements the IEventSourcingEngine contract (Pillar I) with a Write-Ahead Log (WAL) and SHA-256 hash chain for tamper protection.

### Write-Ahead Log


Every event is atomically appended to the WAL file at `.commander_state/event-sourcing.wal` (configurable via `COMMANDER_EVENT_SOURCING_WAL`):

```
[event 1] → SHA256("") → hash_1
[event 2] → SHA256(hash_1 | type | id | timestamp | payload) → hash_2
[event 3] → SHA256(hash_2 | type | id | timestamp | payload) → hash_3
```

A write lock serializes appends to prevent hash chain corruption.

### Hash Chain Integrity


Each event's hash incorporates the previous event's hash, creating a tamper-evident chain. `verifyIntegrity()` recalculates all hashes to detect any tampering.

### Non-Deterministic Input Recording


All non-deterministic inputs are recorded in the event log and used during replay instead of recomputation:

- Timestamps (wall clock readings)
- Random values (UUIDs, salt generation)
- LLM responses (model output, token counts)
- Tool call results (external API responses)

This satisfies constraint IF-05 (deterministic event replay) — replaying the log produces identical state transitions.

### Snapshot & Compaction


- `snapshot()` — Creates a named snapshot for fast recovery without full log replay
- `compact()` — Removes events before a snapshot, rewrites the WAL to reclaim space
- `readFrom(snapshotId)` — AsyncIterable stream of events after a snapshot

### Health Monitoring


`EventSourcingHealth` monitors four metrics:

| Metric | Degraded | Unhealthy |
|--------|----------|-----------|
| WAL write latency (p95) | 50ms | 200ms |
| WAL file size | 100MB | 500MB |
| Event backlog ratio | 1000 | 10000 |
| Hash chain integrity | — | Any break |

Health data is exposed via `/health/detailed` and used by the background monitor and recovery pre-check.

### EventSourcingSubscriber


The subscriber pattern connects to MessageBus without侵入 the agentRuntime main loop:

- Subscribes to relevant system events
- Writes to the event log asynchronously
- Never blocks execution
- Graceful degradation if WAL is unavailable

## RecoveryBootstrapper


On process startup, `RecoveryBootstrapper.bootstrap()` automatically scans for zombie runs:

### Recovery Flow


1. **Scan RunLedger** — Find runs in EXECUTING, VERIFYING, or PAUSED state
2. **Lease check** — Cross-reference with LeaseManager for expired leases
3. **Acquire fencing lease** — Isolates any surviving zombie processes (holder: `recovery-{pid}`, TTL: 30s)
4. **Recovery decision**:
   - PAUSED + recoverable checkpoint → resume (caller takes ownership)
   - EXECUTING/VERIFYING → abort + compensate (safe default)
   - No lease or already reclaimed → skip (log only)
5. **Record DLQ entries** for recovered runs
6. **Publish recovery events** to MessageBus

### Idempotency


Two processes competing for startup will not conflict — the second discovers the lease is already acquired and skips. The `forceAbort` option forces abort+compensate for CI-safe scenarios.

### Recovery Result


```typescript
interface RecoveryResult {
  scanned: number;      // Total zombie runs found
  recovered: number;   // Successfully resumed
  aborted: number;      // Aborted with compensation
  skipped: number;      // Already handled by another process
  details: RecoveryDetail[];
}
```

## Recovery Strategy Priority


The system follows a strict priority order for recovery:

1. **Event replay recovery** — Full event log replay for complete state restoration (most accurate)
2. **Checkpoint recovery** — Resume from last valid checkpoint (fast, may lose recent state)
3. **Abort + compensate** — Degrade gracefully with compensation (safe fallback)

## Integration Points


| Component | Role |
|-----------|------|
| `RunLedger` | Source of truth for run states |
| `LeaseManager` | Fencing tokens for exclusive ownership |
| `CheckpointStore` | SQLite-backed checkpoint persistence |
| `DeadLetterQueue` | Records recovered/aborted runs |
| `MessageBus` | Publishes recovery events for subscribers |
| `CompensationBridge` | Triggers rollback for aborted runs |
