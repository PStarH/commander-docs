# 레질리언스 (Resilience)

Commander는 가용성·데이터 안전·복구 가능성을 위한 **다층 레질리언스**를 둡니다.

## Circuit Breaker

프로바이더마다 3상태 브레이커:

| 상태 | 동작 |
|------|------|
| **CLOSED** | 정상 통과 |
| **OPEN** | 연속 5회 실패 후. 즉시 거절. 쿨다운 30s |
| **HALF-OPEN** | 쿨다운 후 시험 1회. 성공→CLOSED, 실패→OPEN |

```typescript
const breaker = new CircuitBreaker({ threshold: 5, cooldownMs: 30000 });
breaker.onSuccess();
breaker.onFailure();
breaker.isAvailable();
```

`CircuitBreakerRegistry`가 활성 프로바이더 브레이커를 통합 관리합니다.

## Provider Fallback Chain

```typescript
const chain = new ProviderFallbackChain({
  providers: ['openai', 'anthropic', 'deepseek', 'groq'],
  timeoutMs: 30000,
});

const result = await chain.tryProviders(task);
// 전부 실패 시 FallbackChainExhaustedError
```

`llmRetry.ts`가 오류를 재시도 가능(rate limit, timeout) vs 영구(auth, invalid)로 분류합니다.

## Crash-safe Checkpoints

`StateCheckpointer`가 매 단계 SQLite WAL로 상태를 저장합니다.

- `synchronous=NORMAL`, `busy_timeout=5000`  
- 트랜잭션 atomic write  
- 테넌트별 디렉터리  

```typescript
const checkpointer = new StateCheckpointer({ basePath: '/data/checkpoints' });
await checkpointer.checkpoint({ runId, phase, stepNumber, messages, tokenUsage });
```

## Dead Letter Queue

복구 불가 오류를 **7 카테고리 · 15 실패 모드**로 영속화:

| 카테고리 | 설명 |
|----------|------|
| `llm` | LLM 호출 실패 |
| `tool` | 도구 실행 실패 |
| `execution` | 에이전트 실행 실패 |
| `verification` | 품질 게이트 실패 |
| `circuit_breaker` | 브레이커 트립 |
| `compensation` | 보상 실패 |
| `semantic_drift` | 의미 저하 |

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts doctor --reset   # 브레이커 리셋 등
```

## 관련

- [이벤트 소싱](/ko/architecture/event-sourcing)  
- [프로덕션 준비](/ko/architecture/production-readiness)  
- [Saga](/ko/architecture/saga)  
