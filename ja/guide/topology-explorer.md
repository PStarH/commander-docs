# 対話型トポロジエクスプローラー

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/guide/topology-explorer)



Pick a task shape. Commander’s deliberation engine maps similar signals onto one of **five canonical topologies**. This page is a decision aid — not a substitute for `plan`.

## Decision tree


```
Is the task a single clear question with one owner?
  YES → SINGLE
  NO  ↓
Does work form a strict pipeline (A then B then C)?
  YES → CHAIN
  NO  ↓
Can specialists work in parallel then merge?
  YES → DISPATCH
  NO  ↓
Does a lead need to delegate and re-plan?
  YES → ORCHESTRATOR
  NO  ↓
Is quality / risk high enough to require critique?
  YES → REVIEW
  else → start with DISPATCH or ask `commander plan`
```

## Topology cards


### SINGLE


| | |
|--|--|
| **Agents** | 1 |
| **Best for** | FAQ, simple explain, one-shot transform |
| **Cost** | Lowest |
| **Risk** | No peer review |

```bash
npx tsx packages/core/src/cliEntry.ts plan "what does this function do?"
# often → SINGLE
```

### CHAIN


| | |
|--|--|
| **Agents** | Sequential stages |
| **Best for** | Analyze → implement → verify pipelines |
| **Cost** | Medium |
| **Risk** | Stage failures block the line |

```bash
npx tsx packages/core/src/cliEntry.ts plan "migrate the auth module then update callers"
# often → CHAIN
```

### DISPATCH


| | |
|--|--|
| **Agents** | Parallel specialists + synthesizer |
| **Best for** | Research, audits, multi-angle analysis |
| **Cost** | Higher (parallel) |
| **Risk** | Merge conflicts in synthesis |

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
# often → DISPATCH
```

### ORCHESTRATOR


| | |
|--|--|
| **Agents** | Lead + workers |
| **Best for** | Large, ambiguous, multi-module work |
| **Cost** | High |
| **Risk** | Lead bottleneck / over-delegation |

```bash
npx tsx packages/core/src/cliEntry.ts plan "redesign the billing system end to end"
# often → ORCHESTRATOR
```

### REVIEW


| | |
|--|--|
| **Agents** | Producer + critic / merge |
| **Best for** | High-risk code, security-sensitive output |
| **Cost** | Medium–high |
| **Risk** | Extra latency |

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
```

## Quick chooser


Answer mentally, then confirm with `plan`:

| If your task is… | Try |
|------------------|-----|
| One question, one answer | **SINGLE** |
| Ordered steps that depend on previous output | **CHAIN** |
| Multiple independent investigations | **DISPATCH** |
| Unknown scope; need a manager agent | **ORCHESTRATOR** |
| Correctness > speed | **REVIEW** |

## Force a topology


```bash
npx tsx packages/core/src/cliEntry.ts run "your task" --topology dispatch --stream
npx tsx packages/core/src/cliEntry.ts plan "your task" --topology review
```

Canonical names: `single` · `chain` · `dispatch` · `orchestrator` · `review` (CLI casing may vary — see `commander --help`).

## 関連


- [Topology Decision Tree](/ja/guide/usage/topology-decision-tree) — deeper rules  
- [Running Tasks](/ja/guide/usage/running-tasks)  
- [Why Commander](/ja/guide/why-commander)  
- [Multi-Agent Architecture](/ja/architecture/multi-agent)  
