# Contributing to the docs

Thank you for improving Commander documentation. 1. **Metrics:** `25 providers` · `5 topologies` · `18 built-in tools` · `6700+ tests`

本文说明 **Contributing to the docs** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

```bash
git clone https://github.com/PStarH/commander-docs.git
cd commander-docs
npm install
npm run dev      # http://localhost:5173/commander-docs/
npm run check    # content guards
npm run build
```

## 要点

- 与英文源文档语义对齐；API 与 CLI 以 monorepo 为准  
- 需要可运行示例时，优先使用 [快速开始](/zh/guide/getting-started) 中的 `cliEntry.ts` 路径  
- 指标口径：25 提供商 · 5 拓扑 · 18 工具 · 6700+ 测试  

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [API 概览](/zh/api/overview)  
