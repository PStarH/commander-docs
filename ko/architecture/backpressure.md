# 백프레셔 컨트롤러

백프레셔 컨트롤러는 Commander 런타임의 **통합 입장 제어(admission control)** 입니다. 수요가 용량을 넘을 때 과부하를 막으며, **Token Bucket → Ring Buffer → Circuit Breaker** 3단계 파이프라인을 씁니다.

## 구조

```
Producer → [Token Bucket] → [Ring Buffer] → [Circuit Breaker] → Consumer
               rate-limit       absorb bursts     protect when overwhelmed
```

| 단계                | 역할                          | 패턴            |
| ------------------- | ----------------------------- | --------------- |
| **Token Bucket**    | 초당 토큰으로 입장 속도 제한  | Leaky bucket    |
| **Ring Buffer**     | 버스트 흡수 (고정 크기, O(1)) | LMAX Disruptor  |
| **Circuit Breaker** | 소비자 과부하 시 보호         | Hystrix 3-state |

## 동작

1. **Token Bucket** — 요청이 토큰을 소비. 버킷이 비면 ring buffer로 spill.
2. **Ring Buffer** — 고정 크기로 버스트 흡수. 가득 차면 가장 오래된 항목 제거(spill 집계).
3. **Circuit Breaker** — spill 비율이 임계값을 넘으면 open, half-open까지 요청 drop.

## 설정

```typescript
import { BackpressureController } from "@commander/core";

const controller = new BackpressureController({
  tokenBucket: {
    maxTokens: 100,
    refillRatePerSecond: 50,
  },
  ringBuffer: {
    capacity: 200,
  },
  circuitBreaker: {
    failureThreshold: 0.5,
    recoveryTimeoutMs: 30000,
    halfOpenMaxRequests: 10,
  },
});
```

> 패키지는 monorepo `packages/core`에서 가져옵니다. npm 공개가 주 경로가 되기 전까지 workspace를 쓰세요.

## 사용

```typescript
const admission = controller.tryAdmit();

if (admission.allowed) {
  const result = await processRequest(request);
  controller.recordSuccess();
} else {
  return { status: 429, reason: admission.reason };
}
```

## Lock-free

CAS(Compare-And-Swap) 기반 원자 카운터로 동시 읽기가 쓰기를 막지 않습니다 (NFR-PERF-05).

## 메트릭

| 메트릭                                 | 설명                            |
| -------------------------------------- | ------------------------------- |
| `backpressure_tokens_available`        | 버킷 잔여 토큰                  |
| `backpressure_ring_buffer_occupancy`   | 링 버퍼 점유율                  |
| `backpressure_circuit_breaker_state`   | `CLOSED` / `OPEN` / `HALF_OPEN` |
| `backpressure_requests_admitted_total` | 허용 요청                       |
| `backpressure_requests_rejected_total` | 거절 요청                       |
| `backpressure_requests_spilled_total`  | spill 수                        |

## 튜닝

| 증상            | 조정                                     |
| --------------- | ---------------------------------------- |
| 429가 너무 많음 | `maxTokens` / `refillRatePerSecond` 증가 |
| 메모리 압박     | ring `capacity` 감소                     |
| 연쇄 장애       | `failureThreshold` 낮춰 조기 open        |
| 회복이 느림     | `recoveryTimeoutMs` 증가                 |

## 관련

- [프로덕션 준비](/ko/architecture/production-readiness)
- [에이전트 런타임](/ko/architecture/agent-runtime)
- [문제 해결](/ko/guide/troubleshooting)
