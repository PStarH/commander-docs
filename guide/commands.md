# CLI Commands

## Task Execution

| Command | Description |
|---------|-------------|
| `commander <task>` | Quick task analysis |
| `commander run <task>` | Full multi-agent execution pipeline |
| `commander plan <task>` | Show deliberation plan (topology, agents, budget) |
| `commander watch <task>` | Execute with real-time SSE event stream |
| `commander run --file <tasks.json>` | Batch process multiple tasks |

## Interface

| Command | Description |
|---------|-------------|
| `commander gui` | Agent War Room dashboard (React + API server) |
| `commander tui` | Terminal dashboard with live event feed |
| `commander web` | Start web interface |

## Analysis & Planning

| Command | Description |
|---------|-------------|
| `commander company <task>` | Company mode — multi-agent with review |
| `commander review [--commit\|--base\|--json]` | Code review with guidelines |
| `commander workers [topics]` | Parallel research workers |
| `commander benchmark <config> [options]` | Run benchmarks |
| `commander status` | System status, provider, MetaLearner stats |

## Configuration

| Command | Description |
|---------|-------------|
| `commander mode [mode]` | Set approval mode (plan/read-only/auto-edit/full-auto/suggest) |
| `commander config` | View or change settings |
| `commander doctor` | Run diagnostics |
| `commander --debug` | Enable verbose logging across all 74+ modules |

## Skills

| Command | Description |
|---------|-------------|
| `commander skill list` | List all available skills |
| `commander skill view <name>` | View skill content |
| `commander skill create <name>` | Create a new skill |
| `commander skill pin <name>` | Pin a skill (always loaded) |

## Session Management

| Command | Description |
|---------|-------------|
| `commander history` | View session history |
| `commander history view <id>` | View specific session |
| `commander history prune` | Remove old sessions |
| `commander history delete <id>` | Delete a session |
| `commander share` | Share a session link |

## Advanced

| Command | Description |
|---------|-------------|
| `commander connect` | Connect to providers |
| `commander plan --topology <name>` | Force specific topology |
| `commander run --agent-count <n>` | Override agent count |

## Benchmark Runner

```bash
commander benchmark gaia.yaml                       # Run GAIA benchmark
commander benchmark config.yaml --parallel 5         # 5 concurrent requests
commander benchmark config.yaml --output ./results   # Custom output dir
commander benchmark --list                           # List available configs
```

## Approval Modes

| Mode | Behavior |
|------|----------|
| `plan` | Show plan only, no execution |
| `read-only` | Read files, no edits |
| `auto-edit` | Automatic edits without approval |
| `full-auto` | Fully autonomous operation |
| `suggest` | Suggest changes, wait for approval |

```bash
# Set mode globally
export COMMANDER_MODE=auto-edit

# Or at runtime
npx tsx cli.ts mode plan
```
