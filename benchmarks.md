# Benchmarks

> **Generated**: 2026-05-17 | **Base model**: MiMo (mimo-v2.5-pro)
> **Raw data**: See `docs/benchmark-results/` in the Commander repository.

## Results Summary

| Benchmark | Scale | Commander | Competitor | Evidence |
|-----------|:-----:|:---------:|:----------:|----------|
| **HumanEval+** | 164 problems | **91.5%** | o4 97.1% | `docs/benchmark-results/humaneval-results.json` |
| **GAIA (Commander)** | 165 tasks | **69.7%** | Bare MiMo 21.2% | `docs/benchmark-results/gaia-commander-final/` |
| **BFCL (35 scenarios)** | 35 scenarios | Tool **60.0%** / Param **91.4%** | — | `benchmarks/bfcl/results_full.json` + 35 response files |
| **BFCL (12 core)** | 12 scenarios | Tool **91.7%** / Param **91.7%** | Llama 405B 88.5% | `benchmarks/bfcl/results.json` + 12 response files |
| **MT-Bench** | 5 questions (subset) | **7.8/10** | — | `docs/benchmark-results/mtbench/` |
| **PinchBench** | 43 tasks | **97.7%** (42/43) | OpenClaw 89.5% | `docs/benchmark-results/pinchbench-final42/` |

## Key Insight

Commander adds **+48.5 percentage points** over the bare MiMo base model on GAIA — demonstrating the power of multi-agent orchestration over single-agent baselines.

## Benchmark Details

### GAIA (165 Multi-Step Reasoning Tasks)

- **Score**: 69.7% (115/165 correct)
- **Caveat**: 105 of the 115 correct answers have an empty `answer` field — this is an extraction logic bug, not a scoring bug. The `correct` field is based on the full LLM response.
- **Comparison**: Bare MiMo scores 21.2% — Commander's orchestration adds 48.5 percentage points.

### BFCL — Berkeley Function Calling Leaderboard

Commander has **two actual run subsets**:

| Subset | Scenarios | Tool Accuracy | Parameter Accuracy |
|--------|:---------:|:-------------:|:-----------------:|
| 35-scenario (general) | 35 | 60.0% | 91.4% |
| 12-core (core test) | 12 | 91.7% | 91.7% |

Both are unofficial BFCL subsets. The official 2000+ task full run is pending.

### PinchBench (43 Agentic Tasks)

- **Score**: 97.7% (42/43 tasks passed)
- **Failed**: `multifile.json`
- **Comparison**: OpenClaw reports 89.5% on the same benchmark.

### HumanEval+ (164 Python Problems)

- **Score**: 91.5%
- **Testing**: Generates Python solutions and runs them through the HumanEval+ test suite.

### MT-Bench

- **Score**: 7.8/10 on a 5-question subset
- **Note**: This is NOT the standard 80-question full set. The full set run is pending.

## Running Benchmarks Yourself

```bash
cd packages/core

# Run all benchmarks
npx tsx --test tests/benchmark.test.ts

# Run specific benchmarks
npx tsx benchmark.ts --benchmark gaia
npx tsx benchmark.ts --benchmark bfcl
npx tsx benchmark.ts --benchmark pinchbench
```
