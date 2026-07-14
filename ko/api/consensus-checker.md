# Consensus Checker

**Consensus Checker.** Commander monorepo 구성 요소에 대한 한국어 운영 문서입니다. 코드·식별자는 영어를 유지하며, CLI는 `npx tsx packages/core/src/cliEntry.ts` 를 우선합니다. 제품 지표: 25 프로바이더 · 5 토폴로지 · 18 tools · 6700+ 테스트.

## 참고 표

| Level | Threshold | Action |
|-------|-----------|--------|
| Unanimous | ≥95% | Proceed |
| Strong | ≥80% | Proceed |
| Moderate | ≥50% | Discuss |
| Low | >0 | Rethink |
| Diverged | 0 | Escalate |


## 주요 섹션

### Types

**Types** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### API

**API** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Consensus Thresholds

**Consensus Thresholds** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

## 예제

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

## 운영 체크

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 관련

- [아키텍처 개요](/ko/architecture/overview)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [보안](/ko/guide/security)
- [빠른 시작](/ko/guide/getting-started)
