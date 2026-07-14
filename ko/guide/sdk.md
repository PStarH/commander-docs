# Agent SDK (TypeScript)

`@commander/sdk`로 앱에 Commander를 임베드합니다.

> **상태:** 패키지는 monorepo의 `packages/sdk`에 있습니다. **npm 공개는 아직 주 설치 경로가 아닙니다** — monorepo를 클론하고 workspace를 빌드하세요.

## 설치

### monorepo (오늘 권장)

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
pnpm --filter @commander/sdk build
```

앱에서 `"@commander/sdk": "workspace:*"` 또는 개발 중 `packages/sdk` import.

### npm 공개 시 (예정)

```bash
# 공개 후에만 — 빠른 시작 경로 아님
pnpm add @commander/sdk
```

## 빠른 시작

```typescript
import { CommanderClient } from "@commander/sdk";

const client = new CommanderClient({ provider: "openai" });
await client.connect();

const result = await client.run("analyze this repository structure");
console.log(result.status, result.summary);

await client.disconnect();
```

제로 설정 (환경에서 프로바이더 자동 감지):

```typescript
import { createClient } from "@commander/sdk";

const client = await createClient();
const result = await client.run("audit this repo for security vulnerabilities");
await client.disconnect();
```

## 실행 없이 plan

```typescript
const plan = await client.plan("refactor the auth module");
console.log(plan);
```

## 실시간 이벤트

```typescript
const unsub = client.onEvent((event) => {
  console.log(`[${event.type}]`, event.data);
});

await client.run("debug the failing test");
unsub();
```

## 설정

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

## 관련

- [빠른 시작](/ko/guide/getting-started)
- [Python SDK](/ko/guide/sdk-python)
- [API 개요](/ko/api/overview)
