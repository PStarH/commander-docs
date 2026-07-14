# API 参考

Commander has **two layers** of API surface. Most apps only need Layer 1. Architecture V2 durable API: `POST /v1/runs` — see [V2 Migration](/guide/migration-v2).

本文说明 **API 参考** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

```bash
import { CommanderClient, createClient } from '@commander/sdk';

const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const result = await client.run('audit this repo');
console.log(result.status, result.summary);
await client.disconnect();

```

## 要点

- 与英文源文档语义对齐；API 与 CLI 以 monorepo 为准  
- 需要可运行示例时，优先使用 [快速开始](/zh/guide/getting-started) 中的 `cliEntry.ts` 路径  
- 指标口径：25 提供商 · 5 拓扑 · 18 工具 · 6700+ 测试  

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [API 概览](/zh/api/overview)  
