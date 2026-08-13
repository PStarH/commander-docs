# キャッシュ

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/architecture/caching)



Commander implements a multi-level caching layer to reduce LLM calls, improve response times, and prevent redundant computation. Each cache is per-tenant isolated.

## Cache Layers


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

## ToolResultCache


An exact-match cache keyed by SHA-256 hash of `(tenantId + tool + args)`:

```typescript
const cache = new ToolResultCache({ basePath: '/data/cache' });

const key = cache.hashKey(tenantId, toolName, args);
const cached = await cache.get(key);

if (cached) return cached;

const result = await executeTool(toolName, args);
await cache.set(key, result);
```

- Perfect for deterministic tools: file reads, code search, grep operations
- Per-tenant key isolation prevents cross-tenant data leaks
- Cache entries have configurable TTLs
- LRU eviction when storage exceeds quota

## SemanticCache


For non-deterministic operations (LLM calls), Commander uses embedding-based similarity:

```typescript
const semanticCache = new SemanticCache({ similarityThreshold: 0.95 });

// Before LLM call
const similar = await semanticCache.find(input, tenantId);
if (similar) return similar.result;

// After LLM call
await semanticCache.store(input, result, tenantId);
```

- Embedding vectors are compared using cosine similarity
- Configurable threshold: higher = fewer false positives, lower = more cache hits
- Eviction policy: TTL + LRU combination

## SingleFlightRequestCache


Prevents duplicate concurrent execution of identical requests (the "thundering herd" problem):

```typescript
const singleFlight = new SingleFlightRequestCache();

// Three concurrent calls with the same key:
const [a, b, c] = await Promise.all([
  singleFlight.execute('key-1', () => expensiveOperation()),
  singleFlight.execute('key-1', () => expensiveOperation()),
  singleFlight.execute('key-1', () => expensiveOperation()),
]);

// Only ONE expensiveOperation runs, all three get the same result
```

This is particularly valuable when multiple agents or runs start simultaneously and request the same tool execution or LLM call.

## Integration


The caches are layered in the tool execution pipeline:

1. **SingleFlight** deduplicates in-flight requests
2. **ToolResultCache** serves cached exact-match results
3. **SemanticCache** serves cached similar-meaning results
4. Only after all caches miss does the actual LLM call or tool execution proceed
