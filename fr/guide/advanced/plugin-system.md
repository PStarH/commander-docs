# Système de plugins

**19 points de hook** pour observer, modifier ou bloquer l’exécution.

## Hooks principaux

| Hook | Quand |
|------|-------|
| `beforeLLMCall` / `afterLLMCall` | Chaque requête LLM |
| `beforeToolCall` / `afterToolCall` | Chaque tool |
| `onAgentStart` / `onAgentComplete` | Cycle de vie agent |
| `beforeVerification` / `afterVerification` | Portes de qualité |
| `beforeRun` / `afterRun` | Run global |
| `onError` / `onRetry` | Erreurs / retries |
| `onStreamEvent` | SSE |
| `onHandoff` | Handoff inter-agents |

## Créer un plugin

```typescript
import { CommanderPlugin, getHookManager } from '@commander/core';

class LoggingPlugin implements CommanderPlugin {
  name = 'logging';
  hooks = {
    beforeLLMCall: async (params) => {
      console.log(`[LLM] ${params.provider}`);
      return params; // throw pour bloquer
    },
    afterToolCall: async (result) => {
      console.log(`[Tool] ${result.tool} ${result.durationMs}ms`);
      return result;
    },
  };
}

getHookManager().register(new LoggingPlugin());
```

## Sécurité

Les plugins tiers reçoivent un **contexte sandboxed** : leurs permissions ne dépassent jamais le système principal.

```bash
npx tsx packages/core/src/cliEntry.ts plugin enable rag
npx tsx packages/core/src/cliEntry.ts plugin disable rag
```

## Lié

- [Points d’extension](/fr/architecture/extension-points)  
- [RAG](/fr/guide/advanced/rag-knowledge-base)  
- [SDK](/fr/guide/sdk)
