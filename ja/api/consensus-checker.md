# Consensus Checker

高リスク判断のために複数 LLM の **重み付き投票** で合意を見ます。

## 型

```typescript
type ConsensusLevel = 'unanimous' | 'strong' | 'moderate' | 'low' | 'diverged';

interface ConsensusConfig {
  minVoters: number;
  agreementThreshold: number;
  strongAgreementThreshold: number;
  lowConsensusThreshold: number;
  timeoutMs: number;
  enableDiscussion: boolean;
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

## API

```typescript
const checker = new ConsensusChecker(config?: Partial<ConsensusConfig>);
const checkId = checker.createCheck(question: string, context?: string): string;
// addVote / finalize …
```

## いつ使うか

- セキュリティ・コンプライアンス・デプロイなどの高リスク  
- REVIEW トポロジとの multi-model 交差検証  
- Layer 2 拡張 — 通常は `CommanderClient.run` で十分  

パッケージ: monorepo `@commander/core`。

## 関連

- [API 概要](/ja/api/overview)  
- [検証](/ja/architecture/verification)  
- [マルチエージェント](/ja/architecture/multi-agent)  
