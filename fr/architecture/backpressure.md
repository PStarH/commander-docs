# Backpressure Controller

Le contrôleur de backpressure assure le **contrôle d’admission unifié** du runtime Commander : il évite la saturation quand la demande dépasse la capacité, via Token Bucket → Ring Buffer → Circuit Breaker.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Stage | Purpose | Pattern |
|-------|---------|---------|
| **Token Bucket** | Rate-limits admission (tokens per second) | Leaky bucket |
| **Ring Buffer** | Absorbs burst traffic (fixed-size, O(1) insert/evict) | LMAX Disruptor |
| **Circuit Breaker** | Protects consumer when overwhelmed | Hystrix 3-state |


## Contenu principal

### Architecture

En pratique, **Architecture** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/backpressure) pour le détail exhaustif.

### Fonctionnement

En pratique, **How It Works** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/backpressure) pour le détail exhaustif.

### Configuration

En pratique, **Configuration** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/backpressure) pour le détail exhaustif.

### Utilisation

En pratique, **Usage** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/backpressure) pour le détail exhaustif.

### Lock-Free Design

En pratique, **Lock-Free Design** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/backpressure) pour le détail exhaustif.

### Métriques

En pratique, **Metrics** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/backpressure) pour le détail exhaustif.

### When to Tune

En pratique, **When to Tune** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/backpressure) pour le détail exhaustif.

## Exemples (code inchangé)

```
Producer → [Token Bucket] → [Ring Buffer] → [Circuit Breaker] → Consumer
              rate-limit       absorb bursts     protect when overwhelmed
```

```typescript
import { BackpressureController } from '@commander/core';

const controller = new BackpressureController({
  tokenBucket: {
    maxTokens: 100,
    refillRatePerSecond: 50,
  },
  ringBuffer: {
    capacity: 200,
  },
  circuitBreaker: {
    failureThreshold: 0.5,    // 50% failure rate opens breaker
    recoveryTimeoutMs: 30000, // Wait 30s before half-open
    halfOpenMaxRequests: 10,  // Probe requests in half-open
  },
});
```

```typescript
// Check if a request should be admitted
const admission = controller.tryAdmit();

if (admission.allowed) {
  // Process the request
  const result = await processRequest(request);
  controller.recordSuccess();
} else {
  // Request rejected — return 429 or queue
  return { status: 429, reason: admission.reason };
}
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
