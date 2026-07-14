# 自进化

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/architecture/self-evolution)



Commander improves over time through a meta-learning system that tunes agent configurations based on execution outcomes. The system combines Thompson Sampling and Reflexion to optimize topology selection, provider choice, and parameter settings.

## Architecture


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

## MetaLearner


Uses Thompson Sampling with Beta distributions to balance exploration and exploitation:

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

Each configuration variant (topology, provider, retry strategy) is modeled as an arm. Over thousands of executions, the system converges on the optimal configuration for each task type.

## TrajectoryAnalyzer


Analyzes execution traces to extract patterns that inform the meta-learner:

- **Step duration distribution** — Which steps are bottlenecks
- **Token consumption patterns** — Context window utilization
- **Retry and failure patterns** — Which gates fail most often
- **Provider performance** — Latency, error rates per provider

```typescript
const analyzer = new TrajectoryAnalyzer();
const patterns = analyzer.analyze(trajectory);

// patterns.bottlenecks     → [step names sorted by duration]
// patterns.commonFailures  → [failure modes by frequency]
// patterns.providerRanking → [providers sorted by success rate]
```

## EvolverAgent


The `EvolverAgent` bridges analysis to action. It generates configuration recommendations:

- If DISPATCH topology fails 30% more often than CHAIN for RESEARCH tasks, it adjusts the topology router's default mapping
- If a provider consistently times out, it moves that provider later in the fallback chain
- If verification consistently catches hallucination in code tasks, it tightens the hallucination threshold for code outputs

## Reflexion


Commander implements Reflexion — post-execution self-evaluation — as a feedback mechanism:

1. After each run, the system evaluates its own performance
2. Success/failure signals update the meta-learner's Beta distributions
3. Long-term patterns trigger configuration adjustments via the evolver agent

## Outcomes


The self-evolution system produces measurable improvements:

| Metric | Impact |
|--------|--------|
| Topology selection accuracy | +15-20% after 1000 runs |
| Provider availability | Failover optimized for current latency |
| Verification threshold tuning | False positives reduced by 30% |
| Token efficiency | Budget allocation converges to task need |
