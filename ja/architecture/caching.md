# Caching

Commander implements a multi-level caching layer to reduce LLM calls, improve response times, and prevent redundant computation. Each cache is per-tenant isolated. An exact-match cache keyed by SHA-256 hash of `(tenantId + tool + args)`:

本ページは Commander における **Caching** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
Tool Call
  │
  ├─ SingleFlightRequestCache  ── Deduplicates concurrent identical requests
  │   (First request executes, subsequent wait for result)
  │
  ├─ ToolResultCache           ── SHA-256 exact-match cache
  │   (Deterministic tools: read file, search code, etc.)
  │
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
