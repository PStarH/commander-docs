# Caché

Documentación en español de **Caché**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```
Tool Call
  │
  ├─ SingleFlightRequestCache  ── Deduplicates concurrent identical requests
  │   (First request executes, subsequent wait for result)
  │
  ├─ ToolResultCache           ── SHA-256 exact-match cache
  │   (Deterministic tools: read file, search code, etc.)
  │
  └─ SemanticCache             ── Similarity-based semantic cache
      (Non-deterministic LLM calls with similar meaning)
```

```typescript
const cache = new ToolResultCache({ basePath: '/data/cache' });

const key = cache.hashKey(tenantId, toolName, args);
const cached = await cache.get(key);

if (cached) return cached;

const result = await executeTool(toolName, args);
await cache.set(key, result);
```

```typescript
const semanticCache = new SemanticCache({ similarityThreshold: 0.95 });

// Before LLM call
const similar = await semanticCache.find(input, tenantId);
if (similar) return similar.result;

// After LLM call
await semanticCache.store(input, result, tenantId);
```



## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
