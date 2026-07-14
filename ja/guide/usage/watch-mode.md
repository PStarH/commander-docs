# Watch Mode (SSE Streaming)

Watch mode provides real-time streaming of every execution event via Server-Sent Events (SSE). This is ideal for monitoring long-running tasks, debugging agent behavior, or integrating with custom UIs. Every event in the execution pipeline is streamed:

本ページは Commander における **Watch Mode (SSE Streaming)** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
# From monorepo source (or: commander watch "...")
npx tsx packages/core/src/cliEntry.ts watch "investigate this production bug"
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
