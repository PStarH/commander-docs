# Consensus Checker

Multi-model consensus for high-risk decisions, using weighted voting across multiple LLM providers.

## Types

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

## Consensus Thresholds

| Level | Threshold | Action |
|-------|-----------|--------|
| Unanimous | ≥95% | Proceed |
| Strong | ≥80% | Proceed |
| Moderate | ≥50% | Discuss |
| Low | >0 | Rethink |
| Diverged | 0 | Escalate |
