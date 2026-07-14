# Architecture V2 Migration

Migrate from legacy V1 execution paths to the **Architecture V2** durable kernel: control plane schedules work; workers execute steps; state lives in PostgreSQL. - `POST /v1/runs` · `GET /v1/runs/:id` · `GET /v1/runs/:id/steps` · `GET /v1/runs/:id/events`

本ページは Commander における **Architecture V2 Migration** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
# After setting DATABASE_URL
pnpm db:migrate   # from monorepo — see product scripts
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
