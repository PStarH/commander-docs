# CLI Commands

Examples use the `commander` binary (available after building `@commander/core`). From a source checkout without a build, replace `commander` with:

本文说明 **CLI Commands** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

```bash
npx tsx packages/core/src/cliEntry.ts
```

## 要点

- 与英文源文档语义对齐；API 与 CLI 以 monorepo 为准  
- 需要可运行示例时，优先使用 [快速开始](/zh/guide/getting-started) 中的 `cliEntry.ts` 路径  
- 指标口径：25 提供商 · 5 拓扑 · 18 工具 · 6700+ 测试  

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [API 概览](/zh/api/overview)  
