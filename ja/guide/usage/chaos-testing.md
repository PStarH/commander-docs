# Chaos Testing

Commander includes a built-in chaos engineering framework that injects faults across 4 layers and verifies recovery. Use it to validate that your agent deployment can survive real-world failures. Every chaos run calls `RecoveryBootstrapper.bootstrap()` after fault injection. If recovery fails, the run is marked failed in the report.

本ページは Commander における **Chaos Testing** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
# Run a single-layer chaos test
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1 --tenant=ci-staging

# Run multi-layer chaos test
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3 --tenant=ci-staging --duration=60

# With recovery verification (default)
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2 --tenant=ci-staging
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
