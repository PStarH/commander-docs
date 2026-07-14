# Backpressure Controller

The backpressure controller implements **unified admission control** for the Commander runtime, preventing overload when demand exceeds capacity. It uses a three-stage pipeline: Token Bucket → Ring Buffer → Circuit Breaker. 1. **Token Bucket** — Requests consume a token. When the bucket is empty, requests spill to the ring buffer.

이 문서는 Commander에서 **Backpressure Controller** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
Producer → [Token Bucket] → [Ring Buffer] → [Circuit Breaker] → Consumer
              rate-limit       absorb bursts     protect when overwhelmed
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
