# Self-Evolution

**Self-Evolution.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Metric | Impact |
|--------|--------|
| Topology selection accuracy | +15-20% after 1000 runs |
| Provider availability | Failover optimized for current latency |
| Verification threshold tuning | False positives reduced by 30% |
| Token efficiency | Budget allocation converges to task need |


## Contenu principal

### Architecture

En pratique, **Architecture** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/self-evolution) pour le détail exhaustif.

### MetaLearner

En pratique, **MetaLearner** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/self-evolution) pour le détail exhaustif.

### TrajectoryAnalyzer

En pratique, **TrajectoryAnalyzer** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/self-evolution) pour le détail exhaustif.

### EvolverAgent

En pratique, **EvolverAgent** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/self-evolution) pour le détail exhaustif.

### Reflexion

En pratique, **Reflexion** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/self-evolution) pour le détail exhaustif.

### Outcomes

En pratique, **Outcomes** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/self-evolution) pour le détail exhaustif.

## Exemples (code inchangé)

```
Execution completes
  │
  ├─ TrajectoryAnalyzer       ← Analyze execution patterns
  │   └─ Extract features: duration, tokens, success rate
  │
  ├─ MetaLearner              ← Thompson Sampling
  │   └─ Update Beta distributions per arm
  │
  └─ EvolverAgent             ← Cross-run optimization
      └─ Propose configuration changes
```

```typescript
interface Arm {
  name: string;             // e.g., "topology:DISPATCH"
  alpha: number;            // Success count
  beta: number;             // Failure count
}

class MetaLearner {
  selectArm(arms: Arm[]): Arm {
    // Sample from each arm's Beta distribution
    // Pick the arm with the highest sampled value
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

```typescript
const analyzer = new TrajectoryAnalyzer();
const patterns = analyzer.analyze(trajectory);

// patterns.bottlenecks     → [step names sorted by duration]
// patterns.commonFailures  → [failure modes by frequency]
// patterns.providerRanking → [providers sorted by success rate]
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
