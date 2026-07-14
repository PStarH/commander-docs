# Auto-évolution (Self-Evolution)

Commander s’améliore via un **méta-apprentissage** qui ajuste la config agents selon les résultats. Thompson Sampling + Reflexion optimisent topologie, provider et paramètres.

## Architecture

```
Exécution terminée
  → TrajectoryAnalyzer → MetaLearner (Thompson Sampling) → EvolverAgent
```

## MetaLearner

```typescript
interface Arm {
  name: string;   // e.g. "topology:DISPATCH"
  alpha: number;
  beta: number;
}

class MetaLearner {
  selectArm(arms: Arm[]): Arm {
    return arms.reduce((best, arm) => {
      const sample = BetaDistribution.sample(arm.alpha, arm.beta);
      return sample > best.sample ? { ...arm, sample } : best;
    });
  }

  updateArm(arm: Arm, success: boolean): void {
    if (success) arm.alpha++;
    else arm.beta++;
  }
}
```

Chaque variante (topologie, provider, retry) est un bras. Après des milliers d’exécutions, la config converge par type de tâche.

## TrajectoryAnalyzer

Extrait goulots, tokens, modes d’échec pour alimenter le MetaLearner.

## EvolverAgent

Propose des changements cross-run. En prod : modes d’approbation + budgets.

## Point de vue utilisateur

Surtout automatique. Après 5+ expériences, l’auto-optimisation devient plus visible.

```bash
npx tsx packages/core/src/cliEntry.ts status
```

## Voir aussi

- [Intelligence](/fr/architecture/intelligence)  
- [Multi-agent](/fr/architecture/multi-agent)  
- [Reflection engine](/fr/api/reflection-engine)  
