# Model Context Protocol (MCP)

**Model Context Protocol (MCP).** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Contenu principal

### Architecture

En pratique, **Architecture** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/mcp) pour le détail exhaustif.

### MCP Client

En pratique, **MCP Client** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/mcp) pour le détail exhaustif.

### MCP Server

En pratique, **MCP Server** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/mcp) pour le détail exhaustif.

### Agent-to-Agent (A2A) Protocol

En pratique, **Agent-to-Agent (A2A) Protocol** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/mcp) pour le détail exhaustif.

### MCP Tool Adapter

En pratique, **MCP Tool Adapter** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/mcp) pour le détail exhaustif.

### Use Cases

En pratique, **Use Cases** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/mcp) pour le détail exhaustif.

## Exemples (code inchangé)

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

## Opérations

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## Voir aussi

- [Vue d’architecture](/fr/architecture/overview)
- [Prêt production](/fr/architecture/production-readiness)
- [Sécurité](/fr/guide/security)
- [Démarrage rapide](/fr/guide/getting-started)
