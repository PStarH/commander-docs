# Backpressure Controller

The backpressure controller implements **unified admission control** for the Commander runtime, preventing overload when demand exceeds capacity. It uses a three-stage pipeline: Token Bucket → Ring Buffer → Circuit Breaker.

## Architecture

```
Producer → [Token Bucket] → [Ring Buffer] → [Circuit Breaker] → Consumer
              rate-limit       absorb bursts     protect when overwhelmed
```

| Stage | Purpose | Pattern |
|-------|---------|---------|
| **Token Bucket** | Rate-limits admission (tokens per second) | Leaky bucket |
| **Ring Buffer** | Absorbs burst traffic (fixed-size, O(1) insert/evict) | LMAX Disruptor |
| **Circuit Breaker** | Protects consumer when overwhelmed | Hystrix 3-state |

## How It Works

1. **Token Bucket** — Requests consume a token. When the bucket is empty, requests spill to the ring buffer.
2. **Ring Buffer** — Fixed-size buffer absorbs bursts. When full, oldest entry is evicted (counted as spilled).
3. **Circuit Breaker** — When spill rate exceeds threshold, the breaker opens and requests are dropped until half-open.

## Configuration

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

## Usage

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

## Lock-Free Design

The controller uses lock-free CAS (Compare-And-Swap) via atomic counter operations. Concurrent reads never block writes, satisfying constraint NFR-PERF-05.

## Metrics

| Metric | Description |
|--------|-------------|
| `backpressure_tokens_available` | Current tokens in bucket |
| `backpressure_ring_buffer_occupancy` | Ring buffer fill ratio |
| `backpressure_circuit_breaker_state` | `CLOSED`, `OPEN`, or `HALF_OPEN` |
| `backpressure_requests_admitted_total` | Total admitted requests |
| `backpressure_requests_rejected_total` | Total rejected requests |
| `backpressure_requests_spilled_total` | Total spilled from ring buffer |

## When to Tune

| Symptom | Adjustment |
|---------|------------|
| Too many 429 errors | Increase `maxTokens` or `refillRatePerSecond` |
| Memory pressure | Decrease ring buffer `capacity` |
| Cascading failures | Lower `failureThreshold` to open breaker earlier |
| Slow recovery | Increase `recoveryTimeoutMs` |
