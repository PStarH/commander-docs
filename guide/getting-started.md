# Quick Start

Get Commander running in under two minutes. One API key. No graph builders. No YAML.

## Prerequisites

- [Node.js 18+](https://nodejs.org/) (LTS recommended)
- [pnpm](https://pnpm.io/installation) 8+
- Any one LLM provider API key (OpenAI, Anthropic, DeepSeek, Groq, …)

## 1. Clone & install

```bash
git clone https://github.com/sampan/Commander.git
cd Commander
pnpm install
```

## 2. Set an API key

Commander auto-detects the provider from whichever key you set:

```bash
export OPENAI_API_KEY=sk-...
# or: ANTHROPIC_API_KEY / DEEPSEEK_API_KEY / GROQ_API_KEY / ...
```

See the full [providers list](/guide/providers).

## 3. Run a task

From the monorepo root (recommended while developing from source):

```bash
# See the deliberation plan before execution
npx tsx packages/core/src/cliEntry.ts plan "refactor the auth module"

# Full multi-agent execution
npx tsx packages/core/src/cliEntry.ts run "audit this repo for security vulnerabilities"

# Stream every agent thought, tool call, and quality gate
npx tsx packages/core/src/cliEntry.ts run "explain the architecture" --stream
```

After a local build (`pnpm --filter @commander/core build`), you can also use the `commander` binary:

```bash
commander run "audit this repo" --stream
```

## 4. Open the Web Console (optional)

```bash
pnpm gui
```

API on `:4000`, Web Console on `:5173` (or `:3000` via Docker Compose).

## What just happened?

Commander:

1. **Classified** the task (CODING / RESEARCH / ANALYSIS / FACTUAL)
2. **Picked** a topology (SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW)
3. **Ran** one or more agents with tools
4. **Verified** output through five quality gates

No black boxes — every decision is visible in the stream.

## Next steps

- [Installation](/guide/installation) — Docker, production, and CI setup
- [Commands](/guide/commands) — full CLI reference
- [Topology Decision Tree](/guide/usage/topology-decision-tree) — when each topology is chosen
- [Architecture overview](/architecture/overview) — how the runtime works
- [Agent SDK](/guide/sdk) — embed Commander in your own applications
