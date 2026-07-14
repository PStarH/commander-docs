# 交互式拓扑探索器

Pick a task shape. Commander’s deliberation engine maps similar signals onto one of **five canonical topologies**. This page is a decision aid — not a substitute for `plan`. Answer mentally, then confirm with `plan`:

本文说明 **交互式拓扑探索器** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

```bash
Is the task a single clear question with one owner?
  YES → SINGLE
  NO  ↓
Does work form a strict pipeline (A then B then C)?
  YES → CHAIN
  NO  ↓
Can specialists work in parallel then merge?
  YES → DISPATCH
```

## 要点

- 与英文源文档语义对齐；API 与 CLI 以 monorepo 为准  
- 需要可运行示例时，优先使用 [快速开始](/zh/guide/getting-started) 中的 `cliEntry.ts` 路径  
- 指标口径：25 提供商 · 5 拓扑 · 18 工具 · 6700+ 测试  

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [API 概览](/zh/api/overview)  
