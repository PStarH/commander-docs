# API Reference

Commander exposes three integration surfaces. Pick the one that matches how you embed it.

## Surfaces

| Surface | Package / path | When to use |
|---------|----------------|-------------|
| **CLI** | `commander` / `packages/core/src/cliEntry.ts` | Terminal workflows, CI scripts |
| **TypeScript SDK** | `@commander/sdk` → `CommanderClient` | Embed runtime in a Node app |
| **HTTP API** | API server `:4000` | Language-agnostic clients, Web Console, Python SDK |

Deep architectural modules (resilience, security, event sourcing) live under [Architecture](/architecture/overview). This section documents the **orchestration building blocks** you will see in SDK traces and advanced customizations.

## TypeScript SDK (primary)

```typescript
import { CommanderClient, createClient } from '@commander/sdk';

// Explicit
const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const result = await client.run('audit this repo');
await client.disconnect();

// Or zero-config
const c = await createClient();
await c.run('explain the architecture');
await c.disconnect();
```

Full guide: [Agent SDK](/guide/sdk).

## HTTP API (server)

```bash
# Liveness
curl http://localhost:4000/health
curl http://localhost:4000/health/detailed
curl http://localhost:4000/readyz
curl http://localhost:4000/metrics
```

Start the stack with Docker (`API :4000`, Web `:3000`) or `pnpm gui` (API `:4000`, Web `:5173`). See [Deployment](/deployment).

## Orchestration components

These modules power deliberation, budgeting, memory, and verification. They are available from `@commander/core` for advanced integrations; most apps only need `CommanderClient.run()`.

| Component | Purpose |
|-----------|---------|
| [Task Complexity Analyzer](/api/task-complexity-analyzer) | Scores task complexity and recommends topology |
| [Adaptive Orchestrator](/api/adaptive-orchestrator) | Coordinates multi-agent plans and execution |
| [Token Budget Allocator](/api/token-budget-allocator) | Allocates and tracks token budgets |
| [Three-Layer Memory](/api/three-layer-memory) | Working · episodic · long-term memory |
| [Reflection Engine](/api/reflection-engine) | Post-run self-evaluation and patterns |
| [Consensus Checker](/api/consensus-checker) | Multi-model consensus for high-risk decisions |
| [Inspector Agent](/api/inspector-agent) | Health monitoring and issue detection |

## Minimal advanced workflow

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

console.log(complexity.recommendedTopology, budget, plan);
```

## Global accessors

Several components expose process-wide singletons (used by the runtime and SDK helpers):

- `getGlobalTaskComplexityAnalyzer()`
- `getGlobalAdaptiveOrchestrator()`
- `getGlobalTokenBudgetAllocator()`
- `getGlobalThreeLayerMemory()`
- `getGlobalReflectionEngine()`
- `getGlobalConsensusChecker()`
- `getGlobalInspectorAgent()`

Prefer `CommanderClient` unless you are extending the runtime itself.

## Related

- [CLI commands](/guide/commands)
- [Python SDK](/guide/sdk-python)
- [Providers](/guide/providers)
- [Production readiness](/architecture/production-readiness)
