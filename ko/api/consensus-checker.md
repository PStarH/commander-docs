# Consensus Checker

고위험 결정을 위해 여러 LLM 프로바이더의 **가중 투표**로 합의를 봅니다.

## 타입

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

## API

```typescript
const checker = new ConsensusChecker(config?: Partial<ConsensusConfig>);

const checkId = checker.createCheck(question: string, context?: string): string;

checker.addVote(
  checkId: string,
  modelId: string,
  decision: string,
  confidence?: number,
);

const result = await checker.finalize(checkId);
```

## 언제 쓰나

- 보안·규정·배포 같은 **고위험** 판단  
- REVIEW 토폴로지와 함께 multi-model 교차 검증  
- Layer 2 확장 — 일반 앱은 `CommanderClient.run` 으로 충분  

패키지: monorepo `@commander/core`.

## 관련

- [API 개요](/ko/api/overview)  
- [검증](/ko/architecture/verification)  
- [멀티 에이전트](/ko/architecture/multi-agent)  
