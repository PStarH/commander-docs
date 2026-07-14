# 검증 파이프라인

Every agent output passes through a 5-gate quality verification pipeline before it is returned to the caller. This is not a "nice-to-have" check — it is an integral part of the runtime retry loop. The `UnifiedVerificationPipeline` orchestrates all 5 gates:

이 문서는 Commander에서 **검증 파이프라인** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
Agent output
  │
  ├─ Gate 1: Hallucination Detection
  │   └─ Signal-based detector with configurable thresholds
  │
  ├─ Gate 2: Consistency Check
  │   └─ Internal consistency and contradiction detection
  │
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
