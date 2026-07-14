# 事件溯源与恢复

Commander's event sourcing system provides crash-safe execution with tamper-proof audit trails, deterministic replay, and automatic zombie run recovery. The `EventSourcingEngine` implements the IEventSourcingEngine contract (Pillar I) with a Write-Ahead Log (WAL) and SHA-256 hash chain for tamper protection.

本文说明 **事件溯源与恢复** 在 Commander 中的职责、使用方式与相关模块。命令与代码路径与产品保持一致。

```bash
[event 1] → SHA256("") → hash_1
[event 2] → SHA256(hash_1 | type | id | timestamp | payload) → hash_2
[event 3] → SHA256(hash_2 | type | id | timestamp | payload) → hash_3
```

## 要点

- 与英文源文档语义对齐；API 与 CLI 以 monorepo 为准  
- 需要可运行示例时，优先使用 [快速开始](/zh/guide/getting-started) 中的 `cliEntry.ts` 路径  
- 指标口径：25 提供商 · 5 拓扑 · 18 工具 · 6700+ 测试  

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [API 概览](/zh/api/overview)  
