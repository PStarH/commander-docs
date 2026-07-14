# Comprobador de consenso

Documentación en español de **Comprobador de consenso**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

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

| Level | Threshold | Action |
|-------|-----------|--------|
| Unanimous | ≥95% | Proceed |
| Strong | ≥80% | Proceed |
| Moderate | ≥50% | Discuss |
| Low | >0 | Rethink |
| Diverged | 0 | Escalate |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
