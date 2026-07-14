# 워치 모드 (SSE)

실행 이벤트를 Server-Sent Events로 실시간 전송합니다.

```bash
npx tsx packages/core/src/cliEntry.ts watch "investigate this production bug"
```

이벤트: `task.start` · `deliberation` · `topology.select` · `agent.spawn` · `tool.call` · `verification` · `task.complete` …

```bash
npx tsx packages/core/src/cliEntry.ts watch "debug" | jq '.type'
```

```typescript
const unsub = client.onEvent((e) => console.log(e.type, e.data));
await client.run('debug the failing test');
```

[SDK](/ko/guide/sdk) · [Runtime](/ko/architecture/agent-runtime)
