# 快速开始

大约五分钟跑通 Commander。一把 API Key。无需画图、无需 YAML。

## 成功标准

以下三点都满足即算完成：

1. `pnpm install` 无报错  
2. 跑过一次任务，能看到 **审议（deliberation）+ 拓扑（topology）**  
3. 进程正常结束（或 `doctor` 给出明确错误，而不是无声挂起）

## 前置要求

- **Node.js** 18+（推荐 22）  
- **pnpm** 8+（推荐 9+，monorepo workspaces）  
- 任意一家 LLM 的 API Key（OpenAI、Anthropic、DeepSeek、Groq 等）

> 请使用 **pnpm**，不要只用 npm——本项目是多包 monorepo。

## 五分钟清单

### 1. 克隆并安装

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

可选但推荐：

```bash
pnpm -r build
```

### 2. 设置 API Key

```bash
export OPENAI_API_KEY=sk-...
# 或: ANTHROPIC_API_KEY / DEEPSEEK_API_KEY / GROQ_API_KEY / ...
```

Commander 会 **自动识别** 提供商。完整列表见英文文档 [Providers](/guide/providers)。

### 3. 先 plan（零风险）

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
```

应看到复杂度、拓扑、代理分配——**不会改文件**。

### 4. 带 stream 执行

```bash
npx tsx packages/core/src/cliEntry.ts run "explain the architecture of this repository" --stream
```

应看到实时思考、工具调用、质量门。

### 5.（可选）Web 控制台

```bash
pnpm gui
```

- API：`http://localhost:4000`  
- Web：开发态多为 `:5173`，Docker 多为 `:3000`

详见 [Web 控制台](/zh/guide/web-console)。

### 6.（可选）Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000
```

## 构建后使用 `commander` 命令

```bash
pnpm --filter @commander/core build
commander run "audit this repo" --stream
```

## 出问题怎么办

| 现象 | 处理 |
|------|------|
| `Provider not available` | 确认当前 shell 已 `export` Key；运行 `npx tsx packages/core/src/cliEntry.ts doctor` |
| 模块找不到 / workspace 错误 | 在仓库根目录用 **pnpm**，再 `pnpm install` 与 `pnpm -r build` |
| 卡住无输出 | 先 `plan`；设 `COMMANDER_DEBUG=true`；检查网络与提供商状态 |
| 限流 | 等待、降低并发 `COMMANDER_MAX_CONCURRENCY=1`、或加第二把 Key |
| 仅离线 | Ollama：`export OLLAMA_BASE_URL=http://localhost:11434` |

完整排查（英文）：[Troubleshooting](/guide/troubleshooting)。

## 刚刚发生了什么？

1. **分类** 任务（CODING / RESEARCH / ANALYSIS / FACTUAL）  
2. **选择** 拓扑（SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW）  
3. **运行** 一个或多个带工具的代理  
4. **校验** 五层质量门  

## 下一步

| 目标 | 去向 |
|------|------|
| 真实配方 | [实战手册](/zh/guide/cookbook/) |
| 为什么不用别的框架 | [为什么选 Commander](/zh/guide/why-commander) |
| 完整英文文档 | [English docs](/guide/getting-started) |
| 嵌入 TypeScript | [Agent SDK](/guide/sdk) |
