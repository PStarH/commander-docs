# Model Context Protocol (MCP)

**Model Context Protocol (MCP).** Commander monorepo 구성 요소에 대한 한국어 운영 문서입니다. 코드·식별자는 영어를 유지하며, CLI는 `npx tsx packages/core/src/cliEntry.ts` 를 우선합니다. 제품 지표: 25 프로바이더 · 5 토폴로지 · 18 tools · 6700+ 테스트.

## 주요 섹션

### Architecture

**Architecture** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### MCP Client

**MCP Client** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### MCP Server

**MCP Server** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Agent-to-Agent (A2A) Protocol

**Agent-to-Agent (A2A) Protocol** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### MCP Tool Adapter

**MCP Tool Adapter** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Use Cases

**Use Cases** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

## 예제

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

## 운영 체크

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 관련

- [아키텍처 개요](/ko/architecture/overview)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [보안](/ko/guide/security)
- [빠른 시작](/ko/guide/getting-started)
