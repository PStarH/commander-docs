# 보안 샌드박스

**보안 샌드박스.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

이 문서는 Commander에서 **보안 샌드박스** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
sandbox/
├── execPolicy.ts           ← Execution policy definitions
├── approval.ts             ← Approval workflow for sensitive operations
├── profiles.ts             ← Security profiles (READ_ONLY, WORKSPACE_WRITE, FULL_ACCESS, HARDENED)
├── platforms.ts            ← Platform-specific sandbox configurations
├── manager.ts              ← Sandbox lifecycle management
├── executionRouter.ts      ← Route executions to appropriate backends
├── lane.ts                 ← Execution lane management
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
