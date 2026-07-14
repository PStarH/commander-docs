# 자기 진화 (Self-Evolution)

Commander는 실행 결과로 에이전트 설정을 튜닝하는 **메타러닝**으로 시간이 갈수록 나아집니다. Thompson Sampling과 Reflexion을 결합해 토폴로지·프로바이더·파라미터를 최적화합니다.

## 구조

```
Execution completes
  │
  ├─ TrajectoryAnalyzer   ← 실행 패턴 분석 (duration, tokens, success)
  ├─ MetaLearner          ← Thompson Sampling (Beta arms)
  └─ EvolverAgent         ← 크로스 런 설정 제안
```

## MetaLearner

탐색·활용 균형을 위해 Beta 분포 기반 Thompson Sampling을 씁니다.

```typescript
interface Arm {
  name: string;   // e.g. "topology:DISPATCH"
  alpha: number;  // 성공
  beta: number;   // 실패
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

토폴로지·프로바이더·재시도 전략 등이 각각 “팔(arm)”입니다. 수천 회 실행 후 작업 유형별 최적 설정으로 수렴합니다.

## TrajectoryAnalyzer

실행 트레이스에서 병목 스텝, 토큰 소비, 실패 모드를 추출해 MetaLearner에 피처를 제공합니다.

## EvolverAgent

크로스 런으로 설정 변경을 제안합니다. 보통 자동 적용되며, 프로덕션에서는 승인 모드·예산 게이트와 함께 씁니다.

## 사용자 관점

대부분 자동입니다. 5회 이상 경험이 쌓이면 자기 최적화가 더 잘 드러납니다(제품 카피의 “5+ experiences”와 정합).

```bash
npx tsx packages/core/src/cliEntry.ts status   # MetaLearner 통계 등
```

## 관련

- [인텔리전스](/ko/architecture/intelligence)  
- [멀티 에이전트](/ko/architecture/multi-agent)  
- [Reflection engine](/ko/api/reflection-engine)  
