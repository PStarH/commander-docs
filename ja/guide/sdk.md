# Agent SDK (TypeScript)

Commander の **Agent SDK (TypeScript)** について、使い方と運用上の注意をまとめます。

## クイック

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
pnpm --filter @commander/sdk build
```


## ポイント

- CLI は monorepo の `cliEntry.ts`、ビルド後は `commander`  
- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 詳細な挙動は runtime / monorepo ソースを正とする  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
