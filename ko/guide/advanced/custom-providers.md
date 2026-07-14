# Custom Providers

**Custom Providers.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 참고 표

| Factor | Behavior |
|--------|----------|
| Task complexity | Harder tasks → stronger models |
| Cost constraints | Simple tasks → cheaper providers |
| Latency requirements | Time-sensitive → fast inference (Groq, Together) |
| Availability | Fallback chain if primary unavailable |
| Historical accuracy | MetaLearner tracks success rates |


## 주요 내용

### Provider Interface

운영 시 **Provider Interface** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/advanced/custom-providers)를 보세요.

### Example: Custom Provider

운영 시 **Example: Custom Provider** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/advanced/custom-providers)를 보세요.

### Registering a Provider

운영 시 **Registering a Provider** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/advanced/custom-providers)를 보세요.

### Provider Fallback Chain

운영 시 **Provider Fallback Chain** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/advanced/custom-providers)를 보세요.

### Provider Selection Strategy

운영 시 **Provider Selection Strategy** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/advanced/custom-providers)를 보세요.

## 예제 (코드는 영어 유지)

```typescript
interface LLMProvider {
  readonly name: string;
  readonly model: string;

  call(
    messages: Message[],
    options: CallOptions
  ): Promise<LLMResponse>;

  isAvailable(): boolean;
}
```

```typescript
import { BaseLLMProvider, Message, CallOptions, LLMResponse } from '@commander/core';

class MyCustomProvider extends BaseLLMProvider {
  readonly name = 'my-provider';
  readonly model = 'my-model-v1';

  async call(messages: Message[], options: CallOptions): Promise<LLMResponse> {
    const response = await fetch('https://api.my-provider.com/v1/chat', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.MY_PROVIDER_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        messages,
        max_tokens: options.maxTokens,
        temperature: options.temperature ?? 0.7,
      }),
    });

    const data = await response.json();

    return {
      content: data.choices[0].message.content,
      usage: {
        promptTokens: data.usage.prompt_tokens,
        completionTokens: data.usage.completion_tokens,
        totalTokens: data.usage.total_tokens,
      },
      model: this.model,
    };
  }

  isAvailable(): boolean {
    return !!process.env.MY_PROVIDER_KEY;
  }
}
```

```typescript
import { CommanderRuntime } from '@commander/core';

const runtime = new CommanderRuntime();
runtime.registerProvider('my-provider', new MyCustomProvider());
```

## 운영

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 관련

- [아키텍처 개요](/ko/architecture/overview)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [보안](/ko/guide/security)
- [빠른 시작](/ko/guide/getting-started)
