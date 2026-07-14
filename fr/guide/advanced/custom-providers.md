# Fournisseurs custom

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Fournisseurs custom**.

## Entrée rapide

```typescript
import { BaseLLMProvider } from '@commander/core';

class MyProvider extends BaseLLMProvider {
  async call(messages, options) {
    // HTTP a tu endpoint OpenAI-compatible o custom
    return { content: '...', usage: { totalTokens: 0 } };
  }
}

runtime.registerProvider('my-provider', new MyProvider());
```



## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
