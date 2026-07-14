# Web Console

Commander の **Web Console** について、使い方と運用上の注意をまとめます。

## クイック

```bash
cd Commander
pnpm install
export OPENAI_API_KEY=sk-...   # or other provider
pnpm gui
```


## ポイント

- CLI は monorepo の `cliEntry.ts`、ビルド後は `commander`  
- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 詳細な挙動は runtime / monorepo ソースを正とする  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
