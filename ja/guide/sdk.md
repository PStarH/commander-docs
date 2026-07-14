# Agent SDK (TypeScript)

`@commander/sdk` でアプリに Commander を埋め込みます。

> **状態:** パッケージは monorepo `packages/sdk`。**npm 公開はまだ主経路ではない** — clone して workspace をビルド。

## インストール

### monorepo（現在推奨）

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
pnpm --filter @commander/sdk build
```

`"@commander/sdk": "workspace:*"` または開発中 `packages/sdk` import。

### npm 公開後（予定）

```bash
# 公開後のみ
pnpm add @commander/sdk
```

## クイックスタート

```typescript
import { CommanderClient } from "@commander/sdk";

const client = new CommanderClient({ provider: "openai" });
await client.connect();

const result = await client.run("analyze this repository structure");
console.log(result.status, result.summary);

await client.disconnect();
```

ゼロ設定:

```typescript
import { createClient } from "@commander/sdk";

const client = await createClient();
const result = await client.run("audit this repo for security vulnerabilities");
await client.disconnect();
```

## plan のみ

```typescript
const plan = await client.plan("refactor the auth module");
console.log(plan);
```

## リアルタイムイベント

```typescript
const unsub = client.onEvent((event) => {
  console.log(`[${event.type}]`, event.data);
});

await client.run("debug the failing test");
unsub();
```

## 設定

```typescript
const client = new CommanderClient({
  provider: "anthropic",
  apiKey: process.env.ANTHROPIC_API_KEY,
  model: "claude-sonnet-4-20250514",
  tokenBudget: 64_000,
  defaultTopology: "SINGLE",
  persistSessions: true,
});
```

| オプション | 既定 | 説明 |
|------------|------|------|
| `provider` | auto | `openai`, `anthropic`, `ollama`, … |
| `apiKey` | env | 明示キー |
| `model` | provider default | モデル上書き |
| `baseUrl` | provider default | OpenAI 互換 base URL |
| `tokenBudget` | `64000` | ソフト予算 |
| `defaultTopology` | `SINGLE` | フォールバック |
| `persistSessions` | `true` | セッション要約保持 |

## コア・メソッド

| メソッド | 説明 |
|----------|------|
| `connect` / `disconnect` | ランタイム接続 |
| `run(task)` | フル実行 → `ExecutionResult` |
| `plan(task)` | 審議のみ |
| `onEvent(handler)` | イベント購読 |
| `createAgent` / memory helpers | 高度な制御 |

## HTTP API

```bash
curl http://localhost:4000/health

curl -X POST http://localhost:4000/execute \
  -H "Authorization: Bearer $COMMANDER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"task":"analyze this repository","mode":"plan"}'
```

[デプロイ](/ja/deployment) · [Python SDK](/ja/guide/sdk-python)。

## 次へ

- [Python SDK](/ja/guide/sdk-python)  
- [コマンド](/ja/guide/commands)  
- [API 概要](/ja/api/overview)  
