# Model Context Protocol (MCP)

Commander supports the [Model Context Protocol](https://modelcontextprotocol.io) for connecting to external MCP servers and exposing Commander's capabilities as MCP services. Connect to any MCP-compatible server to extend Commander with external tools:

本ページは Commander における **Model Context Protocol (MCP)** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
mcp/
├── client.ts        ← MCP client for connecting to external servers
├── server.ts        ← MCP server for exposing Commander capabilities
├── a2aClient.ts     ← Agent-to-Agent (A2A) protocol client
├── a2aServer.ts     ← A2A protocol server
├── a2aCompliance.ts ← A2A compliance validation
├── types.ts         ← Shared MCP types
└── index.ts         ← Public exports
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
