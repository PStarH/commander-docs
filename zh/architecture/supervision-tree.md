# Supervision Tree

Commander implements an **Erlang/OTP-inspired supervision tree** for fault isolation. Instead of handling every possible error within an agent, agents crash and supervisors restart them automatically — the "Let It Crash" philosophy. Traditional error handling tries to catch and recover from every failure. This leads to complex, fragile code. Supervision trees flip the model: let agents crash, and 

本文说明 **Supervision Tree** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

```bash
┌──────────────────┐
                    │  Root Supervisor │
                    │  (strategy: one_for_one) │
                    └────────┬─────────┘
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │ Agent 1  │  │ Agent 2  │  │ Agent N  │
```

## 要点

- 与英文源文档语义对齐；API 与 CLI 以 monorepo 为准  
- 需要可运行示例时，优先使用 [快速开始](/zh/guide/getting-started) 中的 `cliEntry.ts` 路径  
- 指标口径：25 提供商 · 5 拓扑 · 18 工具 · 6700+ 测试  

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [API 概览](/zh/api/overview)  
