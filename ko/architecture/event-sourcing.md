# 이벤트 소싱 및 복구

Commander's event sourcing system provides crash-safe execution with tamper-proof audit trails, deterministic replay, and automatic zombie run recovery. The `EventSourcingEngine` implements the IEventSourcingEngine contract (Pillar I) with a Write-Ahead Log (WAL) and SHA-256 hash chain for tamper protection.

이 문서는 Commander에서 **이벤트 소싱 및 복구** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
[event 1] → SHA256("") → hash_1
[event 2] → SHA256(hash_1 | type | id | timestamp | payload) → hash_2
[event 3] → SHA256(hash_2 | type | id | timestamp | payload) → hash_3
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
