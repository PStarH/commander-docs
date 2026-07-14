# プロバイダー

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/guide/providers)



Commander supports **25 LLM providers**. Set any single environment variable—Commander auto-detects the provider.

| Variable | Provider |
|----------|----------|
| `OPENAI_API_KEY` | OpenAI / DeepSeek / GLM / MiMo (fallback chain) |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI |
| `ANTHROPIC_API_KEY` | Anthropic Claude |
| `GOOGLE_API_KEY` | Google Gemini |
| `DEEPSEEK_API_KEY` | DeepSeek (dedicated) |
| `ZHIPU_API_KEY` | GLM (Zhipu AI) |
| `MIMO_API_KEY` | MiMo (dedicated) |
| `XIAOMI_API_KEY` | Xiaomi MiMo |
| `GROQ_API_KEY` | Groq (fast inference) |
| `TOGETHER_API_KEY` | Together AI |
| `PERPLEXITY_API_KEY` | Perplexity |
| `FIREWORKS_API_KEY` | Fireworks AI |
| `REPLICATE_API_TOKEN` | Replicate |
| `MISTRAL_API_KEY` | Mistral AI |
| `CO_API_KEY` | Cohere |
| `OPENROUTER_API_KEY` | OpenRouter (200+ models) |
| `OLLAMA_BASE_URL` / `OLLAMA_API_KEY` | Ollama (local) |
| `VLLM_BASE_URL` / `VLLM_API_KEY` | vLLM (local) |
| `AWS_ACCESS_KEY_ID` | AWS Bedrock |
| `XAI_API_KEY` | xAI (Grok) |
| `ANYSCALE_API_KEY` | Anyscale |
| `DEEPINFRA_API_KEY` | DeepInfra |
| `AGNES_API_KEY` | Agnes |
| `STEPFUN_API_KEY` | StepFun |
| `MINIMAX_API_KEY` | MiniMax |

## Provider Selection


Commander uses a `modelRouter.ts` to select the optimal provider based on:

- **Task complexity** — harder tasks route to stronger models
- **Cost constraints** — simpler tasks use cheaper providers
- **Latency requirements** — time-sensitive tasks use faster inference (Groq, Together)
- **Fallback chain** — if primary provider fails, Commander automatically falls back

```bash
# The simplest setup—just one key lets Commander auto-select
export OPENAI_API_KEY=sk-...
```

## カスタムプロバイダー


Implement the `LLMProvider` interface and register it:

```typescript
import { BaseLLMProvider } from '@commander/core';

class MyProvider extends BaseLLMProvider {
  async call(messages, options) {
    // Your implementation
  }
}

runtime.registerProvider('my-provider', new MyProvider());
```
