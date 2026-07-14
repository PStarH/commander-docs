# Cookbook: Refactor a module safely

Commander の **Cookbook: Refactor a module safely** について、使い方と運用上の注意をまとめます。

## クイック

```bash
cd /path/to/your-project   # or the Commander monorepo for a dry run
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=plan
```


## ポイント

- CLI は monorepo の `cliEntry.ts`、ビルド後は `commander`  
- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 詳細な挙動は runtime / monorepo ソースを正とする  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
