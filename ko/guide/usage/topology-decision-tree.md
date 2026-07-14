# 토폴로지 결정 트리

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/guide/usage/topology-decision-tree)



Not sure which orchestration topology to use? Follow this decision tree.

## Quick Reference


```
Is the task simple and well-defined?
├── YES → SINGLE
└── NO  → Are subtasks independent?
    ├── YES → DISPATCH
    └── NO  → Do subtasks depend on each other?
        ├── YES → CHAIN
        └── NO  → Is there a clear lead agent?
            ├── YES → ORCHESTRATOR
            └── NO  → REVIEW
```

## Topology Details


### SINGLE

**When**: Simple, well-scoped tasks
**Example**: "Explain this function", "Format this file"
**Agents**: 1

### CHAIN

**When**: Multi-step transformations where each step depends on the previous
**Example**: "Read the file → analyze the code → generate a report"
**Agents**: 2–3

### DISPATCH

**When**: Independent subtasks that can run simultaneously
**Example**: "Search for bugs in all modules at once"
**Agents**: 2–10

### ORCHESTRATOR

**When**: Complex task with a clear decomposition path
**Example**: A lead architect decomposes the work and delegates to specialists
**Agents**: 3–8

### REVIEW

**When**: High-risk decisions requiring cross-validation, iterative refinement, or consensus
**Example**: "Is this security vulnerability real or a false positive?"
**Agents**: 2–5

## Complexity-Based Selection


Commander automatically selects the topology based on task complexity:

| Score | Auto-Selected Topology |
|:-----:|:----------------------:|
| 0–20 | SINGLE |
| 20–40 | CHAIN |
| 40–60 | DISPATCH |
| 60–80 | ORCHESTRATOR |
| 80–100 | REVIEW |

Override the automatic selection:
```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
```
