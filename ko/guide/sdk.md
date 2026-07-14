# Agent SDK (TypeScript)

`@commander/sdk`로 앱에 Commander를 임베드합니다.

> **상태:** 패키지는 monorepo `packages/sdk`. **npm 공개는 아직 주 설치 경로가 아닙니다** — clone 후 workspace 빌드.

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

제로 설정:

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

| 옵션 | 기본 | 설명 |
|------|------|------|
| `provider` | auto | `openai`, `anthropic`, `ollama`, … |
| `apiKey` | env | 명시 키 |
| `model` | provider default | 모델 오버라이드 |
| `baseUrl` | provider default | OpenAI 호환 base URL |
| `tokenBudget` | `64000` | 소프트 예산 |
| `defaultTopology` | `SINGLE` | 폴백 토폴로지 |
| `persistSessions` | `true` | 세션 요약 유지 |

## 핵심 메서드

| 메서드 | 설명 |
|--------|------|
| `connect` / `disconnect` | 런타임·이벤트 버스 연결 |
| `run(task)` | 멀티 에이전트 실행 → `ExecutionResult` |
| `plan(task)` | 심의만 |
| `onEvent(handler)` | 라이프사이클 이벤트 |
| `createAgent(config)` | 에이전트 프로필 |
| `writeMemory` / `queryMemory` | 3계층 메모리 |

## HTTP API (서버 모드)

`docker compose` 또는 `pnpm gui` 시 REST + SSE:

```bash
curl http://localhost:4000/health

curl -X POST http://localhost:4000/execute \
  -H "Authorization: Bearer $COMMANDER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"task":"analyze this repository","mode":"plan"}'
```

[배포](/ko/deployment) · [Python SDK](/ko/guide/sdk-python).

## 다음

- [Python SDK](/ko/guide/sdk-python)  
- [명령](/ko/guide/commands)  
- [API 개요](/ko/api/overview)  
