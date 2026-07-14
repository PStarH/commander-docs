# API 参考

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/api/overview)



Commander has **two layers** of API surface. Most apps only need Layer 1.

## 第 1 层 — 公共集成（从这里开始）


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

> **npm status:** packages are monorepo-first; public publish is in progress. See [Agent SDK](/zh/guide/sdk).

### HTTP（服务端）


```bash
curl http://localhost:4000/health
curl http://localhost:4000/metrics

curl -X POST http://localhost:4000/execute \
  -H "Authorization: Bearer $COMMANDER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"task":"analyze this repository","mode":"plan"}'
```

Architecture V2 durable API: `POST /v1/runs` — see [V2 Migration](/zh/guide/migration-v2).

### Python


```python
from commander import CommanderClient
# thin httpx client → API server
```

[Python SDK](/zh/guide/sdk-python).

---

## 第 2 层 — 运行时编排组件


These modules power deliberation, budgeting, memory, and verification inside `@commander/core`. Use them when **extending** the runtime — not for normal app integration.

| Component | Purpose |
|-----------|---------|
| [Task Complexity Analyzer](/zh/api/task-complexity-analyzer) | Score task → recommend topology |
| [Adaptive Orchestrator](/zh/api/adaptive-orchestrator) | Multi-agent plan + coordination |
| [Token Budget Allocator](/zh/api/token-budget-allocator) | Budget split across agents |
| [Three-Layer Memory](/zh/api/three-layer-memory) | Working · episodic · long-term |
| [Reflection Engine](/zh/api/reflection-engine) | Post-run evaluation |
| [Consensus Checker](/zh/api/consensus-checker) | Multi-model votes for high risk |
| [Inspector Agent](/zh/api/inspector-agent) | Health / issue detection |

### 何时使用第 2 层


- Building a custom topology or planner  
- Research / instrumentation of memory and consensus  
- Tests that isolate a single subsystem  

### 何时**不要**使用第 2 层


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

### 全局访问器


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

## 架构深度


Subsystem design (not method lists): [Architecture overview](/zh/architecture/overview), [Agent runtime](/zh/architecture/agent-runtime), [Verification](/zh/architecture/verification), [Security](/zh/guide/security).

## 相关指南


- [CLI commands](/zh/guide/commands)  
- [Web Console](/zh/guide/web-console)  
- [Cookbook](/zh/guide/cookbook/)  
