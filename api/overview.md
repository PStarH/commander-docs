# API Reference

Commander has **two layers** of API surface. Most apps only need Layer 1.

## Layer 1 — Public integration (start here)

| Surface | Package / entry | Best for |
|---------|-----------------|----------|
| **CLI** | `commander` · `packages/core/src/cliEntry.ts` | Terminal, scripts, CI |
| **TypeScript SDK** | `@commander/sdk` → `CommanderClient` | Embed in Node apps |
| **HTTP API** | Server `:4000` | Polyglot clients, Web Console |
| **Python SDK** | `commander-ai` (HTTP client) | Python against the API server |

### TypeScript SDK

```typescript
import { CommanderClient, createClient } from '@commander/sdk';

const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const result = await client.run('audit this repo');
console.log(result.status, result.summary);
await client.disconnect();

// or
const c = await createClient();
await c.run('explain the architecture');
await c.disconnect();
```

| Method | Role |
|--------|------|
| `connect` / `disconnect` | Lifecycle |
| `run(task)` | Full execution → `ExecutionResult` |
| `plan(task)` | Deliberation only |
| `onEvent(handler)` | Stream agent/tool events |
| `createAgent` / memory helpers | Advanced session control |

> **npm status:** packages are monorepo-first; public publish is in progress. See [Agent SDK](/guide/sdk).

### HTTP (server)

```bash
# Ops health server — default port 8081 (COMMANDER_OPS_HEALTH_PORT)
curl http://localhost:8081/health   # → 200 {"status":"ok"}
curl http://localhost:8081/ready    # → 200 (ready) / 503 (fail-closed)

# HTTP API base used by the Web Console client — default :4000 (VITE_API_BASE_URL).
# Requests carry `Authorization: Bearer <token>` when a token is configured.
curl http://localhost:4000/v1/actions \
  -H "Authorization: Bearer <token>"
```

Architecture V2 durable API: `POST /v1/runs` — see [V2 Migration](/guide/migration-v2).

### Python

```python
from commander import CommanderClient
# thin httpx client → API server
```

[Python SDK](/guide/sdk-python).

---

## Layer 2 — Runtime orchestration components

These modules power deliberation, budgeting, memory, and verification inside `@commander/core`. Use them when **extending** the runtime — not for normal app integration.

| Component | Purpose |
|-----------|---------|
| [Task Complexity Analyzer](/api/task-complexity-analyzer) | Score task → recommend topology |
| [Token Budget Allocator](/api/token-budget-allocator) | Budget split across agents |
| [Three-Layer Memory](/api/three-layer-memory) | Working · episodic · long-term |
| [Reflection Engine](/api/reflection-engine) | Post-run evaluation |
| [Consensus Checker](/api/consensus-checker) | Multi-model votes for high risk |

### When to use Layer 2

- Building a custom topology or planner  
- Research / instrumentation of memory and consensus  
- Tests that isolate a single subsystem  

### When **not** to use Layer 2

- Product features that only need “run this task” → use `CommanderClient`  
- Remote multi-language clients → use HTTP  

### Minimal Layer 2 example

```typescript
import { TaskComplexityAnalyzer } from '@commander/core';

const analyzer = new TaskComplexityAnalyzer();
const complexity = analyzer.analyze({
  id: 'task-1',
  description: 'Build distributed logging system',
  riskLevel: 'high',
});
// complexity: { level, score, factors, recommendedMode, tokenBudget, confidence }
```

Run-time budget splitting is handled internally by the token budget manager — see [Token Budget Allocator](/api/token-budget-allocator).

### Global accessors

Some components expose process singletons (used by the runtime/SDK helpers):

- `getGlobalThreeLayerMemory()`
- `getGlobalReflectionEngine()`
- `getGlobalLogger()` / `getGlobalMetrics()`
- `getGlobalTenantProvider()`
- `getGlobalMemoryRegistry()`

Prefer `CommanderClient` unless you are sure you need process-wide shared state.

---

## Architecture depth

Subsystem design (not method lists): [Architecture overview](/architecture/overview), [Agent runtime](/architecture/agent-runtime), [Verification](/architecture/verification), [Security](/guide/security).

## Related guides

- [CLI commands](/guide/commands)  
- [Web Console](/guide/web-console)  
- [Cookbook](/guide/cookbook/)  
