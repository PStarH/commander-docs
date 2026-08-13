# Saga 트랜잭션

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/architecture/saga)



Commander implements the saga pattern for distributed compensating transactions — ensuring data consistency across multi-step operations where each step can be rolled back independently.

## Architecture


```
SagaBuilder.define()
  │
  ├─ Step 1: Create resource   → Compensation: Delete resource
  ├─ Step 2: Update resource   → Compensation: Revert update
  ├─ Step 3: Send notification → Compensation: Void notification
  │
  └─ Coordinator.execute(saga)
       │
       ├─ Step 1 → success
       ├─ Step 2 → success
       ├─ Step 3 → FAILURE
       │
       └─ Compensate
            ├─ Undo Step 2 (revert update)
            └─ Undo Step 1 (delete resource)
```

## SagaBuilder


Define sagas with forward actions and their compensating rollbacks:

```typescript
const saga = new SagaBuilder('deploy-service')
  .step('create-dir', async (ctx) => {
    await fs.mkdir(ctx.path);
  }, {
    compensate: async (ctx) => {
      await fs.rmdir(ctx.path);
    },
  })
  .step('write-config', async (ctx) => {
    await fs.writeFile(ctx.path, ctx.config);
  }, {
    compensate: async (ctx) => {
      await fs.unlink(ctx.path);
    },
  })
  .step('restart-service', async (ctx) => {
    await service.restart();
  }, {
    compensate: async (ctx) => {
      await service.restore(ctx.prevVersion);
    },
  })
  .build();
```

## Coordinator


The `Coordinator` manages saga execution with error handling:

- Executes steps in order
- On step failure, executes compensations in reverse order
- Tracks saga state (PENDING, COMPLETED, COMPENSATING, FAILED)
- Integrates with the dead letter queue for unrecoverable states

## WorkerPool


Steps that can execute concurrently run through a worker pool:

```typescript
const pool = new WorkerPool({ maxConcurrency: 5 });
pool.execute(steps);  // Independent steps run in parallel
```

## Checkpointer


Saga state is checkpointed at every step transition, enabling recovery:

```
Step 1 complete → checkpoint
Step 2 complete → checkpoint
Step 3 fails → load last checkpoint → start compensation
```

## ApprovalManager


For sensitive operations (deployments, financial transactions, permission changes), the approval manager can pause execution for human approval:

```typescript
const approvalManager = new ApprovalManager();
await approvalManager.requestApproval('deploy-to-production', {
  timeoutMs: 3600000,  // 1 hour timeout
  requiredApprovers: ['ops-lead'],
});
// Saga pauses here until approved or rejected
```

## RetryController


Each step can have its own retry policy:

| Policy | Behavior |
|--------|----------|
| No retry | Fail immediately, begin compensation |
| Fixed retries | Retry N times with fixed delay |
| Exponential backoff | Retry with doubling delay, up to max |
| Circuit breaker | Use shared circuit breaker state |

## Stores


The saga subsystem supports pluggable persistence backends:

- **InMemorySagaStore** — Development/testing, no persistence
- **FileSagaStore** — JSON-file based, suitable for single-node deployments
- Custom stores via the `SagaStore` interface
