# Agent SDK (TypeScript)

```typescript
import { CommanderClient, createClient } from '@commander/sdk';

const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const result = await client.run('analyze this repository structure');
console.log(result.status, result.summary);
await client.disconnect();

const c = await createClient(); // 環境から自動検出
await c.run('audit this repo');
await c.disconnect();
```

## 主要メソッド

| メソッド | 役割 |
|----------|------|
| `connect` / `disconnect` | ライフサイクル |
| `run` | フル実行 |
| `plan` | 審議のみ |
| `onEvent` | イベント購読 |

npm 公開は進行中 — monorepo からの利用を推奨。

[デプロイ](/ja/deployment) · [Python SDK](/ja/guide/sdk-python)
