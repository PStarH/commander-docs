# Agent SDK (TypeScript)

`@commander/sdk` でアプリに Commander を埋め込みます。

> **状態:** パッケージは monorepo の `packages/sdk`。**npm 公開はまだ主インストール経路ではない** — monorepo を clone して workspace をビルド。

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
# 公開後のみ — クイックスタート経路ではない
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

## 関連

- [クイックスタート](/ja/guide/getting-started)
- [Python SDK](/ja/guide/sdk-python)
- [API 概要](/ja/api/overview)
