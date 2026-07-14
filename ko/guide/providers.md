# 프로바이더

**25**개 LLM 프로바이더. 환경 변수 하나만 설정하면 자동 감지합니다.

주요 키: `OPENAI_API_KEY` · `ANTHROPIC_API_KEY` · `GOOGLE_API_KEY` · `GROQ_API_KEY` · `OPENROUTER_API_KEY` · `XAI_API_KEY` · `OLLAMA_BASE_URL` · `VLLM_BASE_URL` 등 (`providerRegistry.ts` 25개).

```bash
export OPENAI_API_KEY=sk-...
```

`modelRouter.ts`가 복잡도·비용·지연·폴백으로 선택합니다.

## 커스텀

```typescript
import { BaseLLMProvider } from '@commander/core';
class MyProvider extends BaseLLMProvider {
  async call(messages, options) { /* ... */ }
}
runtime.registerProvider('my-provider', new MyProvider());
```
