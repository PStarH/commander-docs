# Speculative Execution

Commander implements **PASTE-style speculative execution** (Pattern-Aware Speculative Execution) that pre-executes likely tool calls during LLM thinking time. Research shows this achieves up to 48.5% reduction in task completion time.

## How It Works

During LLM thinking/processing time, Commander predicts the most likely next tool calls based on observed patterns and pre-executes them. If the model actually makes those calls, results are already available (zero-wait). Wrong predictions are discarded at no cost.

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  LLM Call   │────▶│ Pattern Tracker  │────▶│ Speculative     │
│  (thinking) │     │ (predict next)   │     │ Executor        │
└─────────────┘     └──────────────────┘     └────────┬────────┘
                                                       │
                         ┌─────────────────────────────┘
                         ▼
               ┌──────────────────┐
               │  Pre-executed    │
               │  Tool Results    │
               │  (cached)        │
               └──────────────────┘
```

## Safety

Only **read-only** tools are speculatively executed:
- `file.read`, `web.search`, `web.fetch`, `code.search`, `git.status`

**State-mutating** tools are NEVER speculatively executed:
- `file.write`, `file.edit`, `shell.execute`, `git.commit`, `apply_patch`

This ensures speculative execution is always safe — wrong predictions have zero side effects.

## Pattern Tracking

The `PatternTracker` records tool call sequences and identifies recurring patterns:

```typescript
import { PatternTracker } from '@commander/core';

const tracker = new PatternTracker();

// Record observed tool sequences
tracker.recordSequence(['file.read', 'code.search', 'file.read']);

// Predict next tool given partial sequence
const predictions = tracker.predictNext(['file.read']);
// → [{ toolName: 'code.search', confidence: 0.8 }]
```

### Pattern Lifecycle

1. **Observation** — Tool call sequences are recorded as n-grams (2, 3, 4-grams)
2. **Confidence building** — Each recurrence increases confidence: `min(1, frequency / 10)`
3. **Pruning** — Low-confidence patterns (<2 occurrences) or stale patterns (>5 min unused) are pruned
4. **Prediction** — Given a partial sequence, the tracker finds the most likely next tool

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `maxPatternLength` | `4` | Max n-gram length |
| `maxTrackedPatterns` | `50` | Max patterns in memory |
| `minConfidence` | `0.1` | Minimum confidence to predict |
| `staleThresholdMs` | `300000` | Prune patterns older than 5 min |

## Programmatic API

```typescript
import { SpeculativeExecutor, PatternTracker } from '@commander/core';

const tracker = new PatternTracker();
const executor = new SpeculativeExecutor({ tracker });

// During LLM thinking time
const predictions = tracker.predictNext(currentToolSequence);

// Pre-execute predicted tools (read-only only)
const preExecuted = await executor.speculate(predictions);

// When the model actually calls a tool, check if we already have the result
const cached = executor.getCachedResult('file.read', { path: 'src/index.ts' });
if (cached) {
  // Use cached result — zero wait
  return cached;
} else {
  // Execute normally
  return await executeTool('file.read', { path: 'src/index.ts' });
}
```

## When Speculative Execution Helps Most

| Scenario | Speedup | Why |
|----------|---------|-----|
| Multi-file analysis | High | `file.read` → `code.search` → `file.read` patterns are predictable |
| Code review | Medium | `git.diff` → `file.read` → `code.search` sequences recur |
| Debugging | Low-Medium | Tool sequences are less predictable |
| Simple queries | None | Single tool call, no patterns to exploit |

## Monitoring

Speculative execution metrics are available via the metrics collector:

```
speculative_predictions_total        — Total predictions made
speculative_correct_total            — Predictions that matched actual calls
speculative_accuracy_ratio           — correct / predictions
speculative_preexecuted_tools_total  — Tools pre-executed speculatively
speculative_time_saved_ms            — Total wait time eliminated
```
