# Agent Runtime

Motor de ejecución central. `AgentRuntime` gestiona el ciclo de vida de un agente: LLM, tools, verificación, checkpoints y reintentos bajo presupuestos de tokens y pasos.

## Flujo

```
AgentRuntime.execute(ctx)
  │
  ├─ acquireSlot() / tenant checks / storage
  ├─ [Retry loop]
  │   ├─ callWithTimeout() → LLM
  │   ├─ ToolPlanner → executeTool → cache
  │   ├─ verification (5 puertas)
  │   └─ checkpoint()
  ├─ releaseSlot()
  └─ flush traces
```

## Bucle principal

1. Semáforo de concurrencia
2. Rate limit y cuota por tenant
3. Llamada LLM con timeout
4. Tools con plan de dependencias (paralelo cuando es posible)
5. Verificación de 5 puertas → reintento si falla
6. Checkpoint atómico por paso
7. Flush de traces y muestras

## Componentes

| Componente          | Archivo                        | Rol                   |
| ------------------- | ------------------------------ | --------------------- |
| `AgentRuntime`      | `runtime/agentRuntime.ts`      | Bucle principal       |
| `ToolPlanner`       | `runtime/toolPlanner.ts`       | Plan de tools         |
| `ToolOrchestrator`  | `runtime/toolOrchestrator.ts`  | Ejecuta el plan       |
| `StepErrorBoundary` | `runtime/stepErrorBoundary.ts` | skip/retry/abort      |
| `TokenGovernor`     | `runtime/tokenGovernor.ts`     | Presupuesto de tokens |
| `CycleDetector`     | `runtime/cycleDetector.ts`     | Bucles infinitos      |

## Config

```typescript
interface AgentRuntimeConfig {
  maxStepsPerRun: number;
  maxRetries: number;
  timeoutMs: number;
  maxConcurrency: number;
  budgetHardCapTokens: number;
}
```

## Relacionado

- [Verificación](/es/architecture/verification)
- [Multi-agente](/es/architecture/multi-agent)
- [Cadena de llamadas](/es/architecture/core-call-chain)
