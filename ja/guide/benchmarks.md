# ベンチマーク

Commander is benchmarked across **security, reliability, performance, chaos, and capability**. Numbers below are from the product README / monorepo scripts — re-run them yourself for current baselines. **Source of truth:** monorepo [`BENCHMARK.md`](https://github.com/PStarH/Commander/blob/master/BENCHMARK.md).

本ページは Commander における **ベンチマーク** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
pnpm benchmark:all          # multi-suite readiness
pnpm benchmark:redteam      # 47 scenarios
pnpm benchmark:agentdojo    # injection suite
pnpm benchmark:chaos        # chaos (simulated default)
pnpm bench:slo              # SLO baseline
pnpm check:readiness        # baseline freshness
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
