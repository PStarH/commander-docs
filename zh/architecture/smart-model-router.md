# Smart Model Router

The Smart Model Router provides **capability-based model selection** with user-configurable routing rules. It wraps the core `ModelRouter` with an extended API for defining model pools, routing rules, and budget constraints. Models are tagged with capability types for matching:

本文说明 **Smart Model Router** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

```bash
import { SmartModelRouter } from '@commander/core';

const router = new SmartModelRouter({
  mode: 'cascade',  // auto | manual | cascade
  modelPool: [
    {
      id: 'gpt-4o',
      provider: 'openai',
```

## 要点

- 与英文源文档语义对齐；API 与 CLI 以 monorepo 为准  
- 需要可运行示例时，优先使用 [快速开始](/zh/guide/getting-started) 中的 `cliEntry.ts` 路径  
- 指标口径：25 提供商 · 5 拓扑 · 18 工具 · 6700+ 测试  

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [API 概览](/zh/api/overview)  
