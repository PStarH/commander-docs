# Intelligence Layer

**Intelligence Layer.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Component | Purpose | User sees |
|-----------|---------|-----------|
| **Cost Predictor** | Estimates task cost before execution | "Estimated $0.09, continue?" |
| **Failure Pattern Learner** | Learns from past failures | "You've hit this issue before" |
| **Impact Analyzer** | Predicts change side effects | "Changing this affects 3 files" |
| **Skill Extractor** | Extracts reusable patterns from successes | "Solution saved for reuse" |


## 主な節

### Components

**Components** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Cost Predictor

**Cost Predictor** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Failure Pattern Learner

**Failure Pattern Learner** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Impact Analyzer

**Impact Analyzer** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Skill Extractor

**Skill Extractor** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Configuration

**Configuration** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

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
