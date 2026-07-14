# Supervision Tree

Commander implements an **Erlang/OTP-inspired supervision tree** for fault isolation. Instead of handling every possible error within an agent, agents crash and supervisors restart them automatically — the "Let It Crash" philosophy. Traditional error handling tries to catch and recover from every failure. This leads to complex, fragile code. Supervision trees flip the model: let agents crash, and 

本ページは Commander における **Supervision Tree** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
┌──────────────────┐
                    │  Root Supervisor │
                    │  (strategy: one_for_one) │
                    └────────┬─────────┘
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │ Agent 1  │  │ Agent 2  │  │ Agent N  │
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
