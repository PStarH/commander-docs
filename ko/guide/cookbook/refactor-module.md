# Cookbook: Refactor a module safely

**Goal:** Use plan mode to preview a refactor, then execute with controlled approval. **Time:** ~15 minutes · **Risk:** writes files — start in `plan` / `suggest`

이 문서는 Commander에서 **Cookbook: Refactor a module safely** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
cd /path/to/your-project   # or the Commander monorepo for a dry run
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=plan
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
