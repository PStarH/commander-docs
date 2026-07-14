# 基准测试

Commander adds **+48.5 percentage points** over the bare MiMo base model on GAIA — demonstrating the power of multi-agent orchestration over single-agent baselines. - **Score**: 69.7% (115/165 correct)

本文说明 **基准测试** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

```bash
cd packages/core

# Run all benchmarks
npx tsx --test tests/benchmark.test.ts

# Run specific benchmarks
npx tsx benchmark.ts --benchmark gaia
npx tsx benchmark.ts --benchmark bfcl
```

## 要点

- 与英文源文档语义对齐；API 与 CLI 以 monorepo 为准  
- 需要可运行示例时，优先使用 [快速开始](/zh/guide/getting-started) 中的 `cliEntry.ts` 路径  
- 指标口径：25 提供商 · 5 拓扑 · 18 工具 · 6700+ 测试  

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [API 概览](/zh/api/overview)  
