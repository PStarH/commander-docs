# Frequently Asked Questions

Commander の **Frequently Asked Questions** について、使い方と運用上の注意をまとめます。

## クイック

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```


## ポイント

- CLI は monorepo の `cliEntry.ts`、ビルド後は `commander`  
- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 詳細な挙動は runtime / monorepo ソースを正とする  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
