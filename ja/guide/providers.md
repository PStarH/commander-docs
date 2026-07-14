# プロバイダー

Commander は **25 の LLM プロバイダー** をサポートします。環境変数を 1 つ設定すれば自動検出します。

| 変数                                 | プロバイダー                                        |
| ------------------------------------ | --------------------------------------------------- |
| `OPENAI_API_KEY`                     | OpenAI / DeepSeek / GLM / MiMo（fallback チェーン） |
| `AZURE_OPENAI_API_KEY`               | Azure OpenAI                                        |
| `ANTHROPIC_API_KEY`                  | Anthropic Claude                                    |
| `GOOGLE_API_KEY`                     | Google Gemini                                       |
| `DEEPSEEK_API_KEY`                   | DeepSeek（専用）                                    |
| `ZHIPU_API_KEY`                      | GLM（Zhipu AI）                                     |
| `MIMO_API_KEY`                       | MiMo（専用）                                        |
| `XIAOMI_API_KEY`                     | Xiaomi MiMo                                         |
| `GROQ_API_KEY`                       | Groq（低遅延）                                      |
| `TOGETHER_API_KEY`                   | Together AI                                         |
| `PERPLEXITY_API_KEY`                 | Perplexity                                          |
| `FIREWORKS_API_KEY`                  | Fireworks AI                                        |
| `REPLICATE_API_TOKEN`                | Replicate                                           |
| `MISTRAL_API_KEY`                    | Mistral AI                                          |
| `CO_API_KEY`                         | Cohere                                              |
| `OPENROUTER_API_KEY`                 | OpenRouter（200+ モデル）                           |
| `OLLAMA_BASE_URL` / `OLLAMA_API_KEY` | Ollama（ローカル）                                  |
| `VLLM_BASE_URL` / `VLLM_API_KEY`     | vLLM（ローカル）                                    |
| `AWS_ACCESS_KEY_ID`                  | AWS Bedrock                                         |
| `XAI_API_KEY`                        | xAI（Grok）                                         |
| `ANYSCALE_API_KEY`                   | Anyscale                                            |
| `DEEPINFRA_API_KEY`                  | DeepInfra                                           |
| `AGNES_API_KEY`                      | Agnes                                               |
| `STEPFUN_API_KEY`                    | StepFun                                             |
| `MINIMAX_API_KEY`                    | MiniMax                                             |

## 選択ロジック

`modelRouter.ts` が次を見て最適プロバイダーを選びます。

- **タスク複雑度** — 難しい → 強いモデル
- **コスト** — 単純 → 安価なプロバイダー
- **レイテンシ** — 時間敏感 → Groq、Together など
- **Fallback チェーン** — primary 失敗時に自動切替

```bash
# いちばん単純な設定 — キー 1 つで自動選択
export OPENAI_API_KEY=sk-...
```

## カスタムプロバイダー

`LLMProvider` を実装して登録します。

```typescript
import { BaseLLMProvider } from "@commander/core";

class MyProvider extends BaseLLMProvider {
  async call(messages, options) {
    // Your implementation
  }
}

runtime.registerProvider("my-provider", new MyProvider());
```

> パッケージは monorepo の `packages/core` から。npm 公開が主経路になるまでは workspace を使ってください。

## 関連

- [クイックスタート](/ja/guide/getting-started)
- [設定](/ja/guide/configuration)
- [カスタムプロバイダー](/ja/guide/advanced/custom-providers)
