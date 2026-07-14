# API Reference

Commander has **two layers** of API surface. Most apps only need Layer 1. Architecture V2 durable API: `POST /v1/runs` — see [V2 Migration](/guide/migration-v2).

本ページは Commander における **API Reference** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
import { CommanderClient, createClient } from '@commander/sdk';

const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const result = await client.run('audit this repo');
console.log(result.status, result.summary);
await client.disconnect();

```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
