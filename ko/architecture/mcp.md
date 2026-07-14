# Model Context Protocol (MCP)

Commander는 [Model Context Protocol](https://modelcontextprotocol.io) 을 지원합니다. 외부 MCP 서버에 연결하거나 Commander 능력을 MCP 서비스로 노출할 수 있습니다.

## 구조

```
mcp/
├── client.ts        ← 외부 MCP 서버 클라이언트
├── server.ts        ← Commander 능력을 노출하는 MCP 서버
├── a2aClient.ts     ← Agent-to-Agent (A2A) 클라이언트
├── a2aServer.ts     ← A2A 서버
├── a2aCompliance.ts ← A2A 준수 검증
├── types.ts
└── index.ts
```

## MCP 클라이언트

외부 도구로 Commander를 확장합니다.

```typescript
import { MCPClient } from '@commander/core';

const client = new MCPClient({
  serverUrl: 'http://localhost:8080/mcp',
  capabilities: ['tools', 'resources'],
});

await client.connect();
const tools = await client.listTools();
const result = await client.callTool('external-tool', { arg: 'value' });
```

## MCP 서버

다른 AI 에이전트가 쓸 수 있도록 Commander 도구를 노출합니다.

```typescript
import { MCPServer } from '@commander/core';

const server = new MCPServer({
  port: 8080,
  tools: ['web_search', 'file_read', 'git'],
  auth: { apiKey: 'sk-...' },
});

await server.start();
```

## Agent-to-Agent (A2A)

시스템 간 직접 에이전트 위임:

```typescript
import { A2AClient, A2AServer } from '@commander/core';

const a2aServer = new A2AServer({
  agent: myAgent,
  capabilities: ['task_delegation', 'status_reporting'],
});

const a2aClient = new A2AClient({
  remoteUrl: 'http://other-agent:8081/a2a',
});
const result = await a2aClient.delegateTask({
  description: 'analyze this dataset',
  context: { file: '/data/set.csv' },
});
```

## MCP Tool Adapter

MCP 서버 도구를 네이티브 Commander 도구로 마운트해 토폴로지·품질 게이트와 동일한 파이프라인을 타게 합니다.

> 패키지는 monorepo `packages/core`. 설치는 clone + `pnpm install` 이 주 경로입니다.  
> CLI: `npx tsx packages/core/src/cliEntry.ts`

## 관련

- [도구](/ko/architecture/tools)  
- [에이전트 팀](/ko/guide/advanced/agent-teams)  
- [커스텀 도구](/ko/guide/advanced/custom-tools)  
- [보안](/ko/guide/security)  
