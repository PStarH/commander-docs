# Consensus Checker

**Consensus Checker.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Level | Threshold | Action |
|-------|-----------|--------|
| Unanimous | ≥95% | Proceed |
| Strong | ≥80% | Proceed |
| Moderate | ≥50% | Discuss |
| Low | >0 | Rethink |
| Diverged | 0 | Escalate |


## 主な節

### Types

**Types** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### API

**API** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Consensus Thresholds

**Consensus Thresholds** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```typescript
type ConsensusLevel = 'unanimous' | 'strong' | 'moderate' | 'low' | 'diverged';

interface ConsensusConfig {
  minVoters: number;                    // Default: 3
  agreementThreshold: number;           // Default: 0.8
  strongAgreementThreshold: number;     // Default: 0.95
  lowConsensusThreshold: number;        // Default: 0.5
  timeoutMs: number;                    // Default: 30000
  enableDiscussion: boolean;            // Default: true
}

interface ConsensusResult {
  decision: string;
  consensusLevel: ConsensusLevel;
  consensusScore: number;
  confidence: 'high' | 'medium' | 'low';
  requiresAction: boolean;
  actionType?: 'proceed' | 'discuss' | 'rethink' | 'escalate';
}
```
```typescript
const checker = new ConsensusChecker(config?: Partial<ConsensusConfig>);

// Create a consensus check
const checkId = checker.createCheck(question: string, context?: string): string;

// Add a vote from a model
checker.addVote(
  checkId: string,
  modelId: string,
  modelName: string,
  decision: string,
  confidence: number,
  reasoning: string
): boolean;

// Get the consensus result
const result = checker.getResult(checkId: string): ConsensusResult | undefined;

// Wait for all votes
await checker.waitForVotes(checkId: string): Promise<ConsensusCheck | null>;
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
