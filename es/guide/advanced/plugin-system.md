# Sistema de plugins

El sistema de plugins de Commander expone **19 puntos de hook** para observar, modificar o bloquear la ejecución en cualquier etapa.

## Puntos de hook

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

## Crear un plugin

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

## Registrar

```typescript
import { getHookManager } from '@commander/core';
getHookManager().register(new LoggingPlugin());
```

## Seguridad de plugins

Los plugins de terceros reciben un **contexto de carga sandboxed**: sus permisos no pueden superar los del sistema principal.

```bash
npx tsx packages/core/src/cliEntry.ts plugin enable rag
npx tsx packages/core/src/cliEntry.ts plugin disable rag
```

## Relacionado

- [Puntos de extensión](/es/architecture/extension-points)  
- [RAG](/es/guide/advanced/rag-knowledge-base)  
- [SDK](/es/guide/sdk)
