# 벤치마크

Commander adds **+48.5 percentage points** over the bare MiMo base model on GAIA — demonstrating the power of multi-agent orchestration over single-agent baselines. - **Score**: 69.7% (115/165 correct)

이 문서는 Commander에서 **벤치마크** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
cd packages/core

# Run all benchmarks
npx tsx --test tests/benchmark.test.ts

# Run specific benchmarks
npx tsx benchmark.ts --benchmark gaia
npx tsx benchmark.ts --benchmark bfcl
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
