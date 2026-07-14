# Agent SDK (TypeScript)

```typescript
import { CommanderClient, createClient } from '@commander/sdk';

const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const result = await client.run('analyze this repository structure');
await client.disconnect();

const c = await createClient();
await c.run('audit this repo');
await c.disconnect();
```

| 메서드 | 역할 |
|--------|------|
| `connect` / `disconnect` | 생명주기 |
| `run` | 전체 실행 |
| `plan` | 심의만 |
| `onEvent` | 이벤트 구독 |

npm 공개 진행 중 — monorepo 사용 권장.

[배포](/ko/deployment) · [Python SDK](/ko/guide/sdk-python)
