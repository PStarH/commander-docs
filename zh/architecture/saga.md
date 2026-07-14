# Saga Transactions

Commander implements the saga pattern for distributed compensating transactions — ensuring data consistency across multi-step operations where each step can be rolled back independently. Define sagas with forward actions and their compensating rollbacks:

本文说明 **Saga Transactions** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

```bash
SagaBuilder.define()
  │
  ├─ Step 1: Create resource   → Compensation: Delete resource
  ├─ Step 2: Update resource   → Compensation: Revert update
  ├─ Step 3: Send notification → Compensation: Void notification
  │
  └─ Coordinator.execute(saga)
       │
```

## 要点

- 与英文源文档语义对齐；API 与 CLI 以 monorepo 为准  
- 需要可运行示例时，优先使用 [快速开始](/zh/guide/getting-started) 中的 `cliEntry.ts` 路径  
- 指标口径：25 提供商 · 5 拓扑 · 18 工具 · 6700+ 测试  

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [API 概览](/zh/api/overview)  
