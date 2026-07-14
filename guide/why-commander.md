# Why Commander

Commander is for engineers who refuse to treat multi-agent systems as a black box.

**No graph builders. No YAML. No “hope the agents worked.”**  
Set one API key → classify task → pick topology → stream every decision → verify every output.

## At a glance

| Dimension | Commander | Typical agent frameworks |
|-----------|-----------|---------------------------|
| **How you start** | Plain-language task + one API key | Build a graph, write YAML/JSON workflows |
| **Topology** | 5 canonical topologies auto-selected (SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW) | You wire edges yourself |
| **Visibility** | Live SSE: thoughts, tools, quality gates | Logs after the fact, or opaque runs |
| **Quality** | 5-layer gates (hallucination, consistency, completeness, accuracy, safety) | Optional / DIY |
| **Providers** | 25 with auto-detect + failover | Often 1–2 first-class providers |
| **Production** | Circuit breakers, DLQ, saga, WAL checkpoints, multi-tenancy | Demo-first; ops bolted on later |
| **Embedding** | CLI, TypeScript SDK, HTTP API, Python client | Usually one surface |
| **Tests** | 6700+ | Varies widely |

## When to choose Commander

**Choose Commander if you:**

- Need to **see** what agents are doing while they run
- Want topology and agent count chosen for you, not hand-tuned every time
- Care about **failover**, checkpoints, and auditability in production
- Prefer CLI / SDK over a visual graph builder
- Run security-sensitive or multi-tenant workloads

**Consider something else if you:**

- Only need a single chat completion with tools
- Want a fully managed SaaS with no self-host (cloud is still on our [roadmap](/community))
- Prefer pure Python in-process frameworks with no Node runtime

## vs common approaches

### vs “single agent + tools” coding assistants

Coding assistants optimize for one model, one thread. Commander optimizes for **teams of agents**, automatic scale (1–20), and **verified** multi-step work. Use a coding assistant for quick edits; use Commander when the task needs parallel research, review, or orchestration.

### vs graph-based orchestrators (e.g. LangGraph-style)

Graph frameworks are powerful when you **want** to design every edge. Commander trades that for:

1. Deliberation that picks topology from task class + complexity  
2. Streaming observability by default  
3. Ops primitives (breakers, DLQ, compensation) without a separate platform layer  

You can still force topology and agent count when you need control.

### vs multi-agent “crew” libraries

Crew-style libraries shine at role prompts and collaboration patterns. Commander adds:

- Canonical topologies with decision tree guidance  
- Provider failover across 25 backends  
- Quality gates and production recovery paths  
- Web Console + HTTP API for ops, not only scripts  

## Proof points (honest)

| Claim | Where it lives |
|-------|----------------|
| 25 providers | [Providers](/guide/providers), `providerRegistry.ts` |
| 5 topologies | [Topology Decision Tree](/guide/usage/topology-decision-tree) |
| 18 built-in tools | [Tools](/architecture/tools) |
| 6700+ tests | CI / [Benchmarks](/guide/benchmarks) |
| Streaming | [Agent Runtime](/architecture/agent-runtime), `run --stream` / watch mode |
| Security posture | [Security](/guide/security) |

Benchmarks are reproducible scripts in the monorepo — not marketing screenshots. See [Benchmarks](/guide/benchmarks) for how to run them.

## 60-second taste

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "explain this repository architecture" --stream
```

Success looks like: deliberation classification → topology choice → agent steps → quality gates in the stream.

## Next

- [Quick Start](/guide/getting-started) — 5-minute checklist  
- [Cookbook](/guide/cookbook/) — end-to-end recipes  
- [Architecture overview](/architecture/overview) — how the engine works  
