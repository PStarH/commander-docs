# Model Context Protocol (MCP)

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/architecture/mcp)



Commander supports the [Model Context Protocol](https://modelcontextprotocol.io) for connecting to external MCP servers and exposing Commander's capabilities as MCP services.

## Architecture


```
mcp/
├── client.ts        ← MCP client for connecting to external servers
├── server.ts        ← MCP server for exposing Commander capabilities
├── a2aClient.ts     ← Agent-to-Agent (A2A) protocol client
├── a2aServer.ts     ← A2A protocol server
├── a2aCompliance.ts ← A2A compliance validation
├── types.ts         ← Shared MCP types
└── index.ts         ← Public exports
```

## MCP Client


Connect to any MCP-compatible server to extend Commander with external tools:

```typescript
import { MCPClient } from '@commander/core';

const client = new MCPClient({
  serverUrl: 'http://localhost:8080/mcp',
  capabilities: ['tools', 'resources'],
});

await client.connect();

// List available tools from the MCP server
const tools = await client.listTools();

// Call an MCP tool
const result = await client.callTool('external-tool', { arg: 'value' });
```

## MCP Server


Expose Commander's capabilities as an MCP server for other AI agents:

```typescript
import { MCPServer } from '@commander/core';

const server = new MCPServer({
  port: 8080,
  tools: ['web_search', 'file_read', 'git'], // which tools to expose
  auth: { apiKey: 'sk-...' },
});

await server.start();
```

## Agent-to-Agent (A2A) Protocol


Commander implements the A2A protocol for direct agent-to-agent communication across different systems:

```typescript
import { A2AClient, A2AServer } from '@commander/core';

// Server: expose an agent for remote delegation
const a2aServer = new A2AServer({
  agent: myAgent,
  capabilities: ['task_delegation', 'status_reporting'],
});

// Client: delegate tasks to remote agents
const a2aClient = new A2AClient({
  remoteUrl: 'http://other-agent:8081/a2a',
});
const result = await a2aClient.delegateTask({
  description: 'analyze this dataset',
  context: { file: '/data/set.csv' },
});
```

## MCP Tool Adapter


Mount MCP server tools as native Commander tools:

```typescript
import { MCPToolAdapter } from '@commander/core';

const adapter = new MCPToolAdapter({
  serverUrl: 'http://localhost:8080/mcp',
  toolName: 'external-api',
});

runtime.registerTool('external-api', adapter);
```

## Use Cases


- **Extend toolset** — Connect to databases, APIs, or internal services via MCP
- **Cross-platform A2A** — Commander agents collaborating with other AI agent systems
- **Plugin ecosystem** — Third-party MCP servers providing specialized capabilities
- **Legacy integration** — Wrap existing tools and services as MCP endpoints
