# Custom Providers

**Custom Providers.** このページは Commander アーキテクチャの構成要素を説明します。monorepo に沿った日本語の運用ドキュメントで、コードブロックは英語のままです。

製品メトリクス: **25** プロバイダー · **5** トポロジ · **18** tools · **6700+** テスト。

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · ビルド後: `commander`

## 参照表

| Factor | Behavior |
|--------|----------|
| Task complexity | Harder tasks → stronger models |
| Cost constraints | Simple tasks → cheaper providers |
| Latency requirements | Time-sensitive → fast inference (Groq, Together) |
| Availability | Fallback chain if primary unavailable |
| Historical accuracy | MetaLearner tracks success rates |


## 主な内容

### Provider Interface

運用では **Provider Interface** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/advanced/custom-providers)を参照してください。

### Example: Custom Provider

運用では **Example: Custom Provider** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/advanced/custom-providers)を参照してください。

### Registering a Provider

運用では **Registering a Provider** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/advanced/custom-providers)を参照してください。

### Provider Fallback Chain

運用では **Provider Fallback Chain** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/advanced/custom-providers)を参照してください。

### Provider Selection Strategy

運用では **Provider Selection Strategy** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/guide/advanced/custom-providers)を参照してください。

## 例（コードは英語のまま）

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

## 運用

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 関連

- [アーキテクチャ概要](/ja/architecture/overview)
- [本番準備](/ja/architecture/production-readiness)
- [セキュリティ](/ja/guide/security)
- [クイックスタート](/ja/guide/getting-started)
