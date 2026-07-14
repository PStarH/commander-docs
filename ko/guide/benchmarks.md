# 벤치마크

Commander is benchmarked across **security, reliability, performance, chaos, and capability**. Numbers below are from the product README / monorepo scripts — re-run them yourself for current baselines. **Source of truth:** monorepo [`BENCHMARK.md`](https://github.com/PStarH/Commander/blob/master/BENCHMARK.md).

이 문서는 Commander에서 **벤치마크** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
pnpm benchmark:all          # multi-suite readiness
pnpm benchmark:redteam      # 47 scenarios
pnpm benchmark:agentdojo    # injection suite
pnpm benchmark:chaos        # chaos (simulated default)
pnpm bench:slo              # SLO baseline
pnpm check:readiness        # baseline freshness
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
