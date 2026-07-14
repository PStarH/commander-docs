# Agent Transaction Runtime (ATR)

ATR is the **settlement layer** that sits between the agent's decision loop and every external system call. It guarantees that agent actions are idempotent, recoverable, leased, and fenced. Without ATR, agent execution is fire-and-forget: if a tool call succeeds but the agent crashes before recording the result, the action is lost. If the agent retries, the action executes twice. ATR solves this w

이 문서는 Commander에서 **Agent Transaction Runtime (ATR)** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
Agent Decision → ATR Settlement Layer → External System
                    ├── Idempotency (no duplicates)
                    ├── Recovery (compensable rollback)
                    ├── Leasing (single-owner runs)
                    └── Fencing (zombie process protection)
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
