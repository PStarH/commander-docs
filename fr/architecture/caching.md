# Caching

**Caching.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Contenu principal

### Cache Layers

En pratique, **Cache Layers** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/caching) pour le détail exhaustif.

### ToolResultCache

En pratique, **ToolResultCache** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/caching) pour le détail exhaustif.

### SemanticCache

En pratique, **SemanticCache** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/caching) pour le détail exhaustif.

### SingleFlightRequestCache

En pratique, **SingleFlightRequestCache** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/caching) pour le détail exhaustif.

### Integration

En pratique, **Integration** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/caching) pour le détail exhaustif.

## Exemples (code inchangé)

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
