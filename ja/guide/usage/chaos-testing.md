# カオステスト

カオステストは意図的に障害を入れ、レジリエンス（ブレーカー、フォールバック、チェックポイント、DLQ）が期待どおり動くかを検証します。

## 目的

- プロバイダー・タイムアウト / rate limit 時のフォールバック  
- クラッシュ後のチェックポイント再開  
- ブレーカー open / half-open  
- DLQ 蓄積と再実行  

## monorepo で

製品 CI と `packages/core` テストにカオス・ストレスが含まれます。

```bash
cd packages/core
npx tsx --test tests/*.test.ts
```

ベンチマーク・レッドチームは monorepo の `pnpm benchmark:*` を参照。

## ローカル練習

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo"
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts doctor --reset
```

本番でカオスを入れる場合はカナリア・シャードを使います。

## 関連

- [Resilience](/ja/architecture/resilience)  
- [イベントソーシング](/ja/architecture/event-sourcing)  
- [シャード・トラフィック](/ja/guide/usage/shadow-traffic)  
- [ベンチマーク](/ja/guide/benchmarks)  
