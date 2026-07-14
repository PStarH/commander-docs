# Referencia de API

Commander tiene **dos capas** de superficie API. La mayoría de apps solo necesitan la capa 1.

## Capa 1 — Integración pública (empieza aquí)

| Superficie | Paquete / entrada | Ideal para |
|------------|-------------------|------------|
| **CLI** | `commander` · `packages/core/src/cliEntry.ts` | Terminal, scripts, CI |
| **SDK TypeScript** | `@commander/sdk` → `CommanderClient` | Embed en apps Node |
| **API HTTP** | Servidor `:4000` | Clientes políglotas, consola web |
| **SDK Python** | `commander-ai` (cliente HTTP) | Python contra el API server |

### SDK TypeScript

```typescript
import { CommanderClient, createClient } from '@commander/sdk';

const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const result = await client.run('audit this repo');
console.log(result.status, result.summary);
await client.disconnect();

const c = await createClient();
await c.run('explain the architecture');
await c.disconnect();
```

| Método | Rol |
|--------|-----|
| `connect` / `disconnect` | Ciclo de vida |
| `run(task)` | Ejecución completa → `ExecutionResult` |
| `plan(task)` | Solo deliberación |
| `onEvent(handler)` | Stream de eventos agent/tool |
| `createAgent` / helpers de memoria | Control avanzado de sesión |

> **Estado npm:** monorepo-first; publicación pública en curso. Ver [Agent SDK](/es/guide/sdk).

### HTTP (servidor)

```bash
curl http://localhost:4000/health
curl http://localhost:4000/metrics

curl -X POST http://localhost:4000/execute \
  -H "Authorization: Bearer $COMMANDER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"task":"analyze this repository","mode":"plan"}'
```

API durable Architecture V2: `POST /v1/runs` — ver [Migración V2](/es/guide/migration-v2).

### Python

```python
from commander import CommanderClient
# cliente httpx fino → API server
```

[Python SDK](/es/guide/sdk-python).

---

## Capa 2 — Componentes de orquestación runtime

Estos módulos impulsan deliberación, presupuesto, memoria y verificación dentro de `@commander/core`. Úsalos al **extender** el runtime — no para integración normal de producto.

| Componente | Propósito |
|------------|-----------|
| [Analizador de complejidad](/es/api/task-complexity-analyzer) | Puntuar tarea → recomendar topología |
| [Orquestador adaptativo](/es/api/adaptive-orchestrator) | Plan multi-agente + coordinación |
| [Presupuesto de tokens](/es/api/token-budget-allocator) | Reparto de presupuesto entre agentes |
| [Memoria de 3 capas](/es/api/three-layer-memory) | Working · episodic · long-term |
| [Motor de reflexión](/es/api/reflection-engine) | Evaluación post-run |
| [Consenso](/es/api/consensus-checker) | Votos multi-modelo en alto riesgo |
| [Inspector](/es/api/inspector-agent) | Salud / detección de issues |

### Cuándo usar la capa 2

- Construir topología o planner custom  
- Investigar memoria y consenso  
- Tests que aíslan un subsistema  

### Cuándo **no** usar la capa 2

- Features de producto que solo necesitan «corre esta tarea» → `CommanderClient`  
- Clientes remotos multi-lenguaje → HTTP  

### Ejemplo mínimo capa 2

```typescript
import {
  TaskComplexityAnalyzer,
  AdaptiveOrchestrator,
  TokenBudgetAllocator,
} from '@commander/core';

const analyzer = new TaskComplexityAnalyzer();
const complexity = analyzer.analyze({
  id: 'task-1',
  description: 'Build distributed logging system',
  riskLevel: 'high',
});

const allocator = new TokenBudgetAllocator({ baseBudget: 100_000 });
const budget = allocator.allocate(
  complexity.recommendedTopology,
  complexity.score,
  3,
);
```

### Accesores globales

Algunos componentes exponen singletons de proceso (usados por runtime/SDK):

- `getGlobalTaskComplexityAnalyzer()`
- `getGlobalAdaptiveOrchestrator()`
- `getGlobalTokenBudgetAllocator()`
- `getGlobalThreeLayerMemory()`
- `getGlobalReflectionEngine()`
- `getGlobalConsensusChecker()`
- `getGlobalInspectorAgent()`

Prefiere `CommanderClient` salvo que necesites estado compartido a nivel proceso.

---

## Profundidad de arquitectura

Diseño de subsistemas (no listas de métodos): [Arquitectura](/es/architecture/overview), [Runtime](/es/architecture/agent-runtime), [Verificación](/es/architecture/verification), [Seguridad](/es/guide/security).

## Guías relacionadas

- [Comandos CLI](/es/guide/commands)  
- [Consola web](/es/guide/web-console)  
- [Cookbook](/es/guide/cookbook/)  
