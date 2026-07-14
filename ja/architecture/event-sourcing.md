# イベントソーシングと復旧

Commander's event sourcing system provides crash-safe execution with tamper-proof audit trails, deterministic replay, and automatic zombie run recovery. The `EventSourcingEngine` implements the IEventSourcingEngine contract (Pillar I) with a Write-Ahead Log (WAL) and SHA-256 hash chain for tamper protection.

本ページは Commander における **イベントソーシングと復旧** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
[event 1] → SHA256("") → hash_1
[event 2] → SHA256(hash_1 | type | id | timestamp | payload) → hash_2
[event 3] → SHA256(hash_2 | type | id | timestamp | payload) → hash_3
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
