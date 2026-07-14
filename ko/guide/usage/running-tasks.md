# 작업 실행

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/guide/usage/running-tasks)



Commander offers multiple ways to execute tasks depending on your needs.

> **CLI from source** (monorepo): `npx tsx packages/core/src/cliEntry.ts …`  
> **After build**: `commander …`  
> All examples below use the monorepo form.

## Quick Task


For simple requests where you want an immediate answer:

```bash
npx tsx packages/core/src/cliEntry.ts "what does this function do?"
```

Commander analyzes the task, selects the optimal topology, executes, and returns the result — all in one step.

## Full Execution Pipeline


For complex multi-step tasks:

```bash
npx tsx packages/core/src/cliEntry.ts run "implement user authentication with JWT"
```

The `run` command activates the full pipeline:
1. **Deliberation** — analyze task complexity and dependencies
2. **Effort scaling** — determine how many agents to allocate
3. **Topology routing** — select the optimal execution pattern
4. **Atomization** — decompose into subtasks
5. **Execution** — multi-agent orchestration with tool calls
6. **Verification** — 5 quality gates (hallucination, consistency, completeness, accuracy, safety)

## 플랜 모드


Preview the execution plan before any changes are made:

```bash
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module"
```

Plan mode shows:
- Task complexity score and level
- Selected topology
- Number of agents and their roles
- Provider selection and fallback chain
- Estimated token budget

## Watch Mode (SSE)


Execute with real-time streaming events:

```bash
npx tsx packages/core/src/cliEntry.ts watch "debug the failing test"
```

Watch mode streams every event via SSE:
- Agent deliberation steps
- Tool calls and results  
- Verification checkpoints
- Token usage in real-time

## Batch Processing


```bash
# Process multiple tasks from a file
npx tsx packages/core/src/cliEntry.ts run --file tasks.json

# Format:
# [{"task": "analyze module A"}, {"task": "test module B"}]
```

## Approval Modes


| Mode | Behavior | Use Case |
|------|----------|----------|
| `plan` | Show plan only | Review before execution |
| `read-only` | Read files only | Code review, analysis |
| `auto-edit` | Auto-approve edits | Development workflow |
| `full-auto` | Fully autonomous | CI/CD, batch processing |
| `suggest` | Suggest, wait for approval | Learning, tutorials |

Set the mode via:
```bash
export COMMANDER_MODE=auto-edit
# Or at runtime:
npx tsx packages/core/src/cliEntry.ts mode auto-edit
```
