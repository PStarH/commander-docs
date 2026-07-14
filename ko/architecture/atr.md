# Agent Transaction Runtime (ATR)

ATR은 에이전트 결정 루프와 **모든 외부 시스템 호출 사이**에 있는 정산(settlement) 계층입니다. 액션을 멱등·복구 가능·리스 기반·펜싱 보호로 보장합니다.

## 왜 ATR인가

ATR 없이 에이전트 실행은 fire-and-forget입니다. 도구는 성공했는데 결과 기록 전에 크래시하면 액션이 사라지고, 재시도하면 이중 실행됩니다. ATR은 트랜잭션 보장으로 이를 막습니다.

```
Agent Decision → ATR Settlement Layer → External System
                     ├── Idempotency (중복 없음)
                     ├── Recovery (보상 롤백)
                     ├── Leasing (단일 소유 런)
                     └── Fencing (좀비 프로세스 차단)
```

## 런 수명주기

```
PENDING → EXECUTING → VERIFYING → COMMITTED
               │            │
               │            └──→ ABORTED → COMPENSATED
               └───────────────────→ ABORTED → COMPENSATED
```

- **PENDING** — 생성됨, 미시작  
- **EXECUTING** — 작업 중  
- **VERIFYING** — 품질 게이트  
- **COMMITTED** — 성공 종료  
- **ABORTED** — 실패/취소  
- **COMPENSATED** — 부작용 롤백 완료  
- **PAUSED** — HITL/예산 정지 (재개 가능)  

## 멱등성

외부 액션마다 SHA-256 멱등 키. 동일 키 재시도는 캐시 결과를 반환합니다.

```typescript
import { IdempotencyStore } from '@commander/core';

const store = new IdempotencyStore({ ttlSeconds: 3600 });

const result = await store.execute('github:create-pr:abc123', async () => {
  return await github.createPR({ title: 'Fix bug', body: '...' });
});
```

## 리스 & 펜싱

단일 워커/프로세스가 런을 소유합니다. 만료 lease와 fencing 토큰이 좀비 실행을 막습니다. 복구는 [이벤트 소싱](/ko/architecture/event-sourcing) 의 RecoveryBootstrapper 와 연동됩니다.

## 관련

- [이벤트 소싱](/ko/architecture/event-sourcing)  
- [Saga](/ko/architecture/saga)  
- [Resilience](/ko/architecture/resilience)  
- [V2 마이그레이션](/ko/guide/migration-v2)  
