# 플랜 모드

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/guide/usage/plan-mode)



Plan mode lets you see what Commander will do **before** it does it. Switch to plan mode to review the execution strategy, agent allocation, and tool calls — with zero risk of unintended changes.

## Why Use Plan Mode


- **Safety** — Review the full plan before any files are modified
- **Learning** — Understand how Commander decomposes and approaches tasks
- **Debugging** — See which topology, agents, and tools will be used
- **Collaboration** — Share and iterate on the plan with team members

## 사용법


> From monorepo source; after build use `commander` instead of `npx tsx packages/core/src/cliEntry.ts`.

```bash
# Set plan mode
npx tsx packages/core/src/cliEntry.ts mode plan

# Then run any task
npx tsx packages/core/src/cliEntry.ts run "refactor the database layer"

# Or use the --plan flag for one-off plan mode
npx tsx packages/core/src/cliEntry.ts plan "implement search feature"
```

## Plan Output


When you run a task in plan mode, Commander shows:

```
┃ → Deliberating task...
┃ → Complexity: HIGH (score: 72/100)
┃ → Topology: ORCHESTRATOR
┃ → Agents: 4 (1 lead + 3 specialists)
┃ → Provider: deepseek (fallback: openai → anthropic)
┃ → Token budget: 100,000
┃
┃ → Subtasks:
┃   1. Analyze existing database schema
┃   2. Design migration plan
┃   3. Implement changes (parallel: 2 agents)
┃   4. Verify and test
┃
┃ → Estimated duration: 45s
┃ → Total tools calls: ~12
```

## Visual Indicator


The terminal shows a **plan mode indicator** in the lower-right corner when active, so you always know whether Commander is in plan or execution mode.
