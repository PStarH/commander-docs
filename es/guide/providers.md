# Proveedores

Commander soporta **25 proveedores LLM**. Una sola variable de entorno basta: auto-detección.

| Variable | Proveedor |
|----------|-----------|
| `OPENAI_API_KEY` | OpenAI / DeepSeek / GLM / MiMo |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI |
| `ANTHROPIC_API_KEY` | Anthropic Claude |
| `GOOGLE_API_KEY` | Google Gemini |
| `DEEPSEEK_API_KEY` | DeepSeek |
| `ZHIPU_API_KEY` | GLM (Zhipu) |
| `MIMO_API_KEY` | MiMo |
| `XIAOMI_API_KEY` | Xiaomi MiMo |
| `GROQ_API_KEY` | Groq |
| `TOGETHER_API_KEY` | Together AI |
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

## Selección

`modelRouter.ts` elige según complejidad, coste, latencia y cadena de fallback.

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
