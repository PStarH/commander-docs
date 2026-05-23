# Token Budget Allocator

Allocates and tracks token budgets across agents and execution phases.

## Types

```typescript
interface TokenBudget {
  total: number;
  leadAgent: number;
  specialistAgents: number;
  evaluation: number;
  overhead: number;
  reserved: number;
}

interface BudgetConfig {
  baseBudget: number;
  maxBudget: number;
  efficiencyTarget: number;
  reserveRatio: number;
  warnThreshold: number;   // Default: 0.8
  cutoffThreshold: number; // Default: 0.95
}
```

## API

```typescript
const allocator = new TokenBudgetAllocator(config?: Partial<BudgetConfig>);

// Initialize budget
allocator.initialize(totalBudget: number): void;

// Allocate budget based on mode and complexity
const budget = allocator.allocate(
  mode: OrchestrationMode,
  complexity: number,
  agentCount: number
): TokenBudget;

// Record usage
allocator.recordUsage(agentId: string, tokens: number, phase?: string): void;

// Check thresholds
allocator.isWarningThreshold(): boolean;  // ≥80%
allocator.isCutoffThreshold(): boolean;    // ≥95%

// Get efficiency analysis
allocator.getEfficiencyAnalysis(): {
  overall: number;
  byPhase: Record<string, number>;
  trend: 'improving' | 'declining' | 'stable';
  recommendations: string[];
};
```

## Allocation by Mode

| Mode | Lead | Specialists | Evaluation | Overhead |
|------|------|-------------|------------|----------|
| SEQUENTIAL | 70% | 10% | 15% | 5% |
| PARALLEL | 25% | 55% | 15% | 5% |
| HANDOFF | 35% | 45% | 15% | 5% |
| MAGENTIC | 30% | 40% | 15% | 15% |
| CONSENSUS | 25% | 30% | 40% | 5% |
