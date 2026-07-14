# プロバイダー

Commander supports **25 LLM providers**. Set any single environment variable—Commander auto-detects the provider. Commander uses a `modelRouter.ts` to select the optimal provider based on:

本ページは Commander における **プロバイダー** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
# The simplest setup—just one key lets Commander auto-select
export OPENAI_API_KEY=sk-...
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
