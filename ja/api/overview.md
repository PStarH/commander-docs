# API リファレンス

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/api/overview)



Commander has **two layers** of API surface. Most apps only need Layer 1.

## レイヤー 1 — 公開統合（ここから）


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

> **npm status:** packages are monorepo-first; public publish is in progress. See [Agent SDK](/ja/guide/sdk).

### HTTP (server)


```bash
curl http://localhost:4000/health
curl http://localhost:4000/metrics

curl -X POST http://localhost:4000/execute \
  -H "Authorization: Bearer $COMMANDER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"task":"analyze this repository","mode":"plan"}'
```

Architecture V2 durable API: `POST /v1/runs` — see [V2 Migration](/ja/guide/migration-v2).

### Python


```python
from commander import CommanderClient
# thin httpx client → API server
```

[Python SDK](/ja/guide/sdk-python).

---

## レイヤー 2 — ランタイム編成コンポーネント


These modules power deliberation, budgeting, memory, and verification inside `@commander/core`. Use them when **extending** the runtime — not for normal app integration.

| Component | Purpose |
|-----------|---------|
| [Task Complexity Analyzer](/ja/api/task-complexity-analyzer) | Score task → recommend topology |
| [Adaptive Orchestrator](/ja/api/adaptive-orchestrator) | Multi-agent plan + coordination |
| [Token Budget Allocator](/ja/api/token-budget-allocator) | Budget split across agents |
| [Three-Layer Memory](/ja/api/three-layer-memory) | Working · episodic · long-term |
| [Reflection Engine](/ja/api/reflection-engine) | Post-run evaluation |
| [Consensus Checker](/ja/api/consensus-checker) | Multi-model votes for high risk |
| [Inspector Agent](/ja/api/inspector-agent) | Health / issue detection |

### When to use Layer 2


- Building a custom topology or planner  
- Research / instrumentation of memory and consensus  
- Tests that isolate a single subsystem  

### When **not** to use Layer 2


- Product features that only need “run this task” → use `CommanderClient`  
- Remote multi-language clients → use HTTP  

### Minimal Layer 2 example


```typescript
import {
  TaskComplexityAnalyzer,
  AdaptiveOrchestrator,
  TokenBudgetAllocator,
} from '@commander/core';

const analyzer = new TaskComplexityAnalyzer();
const complexity = analyzer.analyze({
  id: 'task-1',
  description: 'Build distributed logging system',
  riskLevel: 'high',
});

const allocator = new TokenBudgetAllocator({ baseBudget: 100_000 });
const budget = allocator.allocate(
  complexity.recommendedTopology,
  complexity.score,
  3,
);

const orchestrator = new AdaptiveOrchestrator();
orchestrator.registerAgent({
  id: 'lead',
  name: 'Lead',
  role: 'architect',
  capabilities: [],
});

const plan = orchestrator.createPlan(
  [{ id: 'task-1', description: '...', complexity: complexity.score }],
  complexity.recommendedTopology,
);
```

### グローバルアクセサ


Some components expose process singletons (used by the runtime/SDK helpers):

- `getGlobalTaskComplexityAnalyzer()`
- `getGlobalAdaptiveOrchestrator()`
- `getGlobalTokenBudgetAllocator()`
- `getGlobalThreeLayerMemory()`
- `getGlobalReflectionEngine()`
- `getGlobalConsensusChecker()`
- `getGlobalInspectorAgent()`

Prefer `CommanderClient` unless you are sure you need process-wide shared state.

---

## Architecture depth


Subsystem design (not method lists): [Architecture overview](/ja/architecture/overview), [Agent runtime](/ja/architecture/agent-runtime), [Verification](/ja/architecture/verification), [Security](/ja/guide/security).

## 関連ガイド


- [CLI commands](/ja/guide/commands)  
- [Web Console](/ja/guide/web-console)  
- [Cookbook](/ja/guide/cookbook/)  
