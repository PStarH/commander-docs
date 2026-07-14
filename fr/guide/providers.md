# Fournisseurs

Commander prend en charge **25 fournisseurs LLM**. Une seule variable d’environnement suffit pour l’auto-détection.

| Variable | Fournisseur |
|----------|-------------|
| `OPENAI_API_KEY` | OpenAI / DeepSeek / GLM / MiMo |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI |
| `ANTHROPIC_API_KEY` | Anthropic Claude |
| `GOOGLE_API_KEY` | Google Gemini |
| `DEEPSEEK_API_KEY` | DeepSeek |
| `ZHIPU_API_KEY` | GLM (Zhipu) |
| `MIMO_API_KEY` / `XIAOMI_API_KEY` | MiMo / Xiaomi |
| `GROQ_API_KEY` | Groq |
| `TOGETHER_API_KEY` | Together |
| `PERPLEXITY_API_KEY` | Perplexity |
| `FIREWORKS_API_KEY` | Fireworks |
| `REPLICATE_API_TOKEN` | Replicate |
| `MISTRAL_API_KEY` | Mistral |
| `CO_API_KEY` | Cohere |
| `OPENROUTER_API_KEY` | OpenRouter |
| `OLLAMA_BASE_URL` / `OLLAMA_API_KEY` | Ollama (local) |
| `VLLM_BASE_URL` / `VLLM_API_KEY` | vLLM (local) |
| `AWS_ACCESS_KEY_ID` | AWS Bedrock |
| `XAI_API_KEY` | xAI (Grok) |
| `ANYSCALE_API_KEY` | Anyscale |
| `DEEPINFRA_API_KEY` | DeepInfra |
| `AGNES_API_KEY` | Agnes |
| `STEPFUN_API_KEY` | StepFun |
| `MINIMAX_API_KEY` | MiniMax |

## Sélection

`modelRouter.ts` choisit selon complexité, coût, latence et chaîne de fallback.

```bash
export OPENAI_API_KEY=sk-...
```

## Custom

```typescript
import { BaseLLMProvider } from '@commander/core';
class MyProvider extends BaseLLMProvider {
  async call(messages, options) { /* ... */ }
}
runtime.registerProvider('my-provider', new MyProvider());
```

Liste exacte : monorepo `providerRegistry.ts` (25 registrations).
