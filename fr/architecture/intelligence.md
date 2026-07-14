# Couche Intelligence

La couche Intelligence regroupe des **systèmes automatiques** qui rendent Commander plus malin avec le temps. L’utilisateur voit le résultat, pas le mécanisme.

## Composants

| Composant | Rôle | Ce que voit l’utilisateur |
|-----------|------|---------------------------|
| **Cost Predictor** | Coût avant exécution | « ~$0.09, continuer ? » |
| **Failure Pattern Learner** | Apprend des échecs | « Vous avez déjà vu ce problème » |
| **Impact Analyzer** | Effets de bord | « 3 fichiers impactés » |
| **Skill Extractor** | Patterns réutilisables | « Solution enregistrée » |

## Cost Predictor

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
```

Décomposition typique : Deliberation · Execution · Synthesis · Quality Gates.

## Failure Pattern Learner

```typescript
import { getFailurePatternLearner } from '@commander/core';

const learner = getFailurePatternLearner();
const warnings = learner.checkPatterns({
  task: 'deploy to production',
  context: 'after database migration',
});
```

## Impact · Skill

Estiment le blast radius et extraient des skills réutilisables pour la délibération suivante.

## Ops

```bash
export COMMANDER_MODE=plan
npx tsx packages/core/src/cliEntry.ts plan "refactor the auth module"
```

## Voir aussi

- [Self-evolution](/fr/architecture/self-evolution)  
- [Token budget allocator](/fr/api/token-budget-allocator)  
- [Reflection engine](/fr/api/reflection-engine)  
