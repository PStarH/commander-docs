# Frequently Asked Questions

## General

### What is Commander?

Commander is a multi-agent orchestration engine that coordinates multiple AI agents across 5 canonical topologies (single, chain, dispatch, orchestrator, review), backed by 25 LLM providers and 18 built-in tools.

### How is Commander different from other AI coding tools?

Most AI coding tools use a single agent with a single model. Commander orchestrates **multiple agents** across **any topology**, automatically selecting the best execution strategy based on task complexity. It's production-oriented from day one — circuit breakers, multi-tenancy, crash-safe checkpoints, Prometheus metrics, and live SSE streaming.

### Is Commander open source?

Yes. Commander is MIT licensed.

### What does "multi-agent orchestration" mean?

Commander can spawn multiple AI agents that work together on a single task. Depending on the topology, they might work in parallel, review each other's answers, or follow a lead architect who delegates to specialists.

## Setup

### Do I need multiple API keys?

No. **One key is enough**. Set `OPENAI_API_KEY` (or Anthropic, DeepSeek, Groq, …) and Commander auto-detects the provider. Failover chains kick in when you configure multiple keys.

### Can I run Commander locally without internet?

Yes, with local models via Ollama or vLLM:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```

### Is the npm package available?

`@commander/core` and `@commander/sdk` are built for publish; public npm release is **in progress**. Until then, clone the monorepo and use workspace packages. See [Agent SDK](/guide/sdk).

## Usage

### Can Commander edit my files?

By default yes — control it with approval modes:

- `plan` — show plan only
- `read-only` — read files, no edits
- `suggest` — suggest changes, wait for approval
- `auto-edit` — edit automatically
- `full-auto` — fully autonomous

### Can I run Commander in CI/CD?

Yes. Use `full-auto` mode:

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors"
```

### How many agents does Commander use?

1–20 agents depending on task complexity. Simple tasks get 1 agent; complex research or engineering tasks get a full team.

### What are the five topologies?

| Topology | Use when |
|----------|----------|
| **SINGLE** | Simple, one-shot answers |
| **CHAIN** | Sequential pipeline steps |
| **DISPATCH** | Parallel specialists + synthesis |
| **ORCHESTRATOR** | Lead agent delegates to workers |
| **REVIEW** | Produce then critique / merge |

See [Topology Decision Tree](/guide/usage/topology-decision-tree).

## Performance

### Is Commander fast?

Simple tasks often complete in seconds. Complex multi-agent runs typically take tens of seconds to minutes depending on models and tools. Semantic caching (SHA-256 + similarity) reduces redundant LLM work.

## Enterprise

### Does Commander support multi-tenancy?

Yes. Per-tenant rate limits, concurrency quotas, storage isolation, memory sandboxing, and API key mapping. See [Multi-Tenancy](/architecture/multi-tenancy).

### Can I deploy Commander on-premise?

Yes. Docker-based deployment works on any Linux VM. See [Deployment](/deployment).

### Is there a paid tier?

The open-source version is fully featured and free. Managed cloud (SSO, hosted API, SLA) is on the [roadmap](/community).

## Data & Privacy

### Does Commander store my code?

Commander runs on your machine (or your server). It does not upload code to a Commander cloud by default. Content is only sent to the LLM providers **you** configure (unless you use fully local models).

### Can I use Commander with sensitive code?

Yes. Prefer Ollama/vLLM or a VPC deployment so no code leaves your environment.

## Related

- [Troubleshooting](/guide/troubleshooting)
- [Installation](/guide/installation)
- [Community](/community)
