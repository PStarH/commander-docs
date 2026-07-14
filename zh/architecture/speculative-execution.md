# Speculative Execution

Commander implements **PASTE-style speculative execution** (Pattern-Aware Speculative Execution) that pre-executes likely tool calls during LLM thinking time. Research shows this achieves up to 48.5% reduction in task completion time. During LLM thinking/processing time, Commander predicts the most likely next tool calls based on observed patterns and pre-executes them. If the model actually makes

本文说明 **Speculative Execution** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

```bash
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  LLM Call   │────▶│ Pattern Tracker  │────▶│ Speculative     │
│  (thinking) │     │ (predict next)   │     │ Executor        │
└─────────────┘     └──────────────────┘     └────────┬────────┘
                                                       │
                         ┌─────────────────────────────┘
                         ▼
               ┌──────────────────┐
```

## 要点

- 与英文源文档语义对齐；API 与 CLI 以 monorepo 为准  
- 需要可运行示例时，优先使用 [快速开始](/zh/guide/getting-started) 中的 `cliEntry.ts` 路径  
- 指标口径：25 提供商 · 5 拓扑 · 18 工具 · 6700+ 测试  

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [API 概览](/zh/api/overview)  
