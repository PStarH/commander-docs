# Backpressure

Documentación en español de **Backpressure**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

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

| Stage | Purpose | Pattern |
|-------|---------|---------|
| **Token Bucket** | Rate-limits admission (tokens per second) | Leaky bucket |
| **Ring Buffer** | Absorbs burst traffic (fixed-size, O(1) insert/evict) | LMAX Disruptor |
| **Circuit Breaker** | Protects consumer when overwhelmed | Hystrix 3-state |


| Metric | Description |
|--------|-------------|
| `backpressure_tokens_available` | Current tokens in bucket |
| `backpressure_ring_buffer_occupancy` | Ring buffer fill ratio |
| `backpressure_circuit_breaker_state` | `CLOSED`, `OPEN`, or `HALF_OPEN` |
| `backpressure_requests_admitted_total` | Total admitted requests |
| `backpressure_requests_rejected_total` | Total rejected requests |
| `backpressure_requests_spilled_total` | Total spilled from ring buffer |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
