# Système de plugins

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Système de plugins**.

## Entrée rapide

```typescript
import { CommanderPlugin } from '@commander/core';

class LoggingPlugin implements CommanderPlugin {
  name = 'logging';
  hooks = {
    beforeLLMCall: async (params) => {
      console.log(`[LLM] ${params.provider}`);
      return params; // o throw para bloquear
    },
    afterToolCall: async (result) => {
      console.log(`[Tool] ${result.tool} ${result.durationMs}ms`);
      return result;
    },
    onError: async (error) => {
      console.error(error.message);
    },
  };
}
```

```typescript
import { getHookManager } from '@commander/core';
getHookManager().register(new LoggingPlugin());
```

```bash
npx tsx packages/core/src/cliEntry.ts plugin enable rag
npx tsx packages/core/src/cliEntry.ts plugin disable rag
```

| Hook | Cuándo se dispara |
|------|-------------------|
| `beforeLLMCall` / `afterLLMCall` | Antes/después de cada request LLM |
| `beforeToolCall` / `afterToolCall` | Antes/después de cada tool |
| `onAgentStart` / `onAgentComplete` | Inicio/fin de agente |
| `onSubtaskCreate` / `onSubtaskComplete` | Subtareas |
| `onCheckpoint` | Checkpoint de estado |
| `onError` / `onRetry` | Error no fatal / reintento |
| `beforeVerification` / `afterVerification` | Puertas de calidad |
| `onTokenUsage` | Presupuesto de tokens |
| `onMetricsEmit` | Métricas |
| `beforeRun` / `afterRun` | Inicio/fin del run |
| `onHandoff` | Handoff entre agentes |
| `onStreamEvent` | Evento SSE |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
