# Cookbook: CI full-auto lint fix

**Goal:** Run Commander non-interactively in CI to fix lint (or similar) issues. **Time:** ~15 minutes to wire · **Risk:** high autonomy — isolate to a job with PR review

本ページは Commander における **Cookbook: CI full-auto lint fix** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors in this repository" --stream
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
