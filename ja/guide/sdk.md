# Agent SDK (TypeScript)

Embed Commander in your own applications with `@commander/sdk`. Then depend on the workspace package from your app, or import from `packages/sdk` during development.

本ページは Commander における **Agent SDK (TypeScript)** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
pnpm --filter @commander/sdk build
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
