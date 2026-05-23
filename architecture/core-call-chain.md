# Core Call Chain

Every Commander execution follows a structured pipeline:

## 1. Deliberation

```bash
CLI / HTTP / API
  │
  ├─ deliberation.ts     ← "What kind of task is this?"
  │   └─ TaskComplexityAnalyzer
```

The deliberation engine analyzes the task's complexity, dependency graph, and domain requirements to determine the optimal execution strategy.

## 2. Effort Scaling

```bash
  ├─ effortScaler.ts     ← "How many agents?"
```

Based on complexity, Commander scales across 1–20 agents. Simple tasks get a single agent; complex research tasks get a team.

## 3. Topology Routing

```bash
  ├─ topologyRouter.ts   ← "Which topology fits?"
```

Selects the optimal execution topology from 8 options:

- **SINGLE** — Simple tasks, one agent
- **SEQUENTIAL** — Dependent steps, chain-of-thought
- **PARALLEL** — Independent subtasks, max throughput
- **HIERARCHICAL** — Lead agent delegates to specialists
- **HYBRID** — Mixed topology for complex workflows
- **DEBATE** — Multiple agents cross-validate answers
- **ENSEMBLE** — Vote-based consensus from diverse models
- **EVALUATOR-OPT** — Generate → critique → refine loop

## 4. Atomization

```bash
  ├─ atomizer.ts         ← "Break into subtasks"
```

ROMA-style decomposition splits the task into atomic, dependency-aware subtasks.

## 5. Execution

```bash
  ├─ agentRuntime.ts.execute(ctx)
      │
      ├─ acquireSlot()              ← Concurrency semaphore
      ├─ [Tenant check]             ← Rate limit + concurrency quota
      ├─ resolve tenant storage     ← Per-tenant isolation
      │
      ├─ [Retry loop: 0..maxRetries]
      │   ├─ callWithTimeout()      ← LLM provider call
      │   ├─ [Tool execution loop]
      │   │   ├─ toolCache.get()    ← SHA-256 hash lookup
      │   │   ├─ planner.plan()     ← Dependency-aware plan
      │   │   ├─ executeTool()      ← StepErrorBoundary
      │   │   └─ toolCache.set()    ← Cache result
      │   ├─ verification.check()   ← 5 quality gates
      │   └─ checkpoint()           ← Atomic state save
      │
      └─ → AgentExecutionResult
```

## 6. Quality Gates

After execution, results pass through 5 verification gates:

- Hallucination detection
- Consistency check
- Completeness verification
- Accuracy validation
- Safety check

## 7. Completion

Results are flushed to trace store, metrics are recorded, and the execution summary is returned.
