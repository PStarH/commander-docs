# 自己進化 (Self-Evolution)

Commander は実行結果から設定をチューニングする **メタ学習** で時間とともに改善します。Thompson Sampling と Reflexion でトポロジ・プロバイダー・パラメータを最適化します。

## 構造

```
Execution completes
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

トポロジ・プロバイダー・再試行戦略などが各 arm。数千回の実行でタスク種別に収束します。

## TrajectoryAnalyzer

ボトルネック、トークン消費、失敗モードを抽出して MetaLearner に渡します。

## EvolverAgent

クロスランで設定変更を提案。本番では承認モード・予算ゲートと併用。

## ユーザー視点

多くは自動。5 回以上の経験が溜まると自己最適化が効きやすくなります。

```bash
npx tsx packages/core/src/cliEntry.ts status
```

## 関連

- [インテリジェンス](/ja/architecture/intelligence)  
- [マルチエージェント](/ja/architecture/multi-agent)  
- [Reflection engine](/ja/api/reflection-engine)  
