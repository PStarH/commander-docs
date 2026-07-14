# Fournisseurs custom

1. Étendre `BaseLLMProvider`  
2. Implémenter `call(messages, options)`  
3. `runtime.registerProvider('my-provider', new MyProvider())`  

```typescript
import { BaseLLMProvider } from '@commander/core';
class MyProvider extends BaseLLMProvider {
  async call(messages, options) {
    return { content: '...', usage: { totalTokens: 0 } };
  }
}
runtime.registerProvider('my-provider', new MyProvider());
```

Documentez env vars, timeouts, tests de contrat. Pas de secrets dans les logs.

[Fournisseurs](/fr/guide/providers) · [Routeur](/fr/architecture/smart-model-router)
