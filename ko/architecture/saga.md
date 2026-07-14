# Saga 트랜잭션

Commander는 다단계 작업의 일관성을 위해 **사가 패턴**(단계별 보상 롤백)을 구현합니다.

## 구조

```
SagaBuilder.define()
  │
  ├─ Step 1: Create resource   → Compensation: Delete
  ├─ Step 2: Update resource   → Compensation: Revert
  ├─ Step 3: Send notification → Compensation: Void
  │
  └─ Coordinator.execute(saga)
       ├─ 성공 시 순차 진행
       └─ 실패 시 역순 보상
```

## SagaBuilder

정방향 액션과 보상 롤백을 함께 정의합니다.

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

- 순서대로 스텝 실행  
- 실패 시 **역순** 보상  
- 상태: PENDING · COMPLETED · COMPENSATING · FAILED  
- 복구 불가 시 DLQ 연동  

## WorkerPool

독립 스텝은 워커 풀로 병렬화할 수 있습니다.

```typescript
const pool = new WorkerPool({ maxConcurrency: 5 });
pool.execute(steps);
```

## 도구 연동

mutation 도구는 Compensation Registry에 보상을 등록해 런타임 실패 시 자동 롤백합니다. CLI: `saga` / `compensation` / `undo` (빌드 후 `commander`, 소스에서는 `cliEntry.ts`).

```bash
npx tsx packages/core/src/cliEntry.ts doctor
```

## 관련

- [프로덕션 준비](/ko/architecture/production-readiness)  
- [Resilience](/ko/architecture/resilience)  
- [도구](/ko/architecture/tools)  
