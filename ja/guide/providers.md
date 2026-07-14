# プロバイダー

**25** の LLM プロバイダー。環境変数を 1 つ設定すれば自動検出します。

主要キー: `OPENAI_API_KEY` · `ANTHROPIC_API_KEY` · `GOOGLE_API_KEY` · `DEEPSEEK_API_KEY` · `GROQ_API_KEY` · `OPENROUTER_API_KEY` · `XAI_API_KEY` · `OLLAMA_BASE_URL` · `VLLM_BASE_URL` · ほか monorepo `providerRegistry.ts` の 25 登録。

```bash
export OPENAI_API_KEY=sk-...
```

`modelRouter.ts` が複雑度・コスト・レイテンシ・フォールバックに基づき選択します。

## カスタム

```typescript
import { BaseLLMProvider } from '@commander/core';
class MyProvider extends BaseLLMProvider {
  async call(messages, options) { /* ... */ }
}
runtime.registerProvider('my-provider', new MyProvider());
```
