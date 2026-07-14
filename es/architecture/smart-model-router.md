# Router inteligente de modelos

Documentación en español de **Router inteligente de modelos**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```typescript
import { SmartModelRouter } from '@commander/core';

const router = new SmartModelRouter({
  mode: 'cascade',  // auto | manual | cascade
  modelPool: [
    {
      id: 'gpt-4o',
      provider: 'openai',
      capabilities: ['code', 'reasoning', 'function_calling', 'streaming'],
      costPer1MInput: 2.5,
      costPer1MOutput: 10,
      contextWindow: 128000,
      tier: 'power',
    },
    {
      id: 'claude-sonnet-4-20250514',
      provider: 'anthropic',
      capabilities: ['code', 'reasoning', 'long_context', 'function_calling'],
      costPer1MInput: 3,
      costPer1MOutput: 15,
      contextWindow: 200000,
      tier: 'power',
    },
    {
      id: 'deepseek-chat',
      provider: 'deepseek',
      capabilities: ['code', 'reasoning', 'low_cost'],
      costPer1MInput: 0.14,
      costPer1MOutput: 0.28,
      contextWindow: 64000,
      tier: 'eco',
    },
  ],
  routingRules: [
    {
      taskType: 'code_review',
      requiredCapabilities: ['code', 'reasoning'],
      preferredTier: 'power',
      maxCostPer1K: 0.05,
    },
    {
      taskType: 'simple_query',
      requiredCapabilities: ['reasoning'],
      preferredTier: 'eco',
      maxCostPer1K: 0.001,
    },
  ],
  budget: {
    maxCostPerTask: 1.0,
    dailyBudget: 10.0,
  },
});
```

```
Task → Analyze requirements → Match capabilities → Filter by budget
                                                         │
                    ┌────────────────────────────────────┘
                    ▼
            Select model by tier preference
                    │
                    ┌────────────────────────────────────┐
                    ▼                                    ▼
            Primary model                          Fallback chain
            (best match)                           (next tier)
```

```typescript
// Get routing decision for a task
const decision = router.route({
  taskType: 'code_generation',
  requiredCapabilities: ['code', 'function_calling'],
  estimatedTokens: 5000,
});

console.log(`Selected: ${decision.modelId}`);
console.log(`Tier: ${decision.tier}`);
console.log(`Estimated cost: $${decision.estimatedCost}`);

// List available models for a capability set
const models = router.listModels({
  capabilities: ['code', 'reasoning'],
  tier: 'power',
});

// Check budget status
const budget = router.getBudgetStatus();
console.log(`Daily spend: $${budget.spent} / $${budget.limit}`);
```

| Capability | Description |
|------------|-------------|
| `code` | Code generation and understanding |
| `reasoning` | Logical reasoning and chain-of-thought |
| `analysis` | Data analysis and interpretation |
| `creative` | Creative writing and brainstorming |
| `math` | Mathematical computation |
| `multimodal` | Multiple input modalities |
| `vision` | Image understanding |
| `image_generation` | Image creation |
| `long_context` | Large context window support |
| `low_cost` | Cost-efficient inference |
| `fast` | Low-latency inference |
| `high_quality` | Highest quality output |
| `function_calling` | Tool use support |
| `json_mode` | Structured JSON output |
| `streaming` | Streaming response support |
| `translation` | Multi-language translation |
| `summarization` | Text summarization |
| `extraction` | Information extraction |


| Mode | Behavior |
|------|----------|
| `auto` | Router selects best model based on task requirements and budget |
| `manual` | Use only the `defaultModel` — no automatic selection |
| `cascade` | Try models in tier order (eco → standard → power), failover on error |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
