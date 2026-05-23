# Frequently Asked Questions

## General

### What is Commander?
Commander is a multi-agent orchestration engine that coordinates multiple AI agents across 8 different topologies (sequential, parallel, hierarchical, debate, ensemble, etc.), backed by 18 LLM providers and 25+ built-in tools.

### How is Commander different from other AI coding tools?
Most AI coding tools use a single agent with a single model. Commander orchestrates **multiple agents** across **any topology**, automatically selecting the best execution strategy based on task complexity. It's also production-grade from day one — circuit breakers, multi-tenancy, crash-safe checkpoints, Prometheus metrics.

### Is Commander open source?
Yes. Commander is MIT licensed.

### What does "multi-agent orchestration" mean?
Commander can spawn multiple AI agents that work together on a single task. Depending on the topology, they might work in parallel, debate each other's answers, or follow a lead architect who delegates to specialists.

## Setup

### Do I need multiple API keys?
No. **One key is enough**. Set `OPENAI_API_KEY` and Commander can auto-detect and fall back between OpenAI, DeepSeek, GLM, and MiMo. For other providers, set their respective key.

### Can I run Commander locally without internet?
Yes, if you use local models via Ollama or vLLM:
```bash
export OLLAMA_HOST=http://localhost:11434
npx tsx cli.ts run "analyze this code"
```

### Does Commander work with my existing subscriptions?
Yes. If you have GitHub Copilot or ChatGPT Plus/Pro, you can use those subscriptions as your provider.

## Usage

### Can Commander edit my files?
By default, yes — but you can control this with approval modes:
- `plan` — Show plan only
- `read-only` — Read files, no edits
- `suggest` — Suggest changes, wait for approval
- `auto-edit` — Edit automatically
- `full-auto` — Fully autonomous

### Can I run Commander in CI/CD?
Yes. Use `full-auto` mode:
```bash
export COMMANDER_MODE=full-auto
npx tsx cli.ts run "fix all lint errors"
```

### How many agents does Commander use?
1–20 agents depending on task complexity. Simple tasks get 1 agent, complex research tasks get a full team.

## Performance

### How accurate is Commander?
See the [benchmarks](/benchmarks) page:
- **GAIA**: 69.7% (+48.5 pp over bare LLM)
- **BFCL**: 91.4% parameter accuracy
- **PinchBench**: 97.7% (42/43 tasks)
- **HumanEval+**: 91.5%

### Is Commander fast?
Very. Most simple tasks complete in under 5 seconds. Complex multi-agent tasks typically take 30–60 seconds. Commander uses aggressive caching (SHA-256, per-tenant) to avoid redundant work.

## Enterprise

### Does Commander support multi-tenancy?
Yes. Per-tenant rate limits, concurrency quotas, storage isolation, memory sandboxing, and API key mapping. See [Multi-Tenancy](/architecture/multi-tenancy).

### Can I deploy Commander on-premise?
Yes. Docker-based deployment works on any Linux VM. See [Deployment](/deployment).

### Is there a paid tier?
The open-source version is fully featured and free. Cloud tiers (Starter $49/mo, Pro $199/mo, Enterprise custom) add managed hosting, SSO, audit logs, and dedicated support. See [Community](/community) for the roadmap.

## Data & Privacy

### Does Commander store my code?
No. Commander runs locally and does not store your code or context data. All processing stays on your machine (when using local models) or is sent only to the LLM provider you configure.

### Can I use Commander with sensitive code?
Yes. Use local models (Ollama, vLLM) or configure a VPC deployment. No code leaves your environment.
