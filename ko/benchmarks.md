# Benchmarks

Commander 아키텍처 구성 요소에 대한 한국어 문서입니다. monorepo 구현과 정렬됩니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 참고 표

| Benchmark | Scale | Commander | Competitor | Evidence |
|-----------|:-----:|:---------:|:----------:|----------|
| **HumanEval+** | 164 problems | **91.5%** | o4 97.1% | `docs/benchmark-results/humaneval-results.json` |
| **GAIA (Commander)** | 165 tasks | **69.7%** | Bare MiMo 21.2% | `docs/benchmark-results/gaia-commander-final/` |
| **BFCL (35 scenarios)** | 35 scenarios | Tool **60.0%** / Param **91.4%** | — | `benchmarks/bfcl/results_full.json` + 35 response files |
| **BFCL (12 core)** | 12 scenarios | Tool **91.7%** / Param **91.7%** | Llama 405B 88.5% | `benchmarks/bfcl/results.json` + 12 response files |
| **MT-Bench** | 5 questions (subset) | **7.8/10** | — | `docs/benchmark-results/mtbench/` |
| **PinchBench** | 43 tasks | **97.7%** (42/43) | OpenClaw 89.5% | `docs/benchmark-results/pinchbench-final42/` |


## 주요 내용

### Results Summary

운영 시 **Results Summary** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/benchmarks)를 보세요.

### Key Insight

운영 시 **Key Insight** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/benchmarks)를 보세요.

### Benchmark Details

운영 시 **Benchmark Details** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/benchmarks)를 보세요.

### Running Benchmarks Yourself

운영 시 **Running Benchmarks Yourself** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/benchmarks)를 보세요.

## 예제 (코드는 영어 유지)

```bash
cd packages/core

# Run all benchmarks
npx tsx --test tests/benchmark.test.ts

# Run specific benchmarks
npx tsx benchmark.ts --benchmark gaia
npx tsx benchmark.ts --benchmark bfcl
npx tsx benchmark.ts --benchmark pinchbench
```

## 운영

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 관련

- [아키텍처 개요](/ko/architecture/overview)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [보안](/ko/guide/security)
- [빠른 시작](/ko/guide/getting-started)
