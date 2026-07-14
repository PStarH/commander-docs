# Backpressure Controller

The backpressure controller implements **unified admission control** for the Commander runtime, preventing overload when demand exceeds capacity. It uses a three-stage pipeline: Token Bucket → Ring Buffer → Circuit Breaker. 1. **Token Bucket** — Requests consume a token. When the bucket is empty, requests spill to the ring buffer.

本文说明 **Backpressure Controller** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

```bash
Producer → [Token Bucket] → [Ring Buffer] → [Circuit Breaker] → Consumer
              rate-limit       absorb bursts     protect when overwhelmed
```

## 要点

- 与英文源文档语义对齐；API 与 CLI 以 monorepo 为准  
- 需要可运行示例时，优先使用 [快速开始](/zh/guide/getting-started) 中的 `cliEntry.ts` 路径  
- 指标口径：25 提供商 · 5 拓扑 · 18 工具 · 6700+ 测试  

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [API 概览](/zh/api/overview)  
