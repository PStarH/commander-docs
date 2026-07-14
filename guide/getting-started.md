# Quick Start

Get Commander running in about five minutes. One API key. No graph builders. No YAML.

## Success criteria

You are done when **all three** are true:

1. `pnpm install` finished without errors
2. You ran a task and saw **deliberation + topology** (plan or stream)
3. The process exited with a result (or a clear error from `doctor`, not a silent hang)

## Prerequisites

- **Node.js** 18+ (22 recommended)
- **pnpm** 8+ (9+ preferred — monorepo workspaces)
- Any one LLM API key (OpenAI, Anthropic, DeepSeek, Groq, …)

> Use **pnpm**, not npm alone — this is a multi-package monorepo.

## 5-minute checklist

### 1. Clone & install

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

Optional but recommended after install:

```bash
pnpm -r build
```

### 2. Set an API key

```bash
export OPENAI_API_KEY=sk-...
# or: ANTHROPIC_API_KEY / DEEPSEEK_API_KEY / GROQ_API_KEY / ...
```

Commander **auto-detects** the provider. Full list: [Providers](/guide/providers).

### 3. Plan (zero risk)

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
```

You should see complexity, topology, and agent allocation **without** mutating files.

### 4. Run with stream

```bash
npx tsx packages/core/src/cliEntry.ts run "explain the architecture of this repository" --stream
```

You should see live agent thoughts, tool calls, and quality gates.

### 5. (Optional) Web Console

```bash
pnpm gui
```

- API: `http://localhost:4000`
- Web: typically `http://localhost:5173` (dev) or `http://localhost:3000` (Docker)

See [Web Console](/guide/web-console).

### 6. (Optional) Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000
```

## After build: `commander` binary (optional)

Until packages are published to npm, prefer the monorepo entry:

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

After a local core build, a `commander` bin may be available from the workspace:

```bash
pnpm --filter @commander/core build
# then, from the monorepo (pnpm bin / package bin path):
commander run "audit this repo" --stream
```

## If something fails

| Symptom                                 | Fix                                                                                                                  |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `Provider not available`                | `echo $OPENAI_API_KEY` — key must be exported in **this** shell. Then `npx tsx packages/core/src/cliEntry.ts doctor` |
| `Cannot find module` / workspace errors | Run from repo root with **pnpm**, then `pnpm install` and `pnpm -r build`                                            |
| Hang / no output                        | Try `plan` first; set `COMMANDER_DEBUG=true`; check network / provider status                                        |
| Rate limited                            | Wait, lower concurrency (`COMMANDER_MAX_CONCURRENCY=1`), or add a second provider key                                |
| Circuit breaker open                    | Wait ~30s or `npx tsx packages/core/src/cliEntry.ts doctor --reset`                                                  |
| Offline only                            | Use Ollama: `export OLLAMA_BASE_URL=http://localhost:11434`                                                          |

Full guide: [Troubleshooting](/guide/troubleshooting).

## What just happened?

1. **Classified** the task (CODING / RESEARCH / ANALYSIS / FACTUAL)
2. **Picked** a topology (SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW)
3. **Ran** one or more agents with tools
4. **Verified** output through five quality gates

Details: [Topology Decision Tree](/guide/usage/topology-decision-tree) · [Architecture](/architecture/overview).

## Next paths

| Goal                 | Go to                                                           |
| -------------------- | --------------------------------------------------------------- |
| Real recipes         | [Cookbook](/guide/cookbook/)                                    |
| Why not framework X? | [Why Commander](/guide/why-commander)                           |
| Embed in TypeScript  | [Agent SDK](/guide/sdk)                                         |
| Ship to a VM         | [Deployment](/deployment) · [Installation](/guide/installation) |
| CLI reference        | [Commands](/guide/commands)                                     |
