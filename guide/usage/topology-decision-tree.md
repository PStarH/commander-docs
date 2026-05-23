# Topology Decision Tree

Not sure which orchestration topology to use? Follow this decision tree.

## Quick Reference

```
Is the task simple and well-defined?
├── YES → Do agents need to iterate?
│   ├── NO  ──→ SINGLE
│   └── YES ──→ EVALUATOR-OPTIMIZER
└── NO  → Are subtasks independent?
    ├── YES → Are agents debating?
    │   ├── NO  ──→ PARALLEL
    │   └── YES ──→ DEBATE
    └── NO  → Do subtasks depend on each other?
        ├── NO  → Is there a clear lead agent?
        │   ├── YES ──→ HIERARCHICAL
        │   └── NO  ──→ HYBRID
        └── YES → Are steps sequential?
            ├── YES ──→ SEQUENTIAL
            └── NO  ──→ HYBRID
```

## Topology Details

### SINGLE
**When**: Simple, well-scoped tasks
**Example**: "Explain this function", "Format this file"
**Agents**: 1

### SEQUENTIAL
**When**: Multi-step transformations where each step depends on the previous
**Example**: "Read the file → analyze the code → generate a report"
**Agents**: 2–3

### PARALLEL
**When**: Independent subtasks that can run simultaneously
**Example**: "Search for bugs in all modules at once"
**Agents**: 2–10

### HIERARCHICAL
**When**: Complex task with a clear decomposition path
**Example**: A lead architect decomposes the work and delegates to specialists
**Agents**: 3–8

### HYBRID
**When**: Mixed dependencies — some parallel, some sequential
**Example**: "Refactor the API layer" — parallel analysis, sequential implementation
**Agents**: 3–10

### DEBATE
**When**: High-risk decisions requiring cross-validation
**Example**: "Is this security vulnerability real or a false positive?"
**Agents**: 2–5

### ENSEMBLE
**When**: Critical decisions needing consensus across models
**Example**: "Which architecture best meets our requirements?"
**Agents**: 3–7

### EVALUATOR-OPTIMIZER
**When**: Iterative improvement needed
**Example**: "Improve the performance of this query" (generate → benchmark → refine)
**Agents**: 2

## Complexity-Based Selection

Commander automatically selects the topology based on task complexity:

| Score | Auto-Selected Topology |
|:-----:|:----------------------:|
| 0–20 | SINGLE |
| 20–40 | SEQUENTIAL or PARALLEL |
| 40–60 | HIERARCHICAL |
| 60–80 | HYBRID or DEBATE |
| 80–100 | ENSEMBLE or EVALUATOR-OPT |

Override the automatic selection:
```bash
npx tsx cli.ts run "task" --topology debate
```
