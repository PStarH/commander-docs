# 校验流水线

Every agent output passes through a 5-gate quality verification pipeline before it is returned to the caller. This is not a "nice-to-have" check — it is an integral part of the runtime retry loop. The `UnifiedVerificationPipeline` orchestrates all 5 gates:

本文说明 **校验流水线** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

```bash
Agent output
  │
  ├─ Gate 1: Hallucination Detection
  │   └─ Signal-based detector with configurable thresholds
  │
  ├─ Gate 2: Consistency Check
  │   └─ Internal consistency and contradiction detection
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
