# スーパービジョンツリー

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/architecture/supervision-tree)



Commander implements an **Erlang/OTP-inspired supervision tree** for fault isolation. Instead of handling every possible error within an agent, agents crash and supervisors restart them automatically — the "Let It Crash" philosophy.

## Why Supervision Trees


Traditional error handling tries to catch and recover from every failure. This leads to complex, fragile code. Supervision trees flip the model: let agents crash, and have a supervisor restart them with fresh state.

Benefits:
- **Fault isolation** — One agent crash doesn't kill the system
- **Automatic recovery** — Supervisors restart failed agents without human intervention
- **Escalation** — If a child keeps crashing, the supervisor escalates to its parent
- **Graceful shutdown** — Supervisors shut down children in reverse start order

## Architecture


```
                    ┌──────────────────┐
                    │  Root Supervisor │
                    │  (strategy: one_for_one) │
                    └────────┬─────────┘
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │ Agent 1  │  │ Agent 2  │  │ Agent N  │
        │ (child)  │  │ (child)  │  │ (child)  │
        └──────────┘  └──────────┘  └──────────┘
```

## Restart Strategies


| Strategy | Behavior | Use when |
|----------|----------|----------|
| `one_for_one` | Restart only the crashed child | Children are independent |
| `one_for_all` | Restart ALL children | Children are co-dependent |
| `rest_for_one` | Restart crashed child + all children started after it | Children have startup order dependencies |

## 設定


```typescript
import { Supervisor } from '@commander/core';

const supervisor = new Supervisor({
  id: 'agent-pool',
  strategy: 'one_for_one',
  maxRestarts: 10,           // Max restarts across ALL children
  maxRestartIntervalMs: 60000, // Within this time window
  defaultShutdownMs: 5000,    // Graceful shutdown timeout
  publishEvents: true,        // Publish to message bus
});
```

## Adding Children


```typescript
const handle = await supervisor.startChild({
  id: 'agent-1',
  start: async () => {
    const runtime = await createAgentRuntime({ /* config */ });
    return {
      id: 'agent-1',
      isAlive: () => runtime.isRunning(),
      healthCheck: async () => runtime.healthCheck(),
    };
  },
  stop: async (handle) => {
    await runtime.shutdown();
  },
  shutdownMs: 10000,
  maxRestarts: 5,
  maxRestartIntervalMs: 30000,
});
```

## Restart Intensity


If a child restarts more than `maxRestarts` times within `maxRestartIntervalMs`, the supervisor itself crashes — escalating to its parent supervisor.

```
Agent crashes → Supervisor restarts (1/5)
Agent crashes → Supervisor restarts (2/5)
Agent crashes → Supervisor restarts (3/5)
Agent crashes → Supervisor restarts (4/5)
Agent crashes → Supervisor restarts (5/5)
Supervisor CRASHES → Parent supervisor restarts both
```

## Supervision Events


Supervisors publish events to the message bus:

| Event | Description |
|-------|-------------|
| `child_started` | Child successfully started |
| `child_crashed` | Child process crashed |
| `child_restarted` | Child restarted after crash |
| `child_stopped` | Child gracefully stopped |
| `supervisor_crashed` | Supervisor exceeded restart limit |
| `supervisor_recovered` | Supervisor recovered from crash |

```typescript
supervisor.onEvent((event) => {
  console.log(`[${event.type}] ${event.supervisorId}/${event.childId}: ${event.message}`);
});
```

## Health Checks


Supervisors can run periodic health checks on children:

```typescript
await supervisor.startChild({
  id: 'agent-1',
  start: async () => ({
    id: 'agent-1',
    isAlive: () => true,
    healthCheck: async () => {
      const healthy = await checkAgentHealth();
      return { healthy, issues: healthy ? [] : ['Agent not responding'] };
    },
  }),
});
```

## API リファレンス


### `Supervisor`


| Method | Description |
|--------|-------------|
| `startChild(spec)` | Start a new child |
| `stopChild(id, force?)` | Stop a child gracefully (or force-kill) |
| `restartChild(id)` | Restart a specific child |
| `getChildState(id)` | Get child state and history |
| `getSupervisionHistory()` | Get all supervision events |
| `shutdown()` | Graceful shutdown of all children |

### `ChildSpec`


| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `id` | `string` | required | Unique child ID |
| `start` | `() => Promise<ChildHandle>` | required | Factory function |
| `stop` | `(handle) => Promise<void>` | — | Graceful shutdown |
| `restartStrategy` | `RestartStrategy` | supervisor default | Override strategy |
| `shutdownMs` | `number` | `5000` | Shutdown timeout |
| `maxRestarts` | `number` | `5` | Max restarts in interval |
| `maxRestartIntervalMs` | `number` | `60000` | Restart window |
