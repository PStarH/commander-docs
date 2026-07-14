# Self-Evolution

**Self-Evolution.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Metric | Impact |
|--------|--------|
| Topology selection accuracy | +15-20% after 1000 runs |
| Provider availability | Failover optimized for current latency |
| Verification threshold tuning | False positives reduced by 30% |
| Token efficiency | Budget allocation converges to task need |


## 主な節

### Architecture

**Architecture** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### MetaLearner

**MetaLearner** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### TrajectoryAnalyzer

**TrajectoryAnalyzer** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### EvolverAgent

**EvolverAgent** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Reflexion

**Reflexion** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Outcomes

**Outcomes** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

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

## 運用チェック

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 関連

- [アーキテクチャ概要](/ja/architecture/overview)
- [本番準備](/ja/architecture/production-readiness)
- [セキュリティ](/ja/guide/security)
- [クイックスタート](/ja/guide/getting-started)
