# 복원력

Commander includes a multi-layer resilience infrastructure that ensures availability, data safety, and recoverability in production. Each LLM provider has its own circuit breaker with three states:

이 문서는 Commander에서 **복원력** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
const breaker = new CircuitBreaker({ threshold: 5, cooldownMs: 30000 });
breaker.onSuccess();    // Resets failure count
breaker.onFailure();    // Increments; opens circuit at threshold
breaker.isAvailable();  // false when OPEN
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
