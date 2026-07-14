# Enterprise Security Gateway

Commander's `EnterpriseSecurityGateway` provides a 7-layer defense-in-depth architecture that is invoked during all LLM calls and tool executions. It cannot be bypassed — cost checks execute both before and after LLM calls. - **Defense in depth** — Multiple independent layers, each with distinct responsibility

이 문서는 Commander에서 **Enterprise Security Gateway** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
entry_1 → SHA256(prev_hash | entry_1) → hash_1
entry_2 → SHA256(hash_1 | entry_2) → hash_2
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
