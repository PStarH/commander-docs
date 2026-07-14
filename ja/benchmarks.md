# Benchmarks

**Benchmarks.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Benchmark | Scale | Commander | Competitor | Evidence |
|-----------|:-----:|:---------:|:----------:|----------|
| **HumanEval+** | 164 problems | **91.5%** | o4 97.1% | `docs/benchmark-results/humaneval-results.json` |
| **GAIA (Commander)** | 165 tasks | **69.7%** | Bare MiMo 21.2% | `docs/benchmark-results/gaia-commander-final/` |
| **BFCL (35 scenarios)** | 35 scenarios | Tool **60.0%** / Param **91.4%** | — | `benchmarks/bfcl/results_full.json` + 35 response files |
| **BFCL (12 core)** | 12 scenarios | Tool **91.7%** / Param **91.7%** | Llama 405B 88.5% | `benchmarks/bfcl/results.json` + 12 response files |
| **MT-Bench** | 5 questions (subset) | **7.8/10** | — | `docs/benchmark-results/mtbench/` |
| **PinchBench** | 43 tasks | **97.7%** (42/43) | OpenClaw 89.5% | `docs/benchmark-results/pinchbench-final42/` |


## 主な節

### Results Summary

**Results Summary** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Key Insight

**Key Insight** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Benchmark Details

**Benchmark Details** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Running Benchmarks Yourself

**Running Benchmarks Yourself** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```bash
cd packages/core

# Run all benchmarks
npx tsx --test tests/benchmark.test.ts

# Run specific benchmarks
npx tsx benchmark.ts --benchmark gaia
npx tsx benchmark.ts --benchmark bfcl
npx tsx benchmark.ts --benchmark pinchbench
```

## 運用チェック

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 関連

- [アーキテクチャ概要](/ja/architecture/overview)
- [本番準備](/ja/architecture/production-readiness)
- [セキュリティ](/ja/guide/security)
- [クイックスタート](/ja/guide/getting-started)
