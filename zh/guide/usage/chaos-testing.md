# 混沌测试

Commander includes a built-in chaos engineering framework that injects faults across 4 layers and verifies recovery. Use it to validate that your agent deployment can survive real-world failures. Every chaos run calls `RecoveryBootstrapper.bootstrap()` after fault injection. If recovery fails, the run is marked failed in the report.

本文说明 **混沌测试** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

```bash
# Run a single-layer chaos test
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1 --tenant=ci-staging

# Run multi-layer chaos test
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2,L3 --tenant=ci-staging --duration=60

# With recovery verification (default)
npx tsx packages/core/src/cli/commands/chaos.ts --layers=L1,L2 --tenant=ci-staging
```

## 要点

- 与英文源文档语义对齐；API 与 CLI 以 monorepo 为准  
- 需要可运行示例时，优先使用 [快速开始](/zh/guide/getting-started) 中的 `cliEntry.ts` 路径  
- 指标口径：25 提供商 · 5 拓扑 · 18 工具 · 6700+ 测试  

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [API 概览](/zh/api/overview)  
