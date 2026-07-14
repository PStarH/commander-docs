# 常见问题

## 一般

### Commander 是什么？

多代理编排引擎：在 5 种规范拓扑上协调多个 AI 代理，对接 25 家 LLM 提供商与 18 个内置工具。

### 和普通 AI 编程助手有何不同？

助手多为单模型单线程；Commander 做 **多代理、自动拓扑、流式可观测、质量门与生产原语**。

### 开源吗？

是，MIT。

## 安装

### 需要很多 API Key 吗？

不需要。**一把即可**。设置 `OPENAI_API_KEY`（或其它）即可自动识别；配置多把时才走故障转移。

### 能完全离线吗？

可以，用 Ollama / vLLM：

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```

### npm 包发布了吗？

`@commander/core` / `@commander/sdk` 以 monorepo 为主，公开发布进行中。见 [Agent SDK](/guide/sdk)。

## 使用

### 会改我的文件吗？

默认可写，但可用模式控制：`plan` / `read-only` / `suggest` / `auto-edit` / `full-auto`。

### 能在 CI 里跑吗？

可以：

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors"
```

见 [CI 实战](/zh/guide/cookbook/) 与英文 [CI cookbook](/guide/cookbook/ci-full-auto)。

## 企业

### 多租户？

支持。见 [Multi-Tenancy](/architecture/multi-tenancy)。

### 私有化？

支持 Docker / VM。见 [Deployment](/deployment)。

## 隐私

代码默认在你本机或你的服务器处理；仅发送到 **你配置的** LLM 提供商。敏感代码请用本地模型。

## 更多

- [快速开始](/zh/guide/getting-started)  
- [英文 FAQ](/guide/faq)  
- [安全](/guide/security)  
