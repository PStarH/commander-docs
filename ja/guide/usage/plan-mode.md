# プランモード

Plan mode lets you see what Commander will do **before** it does it. Switch to plan mode to review the execution strategy, agent allocation, and tool calls — with zero risk of unintended changes. - **Safety** — Review the full plan before any files are modified

本ページは Commander における **プランモード** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
# Set plan mode
npx tsx packages/core/src/cliEntry.ts mode plan

# Then run any task
npx tsx packages/core/src/cliEntry.ts run "refactor the database layer"

# Or use the --plan flag for one-off plan mode
npx tsx packages/core/src/cliEntry.ts plan "implement search feature"
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
