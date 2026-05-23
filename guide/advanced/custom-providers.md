# Custom Providers

Connect Commander to any LLM provider by implementing the `LLMProvider` interface.

## Provider Interface

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

## Example: Custom Provider

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

## Registering a Provider

```typescript
import { CommanderRuntime } from '@commander/core';

const runtime = new CommanderRuntime();
runtime.registerProvider('my-provider', new MyCustomProvider());
```

## Provider Fallback Chain

Commander supports automatic fallback between providers:

```typescript
runtime.setFallbackChain('my-provider', ['openai', 'anthropic']);
```

If the primary provider fails (rate limited, timeout, down), Commander automatically:
1. Detects the failure
2. Logs the error with full context
3. Falls back to the next provider in the chain
4. Retries with appropriate backoff

## Provider Selection Strategy

Commander selects providers based on:

| Factor | Behavior |
|--------|----------|
| Task complexity | Harder tasks → stronger models |
| Cost constraints | Simple tasks → cheaper providers |
| Latency requirements | Time-sensitive → fast inference (Groq, Together) |
| Availability | Fallback chain if primary unavailable |
| Historical accuracy | MetaLearner tracks success rates |
