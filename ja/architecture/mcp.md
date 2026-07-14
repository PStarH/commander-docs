# Model Context Protocol (MCP)

Commander は [Model Context Protocol](https://modelcontextprotocol.io) をサポートします。外部 MCP サーバーへ接続し、Commander の能力を MCP サービスとして公開できます。

## 構造

```
mcp/
├── client.ts        ← 外部 MCP クライアント
├── server.ts        ← Commander を公開する MCP サーバー
├── a2aClient.ts     ← Agent-to-Agent (A2A) クライアント
├── a2aServer.ts     ← A2A サーバー
├── a2aCompliance.ts ← A2A 準拠検証
├── types.ts
└── index.ts
```

## MCP クライアント

外部ツールで Commander を拡張します。

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

## MCP サーバー

他の AI エージェント向けにツールを公開します。

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

システム横断の直接委譲:

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

MCP ツールをネイティブ Commander ツールとしてマウントし、トポロジ・品質ゲートと同じパイプラインに乗せます。

> パッケージは monorepo `packages/core`。導入は clone + `pnpm install`。  
> CLI: `npx tsx packages/core/src/cliEntry.ts`

## 関連

- [ツール](/ja/architecture/tools)  
- [エージェント・チーム](/ja/guide/advanced/agent-teams)  
- [カスタムツール](/ja/guide/advanced/custom-tools)  
- [セキュリティ](/ja/guide/security)  
