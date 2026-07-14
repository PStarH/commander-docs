# 为什么选 Commander

Commander 面向 **拒绝把多代理当黑盒** 的工程师。

**不画图、不写 YAML、不「祈祷代理跑对了」。**  
一把 Key → 任务分类 → 选拓扑 → 流式输出每一步 → 校验每一次结果。

## 一览对比

| 维度 | Commander | 常见代理框架 |
|------|-----------|--------------|
| **上手** | 自然语言任务 + 一把 Key | 先建图 / 写 YAML 工作流 |
| **拓扑** | 5 种规范拓扑自动选择 | 自己连边 |
| **可见性** | 实时 SSE：思考、工具、质量门 | 事后日志或黑盒 |
| **质量** | 五层门禁（幻觉、一致性、完整性、准确、安全） | 可选 / 自建 |
| **提供商** | 25 家，自动发现 + 故障转移 | 往往 1–2 家一等公民 |
| **生产** | 熔断、DLQ、Saga、WAL 检查点、多租户 | 演示优先，运维后补 |
| **接入面** | CLI / TS SDK / HTTP / Python | 通常单一表面 |

## 适合 / 不适合

**适合你，如果：**

- 需要 **边跑边看** 代理在做什么  
- 希望拓扑与代理数量自动决定  
- 关心故障转移、检查点、审计  
- 更爱 CLI/SDK 而不是可视化画图  
- 有安全敏感或多租户场景  

**可以考虑别的，如果：**

- 只要单次 chat + tools  
- 只要全托管 SaaS、完全不想自建（云产品仍在 [路线图](/zh/community)）  
- 强依赖纯 Python 进程内框架  

## 60 秒体验

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "explain this repository architecture" --stream
```

成功信号：审议分类 → 拓扑选择 → 代理步骤 → 流中的质量门。

## 更多

- [快速开始](/zh/guide/getting-started)  
- [实战手册](/zh/guide/cookbook/)  
- [英文架构总览](/architecture/overview)  
