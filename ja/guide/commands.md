# CLI Commands

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/guide/commands)



Examples use the `commander` binary (available after building `@commander/core`).  
From a source checkout without a build, replace `commander` with:

```bash
npx tsx packages/core/src/cliEntry.ts
```

## Task Execution


| Command | Description |
|---------|-------------|
| `commander <task>` | Quick task analysis |
| `commander run <task>` | Full multi-agent execution pipeline |
| `commander plan <task>` | Show deliberation plan (topology, agents, budget) |
| `commander run <task> --stream` | Execute with real-time SSE event stream |
| `commander run --file <tasks.json>` | Batch process multiple tasks |
| `commander swarm <task>` | Recursive decomposition with parallel execution |
| `commander drive <task>` | Autonomous step-by-step execution |
| `commander goal <task>` | Multi-round convergence loop |
| `commander company <task>` | Enterprise pipeline with quality gates and memory |

## Interface


| Command | Description |
|---------|-------------|
| `commander gui` | Agent War Room dashboard (React + API server) |
| `commander tui` | Terminal dashboard with live event feed |
| `commander web` | Start web interface |

## Analysis & Planning


| Command | Description |
|---------|-------------|
| `commander review [--commit\|--base\|--json]` | Code review with guidelines (P0-P3 findings) |
| `commander workers [topics]` | Parallel research workers |
| `commander status` | System status, provider, MetaLearner stats |
| `commander cost` | Cost analysis and breakdown |

## 設定


| Command | Description |
|---------|-------------|
| `commander mode [mode]` | Set approval mode (plan/read-only/auto-edit/full-auto/suggest) |
| `commander config` | View or change settings |
| `commander doctor` | Run diagnostics |
| `commander budget` | Token budget management |
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

## Saga & Recovery


| Command | Description |
|---------|-------------|
| `commander saga` | Saga transaction operations |
| `commander checkpoint` | Checkpoint operations |
| `commander compensation` | Compensation registry operations |
| `commander resume` | Resume a paused or interrupted run |
| `commander undo` | Undo last operation via compensation |

## 高度な話題


| Command | Description |
|---------|-------------|
| `commander connect` | Connect to providers |
| `commander plan --topology <name>` | Force specific topology |
| `commander run --agent-count <n>` | Override agent count |
| `commander plugin enable <name>` | Enable a plugin (e.g., `rag`) |
| `commander plugin disable <name>` | Disable a plugin |
| `commander intelligence` | View intelligence metrics and patterns |

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

# Or at runtime (from monorepo source)
npx tsx packages/core/src/cliEntry.ts mode plan

# After building @commander/core
commander mode plan
```
