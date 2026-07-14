# 架构总览

Commander 是多代理编排引擎：把一段任务描述，变成跨代理、工具与 LLM 提供商的结构化执行计划。

## 先读这五页

如果刚接触系统，读完下面这些就够建立心智模型：

1. **本页** — 高层流程与包结构  
2. [核心调用链](/zh/architecture/core-call-chain) — 从请求到结果  
3. [多代理编排](/zh/architecture/multi-agent) — 拓扑与协作  
4. [代理运行时](/zh/architecture/agent-runtime) — LLM → 工具 → 校验 → 重试  
5. [校验流水线](/zh/architecture/verification) — 五层质量门  

其余（可靠性、安全、系统）属于可选深度——侧栏默认折叠。

## 高层流程

```
CLI / HTTP / SDK
  │
  ├─ deliberation.ts         任务分析与拓扑选择
  ├─ effortScaler.ts         按复杂度缩放代理数（1-20）
  ├─ topologyRouter.ts       路由到最优拓扑（5 种规范 + 遗留）
  ├─ atomizer.ts             ROMA 任务分解
  │
  ├─ agentRuntime.ts         LLM → 工具 → 校验 → 重试
  │   ├─ providers/          25 家 LLM，带故障转移链
  │   ├─ toolResultCache.ts  按租户的 SHA-256 缓存
  │   ├─ stateCheckpointer.ts 崩溃安全快照（SQLite WAL）
  │   ├─ circuitBreaker.ts   失败阈值 → 熔断打开
  │   ├─ deadLetterQueue.ts  死信队列（可回放）
  │   ├─ compensationRegistry.ts 写操作回滚
  │   ├─ verificationLoop.ts 质量门（5 阶段）
  │   └─ eventSourcingEngine.ts WAL + 哈希链事件日志
  │
  ├─ enterpriseSecurityGateway.ts  七层纵深防御
  ├─ messageBus.ts           发布/订阅
  ├─ metricsCollector.ts     统一指标（Prometheus）
  ├─ threeLayerMemory.ts     工作 / 情景 / 长期记忆
  ├─ metaLearner.ts          Thompson Sampling + Reflexion
  └─ pluginManager.ts        Hook 与沙箱插件
```

## 包结构

```
packages/core/src/
├── runtime/             ← 执行引擎
├── ultimate/            ← 编排
├── security/            ← 安全网关
├── tools/               ← 18 个内置工具
├── sandbox/             ← 安全配置
├── atr/                 ← 代理任务恢复
├── selfEvolution/       ← 元学习
├── saga/                ← 分布式补偿
├── mcp/                 ← Model Context Protocol
└── plugins/builtin/     ← 如 RAG
```

## 设计原则

1. **拓扑优先** — 先分析任务结构再执行  
2. **提供商无关** — 25 家统一接口 + 自动回退  
3. **崩溃安全** — 每步原子 checkpoint（SQLite WAL）  
4. **默认可观测** — 指标、链路、SSE  
5. **天生多租户** — 存储、记忆、限流、缓存隔离  
6. **默认安全** — 七层网关、DLP、能力令牌  
7. **可逆** — 事件溯源、补偿、DLQ、启动恢复  

## 相关

- [核心调用链](/zh/architecture/core-call-chain)  
- [多代理](/zh/architecture/multi-agent)  
- [代理运行时](/zh/architecture/agent-runtime)  
- [生产就绪](/zh/architecture/production-readiness)  
