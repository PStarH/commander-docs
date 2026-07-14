# Smart Model Router

**Smart Model Router.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

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


## Contenu principal

### Capabilities

En pratique, **Capabilities** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/smart-model-router) pour le détail exhaustif.

### Configuration

En pratique, **Configuration** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/smart-model-router) pour le détail exhaustif.

### Routing Modes

En pratique, **Routing Modes** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/smart-model-router) pour le détail exhaustif.

### Model Tiers

En pratique, **Model Tiers** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/smart-model-router) pour le détail exhaustif.

### Routing Decision

En pratique, **Routing Decision** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/smart-model-router) pour le détail exhaustif.

### Programmatic API

En pratique, **Programmatic API** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/smart-model-router) pour le détail exhaustif.

### Integration with Deliberation

En pratique, **Integration with Deliberation** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/smart-model-router) pour le détail exhaustif.

## Exemples (code inchangé)

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
