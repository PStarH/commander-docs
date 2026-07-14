# Model Context Protocol (MCP)

Commander prend en charge le [Model Context Protocol](https://modelcontextprotocol.io) : connexion à des serveurs MCP externes et exposition des capacités Commander en services MCP.

## Architecture

```
mcp/
├── client.ts        ← client vers serveurs MCP externes
├── server.ts        ← serveur MCP exposant Commander
├── a2aClient.ts     ← client Agent-to-Agent (A2A)
├── a2aServer.ts     ← serveur A2A
├── a2aCompliance.ts ← validation de conformité A2A
├── types.ts
└── index.ts
```

## Client MCP

Étendre Commander avec des tools externes :

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

## Serveur MCP

Exposer des tools Commander à d’autres agents :

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

Délégation directe inter-systèmes :

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

Monter les tools d’un serveur MCP comme tools natifs Commander (même pipeline topologie / portes qualité).

> Packages monorepo `packages/core`. Install principal : clone + `pnpm install`.  
> CLI : `npx tsx packages/core/src/cliEntry.ts`

## Voir aussi

- [Tools](/fr/architecture/tools)  
- [Agent teams](/fr/guide/advanced/agent-teams)  
- [Custom tools](/fr/guide/advanced/custom-tools)  
- [Sécurité](/fr/guide/security)  
