# Intelligence Layer

**Intelligence Layer.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Component | Purpose | User sees |
|-----------|---------|-----------|
| **Cost Predictor** | Estimates task cost before execution | "Estimated $0.09, continue?" |
| **Failure Pattern Learner** | Learns from past failures | "You've hit this issue before" |
| **Impact Analyzer** | Predicts change side effects | "Changing this affects 3 files" |
| **Skill Extractor** | Extracts reusable patterns from successes | "Solution saved for reuse" |


## Contenu principal

### Components

En pratique, **Components** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/intelligence) pour le détail exhaustif.

### Cost Predictor

En pratique, **Cost Predictor** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/intelligence) pour le détail exhaustif.

### Failure Pattern Learner

En pratique, **Failure Pattern Learner** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/intelligence) pour le détail exhaustif.

### Impact Analyzer

En pratique, **Impact Analyzer** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/intelligence) pour le détail exhaustif.

### Skill Extractor

En pratique, **Skill Extractor** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/intelligence) pour le détail exhaustif.

### Configuration

En pratique, **Configuration** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/intelligence) pour le détail exhaustif.

## Exemples (code inchangé)

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
