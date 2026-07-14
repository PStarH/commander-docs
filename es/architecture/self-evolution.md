# Auto-evolución

Documentación en español de **Auto-evolución**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

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

| Metric | Impact |
|--------|--------|
| Topology selection accuracy | +15-20% after 1000 runs |
| Provider availability | Failover optimized for current latency |
| Verification threshold tuning | False positives reduced by 30% |
| Token efficiency | Budget allocation converges to task need |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
