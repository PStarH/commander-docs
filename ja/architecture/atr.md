# Agent Transaction Runtime (ATR)

ATR is the **settlement layer** that sits between the agent's decision loop and every external system call. It guarantees that agent actions are idempotent, recoverable, leased, and fenced. Without ATR, agent execution is fire-and-forget: if a tool call succeeds but the agent crashes before recording the result, the action is lost. If the agent retries, the action executes twice. ATR solves this w

本ページは Commander における **Agent Transaction Runtime (ATR)** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
Agent Decision → ATR Settlement Layer → External System
                    ├── Idempotency (no duplicates)
                    ├── Recovery (compensable rollback)
                    ├── Leasing (single-owner runs)
                    └── Fencing (zombie process protection)
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
