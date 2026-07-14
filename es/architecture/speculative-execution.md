# Ejecución especulativa

Documentación en español de **Ejecución especulativa**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  LLM Call   │────▶│ Pattern Tracker  │────▶│ Speculative     │
│  (thinking) │     │ (predict next)   │     │ Executor        │
└─────────────┘     └──────────────────┘     └────────┬────────┘
                                                       │
                         ┌─────────────────────────────┘
                         ▼
               ┌──────────────────┐
               │  Pre-executed    │
               │  Tool Results    │
               │  (cached)        │
               └──────────────────┘
```

```typescript
import { PatternTracker } from '@commander/core';

const tracker = new PatternTracker();

// Record observed tool sequences
tracker.recordSequence(['file.read', 'code.search', 'file.read']);

// Predict next tool given partial sequence
const predictions = tracker.predictNext(['file.read']);
// → [{ toolName: 'code.search', confidence: 0.8 }]
```

```typescript
import { SpeculativeExecutor, PatternTracker } from '@commander/core';

const tracker = new PatternTracker();
const executor = new SpeculativeExecutor({ tracker });

// During LLM thinking time
const predictions = tracker.predictNext(currentToolSequence);

// Pre-execute predicted tools (read-only only)
const preExecuted = await executor.speculate(predictions);

// When the model actually calls a tool, check if we already have the result
const cached = executor.getCachedResult('file.read', { path: 'src/index.ts' });
if (cached) {
  // Use cached result — zero wait
  return cached;
} else {
  // Execute normally
  return await executeTool('file.read', { path: 'src/index.ts' });
}
```

| Setting | Default | Description |
|---------|---------|-------------|
| `maxPatternLength` | `4` | Max n-gram length |
| `maxTrackedPatterns` | `50` | Max patterns in memory |
| `minConfidence` | `0.1` | Minimum confidence to predict |
| `staleThresholdMs` | `300000` | Prune patterns older than 5 min |


| Scenario | Speedup | Why |
|----------|---------|-----|
| Multi-file analysis | High | `file.read` → `code.search` → `file.read` patterns are predictable |
| Code review | Medium | `git.diff` → `file.read` → `code.search` sequences recur |
| Debugging | Low-Medium | Tool sequences are less predictable |
| Simple queries | None | Single tool call, no patterns to exploit |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
