# Cookbook: Refactor a module safely

**Goal:** Use plan mode to preview a refactor, then execute with controlled approval. **Time:** ~15 minutes · **Risk:** writes files — start in `plan` / `suggest`

本ページは Commander における **Cookbook: Refactor a module safely** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
cd /path/to/your-project   # or the Commander monorepo for a dry run
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=plan
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
