# Model Context Protocol (MCP)

Commander supports the [Model Context Protocol](https://modelcontextprotocol.io) for connecting to external MCP servers and exposing Commander's capabilities as MCP services. Connect to any MCP-compatible server to extend Commander with external tools:

本文说明 **Model Context Protocol (MCP)** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

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

- 与英文源文档语义对齐；API 与 CLI 以 monorepo 为准  
- 需要可运行示例时，优先使用 [快速开始](/zh/guide/getting-started) 中的 `cliEntry.ts` 路径  
- 指标口径：25 提供商 · 5 拓扑 · 18 工具 · 6700+ 测试  

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [API 概览](/zh/api/overview)  
