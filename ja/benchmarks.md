# ベンチマーク（短縮入口）

詳細は [ガイド: ベンチマーク](/ja/guide/benchmarks) を参照してください。

- monorepo の再現スクリプトが真実源  
- 現在の製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト  
- 実行例: `pnpm benchmark:redteam` / `pnpm benchmark:agentdojo`  

```bash
npx tsx packages/core/src/cliEntry.ts doctor
```

## 関連

- [セキュリティ](/ja/guide/security)  
- [本番準備](/ja/architecture/production-readiness)  
