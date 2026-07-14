# Funciones avanzadas

Documentación en español de **Funciones avanzadas**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```typescript
import { SpeculativeExecutor } from '@commander/core';

const executor = new SpeculativeExecutor();

// Run 3 speculative paths in parallel
const results = await executor.executeSpeculative(task, {
  strategies: [
    { provider: 'deepseek', temperature: 0.3 },
    { provider: 'openai', temperature: 0.5 },
    { provider: 'anthropic', temperature: 0.7 },
  ],
  selector: 'quality', // Pick the highest quality result
});
```

```typescript
import { EntropyGater } from '@commander/core';

const gater = new EntropyGater({ threshold: 0.7 });

// Filter unreliable outputs
const filtered = gater.filter(agentOutputs);
// Only returns outputs with confidence > 0.7
```

```typescript
import { CycleDetector } from '@commander/core';

const detector = new CycleDetector();

if (detector.hasCycle(taskGraph)) {
  const broken = detector.breakCycles(taskGraph);
  // Reorders tasks to eliminate circular dependencies
}
```



## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
