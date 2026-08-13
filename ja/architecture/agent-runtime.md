# エージェントランタイム

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/architecture/agent-runtime)



The execution engine at the heart of Commander. The `AgentRuntime` manages the full lifecycle of a single agent: LLM calls, tool execution, verification, checkpointing, and retry — all within configurable token and step budgets.

## Architecture


```
AgentRuntime.execute(ctx)
  │
  ├─ acquireSlot()        ← Concurrency semaphore
  ├─ [Tenant check]       ← Rate limit + concurrency quota
  ├─ resolve storage      ← Tenant-scoped memory + caching
  │
  ├─ [Retry loop: 0..maxRetries]
  │   ├─ callWithTimeout()       ← LLM provider call
  │   ├─ [Tool execution loop]
  │   │   ├─ planner.plan()      ← Dependency-aware execution plan
  │   │   ├─ executeTool()       ← StepErrorBoundary → tool.execute()
  │   │   └─ cache.set()         ← Cache result
  │   ├─ verification.check()    ← 5 quality gates
  │   └─ checkpoint()            ← Atomic save
  │
  ├─ releaseSlot()
  └─ flush traces + samples
```

## Main Loop


Each agent run follows this sequence:

1. **Slot acquisition** — A concurrency semaphore prevents exceeding max concurrent runs
2. **Tenant validation** — Rate limits and concurrency quotas are checked per tenant
3. **LLM call** — The provider is called with a configurable timeout
4. **Tool execution** — The LLM's tool requests are executed. The `ToolPlanner` builds a dependency-aware execution plan so parallelizable tools run concurrently
5. **Verification** — The output passes through a 5-gate verification pipeline. If it fails, the runtime retries
6. **Checkpointing** — State is persisted atomically at every step for crash recovery
7. **Tracing** — Execution traces and LLM samples are flushed to persistent stores

## Key Components


| Component | File | Purpose |
|-----------|------|---------|
| `AgentRuntime` | `runtime/agentRuntime.ts` | Main execution loop |
| `ToolPlanner` | `runtime/toolPlanner.ts` | Dependency-aware tool execution plan |
| `ToolOrchestrator` | `runtime/toolOrchestrator.ts` | Executes planned tool calls |
| `StepErrorBoundary` | `runtime/stepErrorBoundary.ts` | Per-step recovery: skip, retry, or abort |
| `StepTimeoutManager` | `runtime/stepTimeoutManager.ts` | Per-step timeout enforcement |
| `ContextCompactor` | `runtime/contextCompactor.ts` | Token-aware message compaction |
| `ContextWindow` | `runtime/contextWindow.ts` | Sliding window context management |
| `TokenGovernor` | `runtime/tokenGovernor.ts` | Token budget enforcement |
| `CycleDetector` | `runtime/cycleDetector.ts` | Loop detection to prevent infinite execution |
| `ToolOutputManager` | `runtime/toolOutputManager.ts` | Token-budgeted tool output management |

## 設定


```typescript
interface AgentRuntimeConfig {
  maxStepsPerRun: number;      // Max LLM→tool cycles per run
  maxRetries: number;          // Max verification retries
  timeoutMs: number;           // Per-LLM-call timeout
  maxConcurrency: number;      // Max concurrent agent runs
  budgetHardCapTokens: number; // Absolute token ceiling
}
```

## Execution Plan


Tools are not executed in LLM response order. The `ToolPlanner` analyzes dependencies between tool calls and produces a parallel-aware execution plan:

- Independent tools execute concurrently
- Dependent tools execute sequentially after their prerequisites
- The plan is validated before any tool runs, catching circular dependencies early
