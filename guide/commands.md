# Commands

| Command | Description |
|---------|-------------|
| `commander <task>` | Quick task analysis |
| `commander run <task>` | Full multi-agent execution pipeline |
| `commander plan <task>` | Show deliberation plan (topology, agents, budget) |
| `commander watch <task>` | Execute with real-time SSE event stream |
| `commander gui` | Agent War Room dashboard (React + API server) |
| `commander tui` | Terminal dashboard with live event feed |
| `commander history [view\|prune\|delete]` | Session management |
| `commander workers [topics]` | Parallel research workers |
| `commander company <task>` | Company mode with review |
| `commander review [--commit\|--base\|--json]` | Code review with guidelines |
| `commander mode [mode]` | Set approval mode |
| `commander skill [list\|view\|create\|pin]` | Manage learnable skills |
| `commander status` | System status, provider, MetaLearner stats |
| `commander config` | View or change settings |
| `commander doctor` | Run diagnostics |
| `commander --debug` | Enable verbose logging across all 74+ modules |

## Approval Modes

| Mode | Behavior |
|------|----------|
| `plan` | Show plan only, no execution |
| `read-only` | Read files, no edits |
| `auto-edit` | Automatic edits without approval |
| `full-auto` | Autonomous operation |
| `suggest` | Suggest changes, wait for approval |
