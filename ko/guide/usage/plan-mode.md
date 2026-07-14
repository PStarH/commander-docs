# 플랜 모드

Plan mode lets you see what Commander will do **before** it does it. Switch to plan mode to review the execution strategy, agent allocation, and tool calls — with zero risk of unintended changes. - **Safety** — Review the full plan before any files are modified

이 문서는 Commander에서 **플랜 모드** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
# Set plan mode
npx tsx packages/core/src/cliEntry.ts mode plan

# Then run any task
npx tsx packages/core/src/cliEntry.ts run "refactor the database layer"

# Or use the --plan flag for one-off plan mode
npx tsx packages/core/src/cliEntry.ts plan "implement search feature"
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
