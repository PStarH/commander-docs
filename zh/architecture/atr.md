# Agent Transaction Runtime (ATR)

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/architecture/atr)



ATR is the **settlement layer** that sits between the agent's decision loop and every external system call. It guarantees that agent actions are idempotent, recoverable, leased, and fenced.

## Why ATR


Without ATR, agent execution is fire-and-forget: if a tool call succeeds but the agent crashes before recording the result, the action is lost. If the agent retries, the action executes twice. ATR solves this with transactional guarantees.

```
Agent Decision → ATR Settlement Layer → External System
                    ├── Idempotency (no duplicates)
                    ├── Recovery (compensable rollback)
                    ├── Leasing (single-owner runs)
                    └── Fencing (zombie process protection)
```

## Core Concepts


### Run Lifecycle


Every agent execution is a **run** with a well-defined state machine:

```
PENDING → EXECUTING → VERIFYING → COMMITTED
               │            │
               │            └──→ ABORTED → COMPENSATED
               └───────────────────→ ABORTED → COMPENSATED
```

- **PENDING** — Run created, not yet started
- **EXECUTING** — Agent is actively working
- **VERIFYING** — Post-execution verification (quality gates)
- **COMMITTED** — Terminal success
- **ABORTED** — Run failed or was cancelled
- **COMPENSATED** — All side effects rolled back
- **PAUSED** — HITL approval or budget halt (can resume)

### Idempotency


Every external action gets a SHA-256 idempotency key. Retries with the same key return the cached result instead of re-executing.

```typescript
import { IdempotencyStore } from '@commander/core';

const store = new IdempotencyStore({ ttlSeconds: 3600 });

// First execution — runs the action
const result = await store.execute('github:create-pr:abc123', async () => {
  return await github.createPR({ title: 'Fix bug', body: '...' });
});

// Retry with same key — returns cached result, no side effect
const cached = await store.execute('github:create-pr:abc123', async () => {
  return await github.createPR({ title: 'Fix bug', body: '...' });
});
```

### Leasing & Fencing


Only one process can own a run at a time. The lease includes a **fencing epoch** — a monotonically increasing counter that rejects stale operations from zombie processes.

```typescript
import { LeaseManager } from '@commander/core';

const leaseMgr = new LeaseManager();

// Acquire lease before mutating a run
const lease = await leaseMgr.acquire({
  runId: 'run-123',
  holder: `host:${process.pid}`,
  ttlMs: 30000,
});

// All mutations must present the lease token
await leaseMgr.heartbeat(lease.token);

// On completion, release the lease
await leaseMgr.release(lease.token);
```

### Compensable Actions


Every side effect is recorded as a **compensable action** with metadata for rollback:

```typescript
interface CompensableAction {
  actionId: string;
  runId: string;
  toolName: string;
  args: Record<string, unknown>;
  externalSystem: string;  // github, stripe, slack, db, fs, llm, mcp, shell
  idempotencyKey: string;
  compensable: boolean;
  tags: string[];  // e.g., ['destructive', 'github:pr']
}
```

If a run aborts, ATR walks the action list in reverse order and invokes registered compensation handlers for each compensable action.

## GitHub Adapter


ATR ships with a built-in GitHub adapter that provides compensable PR operations:

```typescript
import { createGitHubTools } from '@commander/core';

const tools = createGitHubTools({
  token: process.env.GITHUB_TOKEN,
  owner: 'my-org',
  repo: 'my-repo',
});

// Create a PR — ATR records it as compensable
const result = await tools.createPR({
  title: 'Feature X',
  body: 'Implements feature X',
  head: 'feature-x',
  base: 'main',
});

// If the run aborts, the PR is automatically closed
```

## HTTP API


ATR exposes HTTP endpoints for external integration:

```bash
# Start a new run
POST /atr/runs/start

# Record an action
POST /atr/runs/:runId/actions

# Finalize (commit or abort)
POST /atr/runs/:runId/finalize

# Query run status
GET /atr/runs/:runId
```

## 配置


| Setting | Default | Description |
|---------|---------|-------------|
| `idempotency.ttlSeconds` | `3600` | How long to retain idempotency records |
| `lease.ttlMs` | `30000` | Lease time-to-live |
| `lease.heartbeatMs` | `5000` | Heartbeat interval |
| `compensation.timeoutMs` | `10000` | Max time per compensation handler |

## Architecture


```
┌─────────────────────────────────────────────────┐
│                  ATR Kernel                      │
│                                                  │
│  ┌──────────────┐  ┌──────────────┐             │
│  │  Idempotency │  │    Lease     │             │
│  │    Store     │  │   Manager    │             │
│  └──────┬───────┘  └──────┬───────┘             │
│         │                  │                     │
│  ┌──────▼──────────────────▼───────┐            │
│  │         Run Ledger              │            │
│  │  (actions, state, compensation) │            │
│  └──────────────┬──────────────────┘            │
│                 │                                │
│  ┌──────────────▼──────────────────┐            │
│  │      Compensation Bridge        │            │
│  │  (handler registry + execution) │            │
│  └──────────────┬──────────────────┘            │
│                 │                                │
│  ┌──────────────▼──────────────────┐            │
│  │     Execution Scheduler         │            │
│  │  (commit / abort / kill)        │            │
│  └─────────────────────────────────┘            │
└─────────────────────────────────────────────────┘
```
