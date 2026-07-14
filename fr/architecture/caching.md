# Cache

Commander met en place un **cache multi-niveaux** pour réduire les appels LLM, accélérer les réponses et éviter le travail redondant. Chaque cache est **isolé par tenant**.

## Couches

```
Tool Call
  │
  ├─ SingleFlightRequestCache  ── déduplique les requêtes concurrentes identiques
  │   (la première exécute, les autres attendent le résultat)
  │
  ├─ ToolResultCache           ── cache exact SHA-256
  │   (tools déterministes : lecture fichier, recherche code, etc.)
  │
  └─ SemanticCache             ── cache sémantique par similarité
      (appels LLM non déterministes au sens proche)
```

## ToolResultCache

Clé = SHA-256 de `(tenantId + tool + args)` :

```typescript
const cache = new ToolResultCache({ basePath: '/data/cache' });

const key = cache.hashKey(tenantId, toolName, args);
const cached = await cache.get(key);

if (cached) return cached;

const result = await executeTool(toolName, args);
await cache.set(key, result);
```

- Idéal pour tools déterministes  
- Isolation par tenant → pas de fuite inter-tenant  
- TTL configurable  
- Éviction LRU au-delà du quota  

## SemanticCache

Pour les opérations non déterministes (LLM), similarité d’embeddings :

```typescript
const semanticCache = new SemanticCache({ similarityThreshold: 0.95 });

const similar = await semanticCache.find(input, tenantId);
if (similar) return similar.result;

await semanticCache.store(input, result, tenantId);
```

- Similarité cosinus  
- Seuil haut = moins de faux positifs, moins de hits  
- Éviction TTL + LRU  

## SingleFlightRequestCache

Évite le **thundering herd** (plusieurs exécutions concurrentes de la même clé) :

```typescript
const singleFlight = new SingleFlightRequestCache();

const [a, b, c] = await Promise.all([
  singleFlight.execute('key-1', () => expensiveOperation()),
  singleFlight.execute('key-1', () => expensiveOperation()),
  singleFlight.execute('key-1', () => expensiveOperation()),
]);
// une seule expensiveOperation
```

Utile quand plusieurs agents demandent le même tool/LLM en même temps.

## Intégration

Dans le pipeline d’exécution des tools :

1. **SingleFlight** — dédup in-flight  
2. **ToolResultCache** — match exact  
3. **SemanticCache** — sens similaire  
4. Exécution réelle seulement en cas de miss total  

Packages monorepo (`packages/core`). Install principal : clone + `pnpm install`.

## Voir aussi

- [Multi-tenancy](/fr/architecture/multi-tenancy)  
- [Agent Runtime](/fr/architecture/agent-runtime)  
- [Tools](/fr/architecture/tools)  
