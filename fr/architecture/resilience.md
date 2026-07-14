# Resilience

**Resilience.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| State | Behavior |
|-------|----------|
| **CLOSED** | Normal operation. Requests pass through. |
| **OPEN** | After 5 consecutive failures. All requests are rejected immediately. Cooldown: 30 seconds. |
| **HALF-OPEN** | After cooldown. One test request is allowed. Success → CLOSED, failure → OPEN again. |


## Contenu principal

### Circuit Breaker

En pratique, **Circuit Breaker** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/resilience) pour le détail exhaustif.

### Provider Fallback Chain

En pratique, **Provider Fallback Chain** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/resilience) pour le détail exhaustif.

### Crash-Safe Checkpoints

En pratique, **Crash-Safe Checkpoints** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/resilience) pour le détail exhaustif.

### Dead Letter Queue

En pratique, **Dead Letter Queue** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/resilience) pour le détail exhaustif.

### Compensation Registry

En pratique, **Compensation Registry** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/resilience) pour le détail exhaustif.

### Event Sourcing Recovery

En pratique, **Event Sourcing Recovery** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/resilience) pour le détail exhaustif.

### Recovery Bootstrapper

En pratique, **Recovery Bootstrapper** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/resilience) pour le détail exhaustif.

### ATR System

En pratique, **ATR System** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/resilience) pour le détail exhaustif.

### SLOs

En pratique, **SLOs** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/resilience) pour le détail exhaustif.

## Exemples (code inchangé)

```typescript
const breaker = new CircuitBreaker({ threshold: 5, cooldownMs: 30000 });
breaker.onSuccess();    // Resets failure count
breaker.onFailure();    // Increments; opens circuit at threshold
breaker.isAvailable();  // false when OPEN
```

```typescript
const chain = new ProviderFallbackChain({
  providers: ['openai', 'anthropic', 'deepseek', 'groq'],
  timeoutMs: 30000,
});

const result = await chain.tryProviders(task);
// Tries OpenAI → Anthropic → DeepSeek → Groq
// Throws FallbackChainExhaustedError if all fail
```

```typescript
const checkpointer = new StateCheckpointer({ basePath: '/data/checkpoints' });
await checkpointer.checkpoint({ runId, phase, stepNumber, messages, tokenUsage });
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
