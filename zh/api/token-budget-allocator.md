# Token Budget Allocator

本页说明 Commander 中 **Token Budget Allocator** 的用途、操作方式与生产注意点。命令路径与产品 monorepo 保持一致。

## 快速入口

```bash
interface TokenBudget {
  totalBudget: number;
  perAgentBudget: number;
  reservedForTools: number;
  reservedForVerification: number;
}

interface AllocationResult {
  lead: number;
  specialists: number;
  evaluation: number;
  overhead: number;
```


## 说明

### Types

（对应英文文档章节 **Types** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）

### API

（对应英文文档章节 **API** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）

### Allocation by Topology

（对应英文文档章节 **Allocation by Topology** 的完整说明与示例见 monorepo / 英文源；下方给出可运行入口。）


## 指标口径

25 提供商 · 5 规范拓扑 · 18 内置工具 · 6700+ 测试。

## 相关

- [架构总览](/zh/architecture/overview)  
- [快速开始](/zh/guide/getting-started)  
- [命令](/zh/guide/commands)  
