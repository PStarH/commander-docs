# Quick Start

Get Commander running in under a minute.

## One-Line Command

```bash
npx tsx cli.ts run "analyze this repository structure"
```

Make sure you have [Node.js 18+](https://nodejs.org/) and [pnpm](https://pnpm.io/installation) installed.

## Step-by-Step

### 1. Clone & Install

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

### 2. Set an API Key

Set any one of the supported provider keys:

```bash
export OPENAI_API_KEY=sk-...        # OpenAI / DeepSeek / GLM / MiMo
export ANTHROPIC_API_KEY=sk-ant-... # Anthropic Claude
export GOOGLE_API_KEY=...           # Google Gemini
```

See the full [providers list](/guide/providers).

### 3. Try It

```bash
# See the deliberation plan before execution
npx tsx cli.ts plan "refactor this module"

# Full multi-agent execution
npx tsx cli.ts run "write a FastAPI CRUD endpoint"

# Execute with real-time SSE streaming
npx tsx cli.ts watch "debug the failing test"
```

## Next Steps

- [Installation guide](/guide/installation) — Docker, production, and CI setup
- [Commands reference](/guide/commands) — all CLI commands
- [Architecture overview](/architecture/overview) — how Commander works under the hood
- [Agent SDK](/guide/sdk) — embed Commander in your own applications
