# 프로바이더

Commander는 **25개 LLM 프로바이더**를 지원합니다. 환경 변수 하나만 설정하면 자동 감지합니다.

| 변수                                 | 프로바이더                                     |
| ------------------------------------ | ---------------------------------------------- |
| `OPENAI_API_KEY`                     | OpenAI / DeepSeek / GLM / MiMo (fallback 체인) |
| `AZURE_OPENAI_API_KEY`               | Azure OpenAI                                   |
| `ANTHROPIC_API_KEY`                  | Anthropic Claude                               |
| `GOOGLE_API_KEY`                     | Google Gemini                                  |
| `DEEPSEEK_API_KEY`                   | DeepSeek (전용)                                |
| `ZHIPU_API_KEY`                      | GLM (Zhipu AI)                                 |
| `MIMO_API_KEY`                       | MiMo (전용)                                    |
| `XIAOMI_API_KEY`                     | Xiaomi MiMo                                    |
| `GROQ_API_KEY`                       | Groq (저지연)                                  |
| `TOGETHER_API_KEY`                   | Together AI                                    |
| `PERPLEXITY_API_KEY`                 | Perplexity                                     |
| `FIREWORKS_API_KEY`                  | Fireworks AI                                   |
| `REPLICATE_API_TOKEN`                | Replicate                                      |
| `MISTRAL_API_KEY`                    | Mistral AI                                     |
| `CO_API_KEY`                         | Cohere                                         |
| `OPENROUTER_API_KEY`                 | OpenRouter (200+ 모델)                         |
| `OLLAMA_BASE_URL` / `OLLAMA_API_KEY` | Ollama (로컬)                                  |
| `VLLM_BASE_URL` / `VLLM_API_KEY`     | vLLM (로컬)                                    |
| `AWS_ACCESS_KEY_ID`                  | AWS Bedrock                                    |
| `XAI_API_KEY`                        | xAI (Grok)                                     |
| `ANYSCALE_API_KEY`                   | Anyscale                                       |
| `DEEPINFRA_API_KEY`                  | DeepInfra                                      |
| `AGNES_API_KEY`                      | Agnes                                          |
| `STEPFUN_API_KEY`                    | StepFun                                        |
| `MINIMAX_API_KEY`                    | MiniMax                                        |

## 선택 방식

`modelRouter.ts`가 다음을 보고 최적 프로바이더를 고릅니다.

- **작업 복잡도** — 어려운 작업 → 강한 모델
- **비용** — 단순 작업 → 저렴한 프로바이더
- **지연** — 시간 민감 → Groq, Together 등
- **Fallback 체인** — primary 실패 시 자동 전환

```bash
# 가장 단순한 설정 — 키 하나면 자동 선택
export OPENAI_API_KEY=sk-...
```

## 커스텀 프로바이더

`LLMProvider` 인터페이스를 구현하고 등록합니다.

```typescript
import { BaseLLMProvider } from "@commander/core";

class MyProvider extends BaseLLMProvider {
  async call(messages, options) {
    // Your implementation
  }
}

runtime.registerProvider("my-provider", new MyProvider());
```

> 패키지는 monorepo의 `packages/core`에서 가져옵니다. npm 공개가 주 경로가 되기 전까지 workspace 설치를 쓰세요.

## 관련

- [빠른 시작](/ko/guide/getting-started)
- [설정](/ko/guide/configuration)
- [커스텀 프로바이더](/ko/guide/advanced/custom-providers)
