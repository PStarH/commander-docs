# Resiliencia

Documentación en español de **Resiliencia**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

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

| State | Behavior |
|-------|----------|
| **CLOSED** | Normal operation. Requests pass through. |
| **OPEN** | After 5 consecutive failures. All requests are rejected immediately. Cooldown: 30 seconds. |
| **HALF-OPEN** | After cooldown. One test request is allowed. Success → CLOSED, failure → OPEN again. |


| Category | Description |
|----------|-------------|
| `llm` | LLM call failures |
| `tool` | Tool execution failures |
| `execution` | Agent execution failures |
| `verification` | Quality gate failures |
| `circuit_breaker` | Circuit breaker trips |
| `compensation` | Compensation failures |
| `semantic_drift` | Semantic degradation detected |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
