# Capa de inteligencia

Documentación en español de **Capa de inteligencia**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```typescript
import { getCostPredictor } from '@commander/core';

const predictor = getCostPredictor();

const estimate = await predictor.estimate({
  task: 'refactor the auth module',
  topology: 'ORCHESTRATOR',
  effortLevel: 'COMPLEX',
  agentCount: 4,
});

console.log(`Estimated cost: $${estimate.estimatedCostUsd}`);
console.log(`Estimated duration: ${estimate.estimatedDurationMs}ms`);
console.log(`Confidence: ${estimate.confidence}`);
```

```
┌─────────────────────────────────┐
│         Total Estimate          │
├─────────────────────────────────┤
│  Deliberation:  $0.002         │
│  Execution:     $0.06          │
│  Synthesis:     $0.02          │
│  Quality Gates: $0.008         │
├─────────────────────────────────┤
│  Total:         $0.09          │
└─────────────────────────────────┘
```

```typescript
import { getFailurePatternLearner } from '@commander/core';

const learner = getFailurePatternLearner();

// Check for warnings before executing
const warnings = learner.checkPatterns({
  task: 'deploy to production',
  context: 'after database migration',
});

for (const warning of warnings) {
  console.log(`[${warning.severity}] ${warning.suggestion}`);
  // "You've deployed without running migrations 3 times before"
}
```

| Component | Purpose | User sees |
|-----------|---------|-----------|
| **Cost Predictor** | Estimates task cost before execution | "Estimated $0.09, continue?" |
| **Failure Pattern Learner** | Learns from past failures | "You've hit this issue before" |
| **Impact Analyzer** | Predicts change side effects | "Changing this affects 3 files" |
| **Skill Extractor** | Extracts reusable patterns from successes | "Solution saved for reuse" |


| Category | Examples |
|----------|---------|
| `deploy` | Deploy without migration, missing env vars |
| `test` | Skipping tests, flaky test ignored |
| `config` | Wrong config format, missing required field |
| `dependency` | Breaking change in upgrade, missing peer dep |
| `security` | Hardcoded secret, exposed endpoint |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
