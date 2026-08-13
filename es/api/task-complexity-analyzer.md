# Analizador de complejidad de tareas

Documentación en español de **Analizador de complejidad de tareas**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```typescript
type ComplexityLevel = 'trivial' | 'simple' | 'moderate' | 'complex' | 'extreme';

type OrchestrationMode =
  | 'SEQUENTIAL'  // Low complexity, single thread
  | 'PARALLEL'    // Independent subtasks
  | 'HANDOFF'     // Needs expert
  | 'MAGENTIC'    // Open exploration
  | 'CONSENSUS';  // High-risk decision

interface ComplexityScore {
  level: ComplexityLevel;
  score: number;              // 0-100
  factors: ComplexityFactors;
  recommendedMode: OrchestrationMode;
  tokenBudget: TokenBudget;
  confidence: number;         // 0-1
}

interface ComplexityFactors {
  treewidth: number;          // Dependency complexity (0-100)
  dependencyDepth: number;    // How deep dependencies go (0-100)
  inputSize: number;          // Token count of input
  outputComplexity: number;   // Expected output structure (0-100)
  domainKnowledge: number;    // Need for specialized knowledge (0-100)
  riskLevel: number;          // Failure impact (0-100)
  uncertaintyLevel: number;   // Ambiguity in requirements (0-100)
  timeConstraints: number;    // Deadline pressure (0-100)
}

interface TokenBudget {
  leadAgent: number;          // Percentage for lead agent
  specialistAgents: number;   // Percentage for specialists
  evaluation: number;         // Percentage for evaluation
  overhead: number;           // Percentage for orchestration
  total: number;              // Total budget
}

interface Task {
  id: string;
  description: string;
  input?: string;
  context?: string;
  constraints?: string[];
  deadline?: Date;
  riskLevel?: 'low' | 'medium' | 'high' | 'critical';
}
```

## API

```typescript
import { TaskComplexityAnalyzer } from '@commander/core';
// BatchComplexityAnalyzer se define en packages/core/src/taskComplexityAnalyzer.ts
// y no se re-exporta desde la raíz de '@commander/core'.
import { BatchComplexityAnalyzer } from 'packages/core/src/taskComplexityAnalyzer';

// Analiza una tarea
const analyzer = new TaskComplexityAnalyzer();
const score = analyzer.analyze(task); // → ComplexityScore

// Análisis por lotes
const batchAnalyzer = new BatchComplexityAnalyzer();
const scores = batchAnalyzer.analyzeBatch(tasks); // → ComplexityScore[]

// Recomendación de orquestación
const orch = batchAnalyzer.getBatchOrchestration(scores);
// → { mode: OrchestrationMode; totalBudget: number; parallelGroups: number }
```

Pesos de los factores (suma ponderada → score 0-100): treewidth 0.2 · dependencyDepth 0.15 · inputSize 0.1 · outputComplexity 0.15 · domainKnowledge 0.15 · riskLevel 0.1 · uncertaintyLevel 0.1 · timeConstraints 0.05.

Umbrales `scoreToLevel`: `< 15` trivial · `< 30` simple · `< 50` moderate · `< 75` complex · resto extreme.

## Reglas de selección de modo

Los factores de alta prioridad ganan sobre el default por nivel (se evalúan en orden):

| Condición | Modo de orquestación |
|-----------|----------------------|
| `riskLevel >= 75` | CONSENSUS |
| `uncertaintyLevel >= 60` | MAGENTIC |
| `domainKnowledge >= 70` | HANDOFF |
| Nivel `trivial` / `simple` | SEQUENTIAL |
| Nivel `moderate` + `treewidth < 30` | PARALLEL |
| Nivel `moderate` (resto) | SEQUENTIAL |
| Nivel `complex` + `dependencyDepth > 50` | HANDOFF |
| Nivel `complex` (resto) | PARALLEL |
| Nivel `extreme` | MAGENTIC |

## Presupuestos de tokens

Total base por nivel de complejidad:

| Nivel | Total base |
|-------|-----------|
| trivial | 1000 |
| simple | 3000 |
| moderate | 10000 |
| complex | 30000 |
| extreme | 100000 |

Multiplicador y reparto por modo (lead / specialists / evaluation / overhead):

| Modo | Multiplicador | Reparto |
|------|---------------|---------|
| SEQUENTIAL | ×1 | 70 / 10 / 15 / 5 |
| PARALLEL | ×1.5 | 30 / 50 / 15 / 5 |
| HANDOFF | ×1.3 | 35 / 45 / 15 / 5 |
| MAGENTIC | ×2 | 40 / 35 / 15 / 10 |
| CONSENSUS | ×1.5 | 30 / 30 / 35 / 5 |

La confianza parte de 1.0 y pierde 0.05 por factor en rango medio (30-70), con mínimo 0.5.

## Orquestación por lotes

`getBatchOrchestration(scores)`:

- Alguna tarea recomienda `CONSENSUS` → todo el lote corre `CONSENSUS`, `parallelGroups: 1`
- Todas trivial/simple → `PARALLEL`, total ×0.8 (eficiencia paralela), `parallelGroups: scores.length`
- Resto → modo de la tarea con mayor score, `parallelGroups: scores.length` si `PARALLEL`, si no `1`

## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests
- Firmas API exactas: monorepo / [API overview](/es/api/overview)

## Relacionado

- [Arquitectura](/es/architecture/overview)
- [Inicio rápido](/es/guide/getting-started)