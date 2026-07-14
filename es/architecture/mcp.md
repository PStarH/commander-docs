# Integración MCP

Documentación en español de **Integración MCP**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

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

```typescript
import { MCPServer } from '@commander/core';

const server = new MCPServer({
  port: 8080,
  tools: ['web_search', 'file_read', 'git'], // which tools to expose
  auth: { apiKey: 'sk-...' },
});

await server.start();
```



## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
