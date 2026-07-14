# Custom Providers

**Custom Providers.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Factor | Behavior |
|--------|----------|
| Task complexity | Harder tasks → stronger models |
| Cost constraints | Simple tasks → cheaper providers |
| Latency requirements | Time-sensitive → fast inference (Groq, Together) |
| Availability | Fallback chain if primary unavailable |
| Historical accuracy | MetaLearner tracks success rates |


## Contenu principal

### Provider Interface

En pratique, **Provider Interface** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/custom-providers) pour le détail exhaustif.

### Example: Custom Provider

En pratique, **Example: Custom Provider** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/custom-providers) pour le détail exhaustif.

### Registering a Provider

En pratique, **Registering a Provider** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/custom-providers) pour le détail exhaustif.

### Provider Fallback Chain

En pratique, **Provider Fallback Chain** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/custom-providers) pour le détail exhaustif.

### Provider Selection Strategy

En pratique, **Provider Selection Strategy** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/custom-providers) pour le détail exhaustif.

## Exemples (code inchangé)

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

## Opérations

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## Voir aussi

- [Vue d’architecture](/fr/architecture/overview)
- [Prêt production](/fr/architecture/production-readiness)
- [Sécurité](/fr/guide/security)
- [Démarrage rapide](/fr/guide/getting-started)
