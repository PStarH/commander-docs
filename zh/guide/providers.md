# 提供商（Providers）

Commander 支持 **25 家 LLM 提供商**。设置任意一个环境变量即可自动识别。

| 变量                                 | 提供商                                   |
| ------------------------------------ | ---------------------------------------- |
| `OPENAI_API_KEY`                     | OpenAI / DeepSeek / GLM / MiMo（回退链） |
| `AZURE_OPENAI_API_KEY`               | Azure OpenAI                             |
| `ANTHROPIC_API_KEY`                  | Anthropic Claude                         |
| `GOOGLE_API_KEY`                     | Google Gemini                            |
| `DEEPSEEK_API_KEY`                   | DeepSeek（专用）                         |
| `ZHIPU_API_KEY`                      | 智谱 GLM                                 |
| `MIMO_API_KEY`                       | MiMo（专用）                             |
| `XIAOMI_API_KEY`                     | 小米 MiMo                                |
| `GROQ_API_KEY`                       | Groq（低延迟）                           |
| `TOGETHER_API_KEY`                   | Together AI                              |
| `PERPLEXITY_API_KEY`                 | Perplexity                               |
| `FIREWORKS_API_KEY`                  | Fireworks AI                             |
| `REPLICATE_API_TOKEN`                | Replicate                                |
| `MISTRAL_API_KEY`                    | Mistral AI                               |
| `CO_API_KEY`                         | Cohere                                   |
| `OPENROUTER_API_KEY`                 | OpenRouter（200+ 模型）                  |
| `OLLAMA_BASE_URL` / `OLLAMA_API_KEY` | Ollama（本地）                           |
| `VLLM_BASE_URL` / `VLLM_API_KEY`     | vLLM（本地）                             |
| `AWS_ACCESS_KEY_ID`                  | AWS Bedrock                              |
| `XAI_API_KEY`                        | xAI（Grok）                              |
| `ANYSCALE_API_KEY`                   | Anyscale                                 |
| `DEEPINFRA_API_KEY`                  | DeepInfra                                |
| `AGNES_API_KEY`                      | Agnes                                    |
| `STEPFUN_API_KEY`                    | StepFun                                  |
| `MINIMAX_API_KEY`                    | MiniMax                                  |

## 如何选择

`modelRouter.ts` 会综合：

- **任务复杂度** — 难任务走更强模型
- **成本** — 简单任务走更便宜提供商
- **延迟** — 时间敏感走 Groq、Together 等
- **回退链** — 主提供商失败自动切换

```bash
# 最简配置：一把 Key 即可自动选择
export OPENAI_API_KEY=sk-...
```

## 自定义提供商

实现 `LLMProvider` 并注册：

```typescript
import { BaseLLMProvider } from "@commander/core";

class MyProvider extends BaseLLMProvider {
  async call(messages, options) {
    // Your implementation
  }
}

runtime.registerProvider("my-provider", new MyProvider());
```

> 包来自 monorepo 的 `packages/core`。在 npm 公开发行为主路径之前，请用 workspace 安装。

## 相关

- [快速开始](/zh/guide/getting-started)
- [配置](/zh/guide/configuration)
- [自定义提供商](/zh/guide/advanced/custom-providers)
