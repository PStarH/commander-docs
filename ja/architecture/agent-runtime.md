# エージェントランタイム

The execution engine at the heart of Commander. The `AgentRuntime` manages the full lifecycle of a single agent: LLM calls, tool execution, verification, checkpointing, and retry — all within configurable token and step budgets. Each agent run follows this sequence:

本ページは Commander における **エージェントランタイム** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
AgentRuntime.execute(ctx)
  │
  ├─ acquireSlot()        ← Concurrency semaphore
  ├─ [Tenant check]       ← Rate limit + concurrency quota
  ├─ resolve storage      ← Tenant-scoped memory + caching
  │
  ├─ [Retry loop: 0..maxRetries]
  │   ├─ callWithTimeout()       ← LLM provider call
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
