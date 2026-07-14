# Cookbook: Refactor a module safely

Commander의 **Cookbook: Refactor a module safely** 사용법과 운영 포인트를 정리합니다.

## 빠른 시작

```bash
cd /path/to/your-project   # or the Commander monorepo for a dry run
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=plan
```


## 포인트

- monorepo CLI: `cliEntry.ts` / 빌드 후 `commander`  
- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 정확한 동작은 monorepo 소스를 기준으로 합니다  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
