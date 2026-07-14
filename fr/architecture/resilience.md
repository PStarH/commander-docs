# Résilience

Commander dispose d’une **résilience multi-couches** : disponibilité, sûreté des données, récupérabilité.

## Circuit breaker

Trois états par provider :

| État | Comportement |
|------|--------------|
| **CLOSED** | Passage normal |
| **OPEN** | Après 5 échecs. Rejet immédiat. Cooldown 30s |
| **HALF-OPEN** | 1 requête test. Succès → CLOSED, échec → OPEN |

```typescript
const breaker = new CircuitBreaker({ threshold: 5, cooldownMs: 30000 });
breaker.onSuccess();
breaker.onFailure();
breaker.isAvailable();
```

`CircuitBreakerRegistry` centralise les breakers.

## Chaîne de fallback

```typescript
const chain = new ProviderFallbackChain({
  providers: ['openai', 'anthropic', 'deepseek', 'groq'],
  timeoutMs: 30000,
});

const result = await chain.tryProviders(task);
```

`llmRetry.ts` classe retryable vs permanent.

## Checkpoints crash-safe

`StateCheckpointer` (SQLite WAL) après chaque étape, isolation par tenant.

```typescript
const checkpointer = new StateCheckpointer({ basePath: '/data/checkpoints' });
await checkpointer.checkpoint({ runId, phase, stepNumber, messages, tokenUsage });
```

## Dead letter queue

**7 catégories · 15 modes** : `llm`, `tool`, `execution`, `verification`, `circuit_breaker`, `compensation`, `semantic_drift`.

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts doctor --reset
```

## Voir aussi

- [Event sourcing](/fr/architecture/event-sourcing)  
- [Production readiness](/fr/architecture/production-readiness)  
- [Saga](/fr/architecture/saga)  
