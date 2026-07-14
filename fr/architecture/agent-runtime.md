# Agent Runtime

**Agent Runtime.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

## Architecture

```
AgentRuntime.execute(ctx)
  │
  ├─ acquireSlot()        ← sémaphore de concurrence
  ├─ [Tenant check]       ← rate limit + quota de concurrence
  ├─ resolve storage      ← mémoire + cache scopés tenant
  │
  ├─ [Retry loop: 0..maxRetries]
  │   ├─ callWithTimeout()       ← provider LLM
  │   ├─ [Tool execution loop]
  │   │   ├─ planner.plan()      ← plan dépendances
  │   │   ├─ executeTool()       ← StepErrorBoundary → tool.execute()
  │   │   └─ cache.set()
  │   ├─ verification.check()    ← 5 portes qualité
  │   └─ checkpoint()            ← save atomique
  │
  ├─ releaseSlot()
  └─ flush traces + samples
```

## Boucle principale

1. **Acquisition de slot** — ne pas dépasser les runs concurrents
2. **Validation tenant** — rate limits et quotas
3. **Appel LLM** — timeout configurable
4. **Exécution tools** — `ToolPlanner` parallélise les tools indépendants
5. **Vérification** — 5 portes ; échec → retry
6. **Checkpoint** — persistance atomique à chaque étape
7. **Tracing** — flush des traces et échantillons LLM

## Composants clés

| Composant            | Fichier                         | Rôle                           |
| -------------------- | ------------------------------- | ------------------------------ |
| `AgentRuntime`       | `runtime/agentRuntime.ts`       | Boucle principale              |
| `ToolPlanner`        | `runtime/toolPlanner.ts`        | Plan d’exécution tools         |
| `ToolOrchestrator`   | `runtime/toolOrchestrator.ts`   | Exécute le plan                |
| `StepErrorBoundary`  | `runtime/stepErrorBoundary.ts`  | skip / retry / abort par étape |
| `StepTimeoutManager` | `runtime/stepTimeoutManager.ts` | Timeouts d’étape               |
| `ContextCompactor`   | `runtime/contextCompactor.ts`   | Compactage messages            |
| `ContextWindow`      | `runtime/contextWindow.ts`      | Fenêtre glissante              |
| `TokenGovernor`      | `runtime/tokenGovernor.ts`      | Budget tokens                  |
| `CycleDetector`      | `runtime/cycleDetector.ts`      | Boucles infinies               |
| `ToolOutputManager`  | `runtime/toolOutputManager.ts`  | Budget sorties tools           |

## Configuration

```typescript
interface AgentRuntimeConfig {
  maxStepsPerRun: number;
  maxRetries: number;
  timeoutMs: number;
  maxConcurrency: number;
  budgetHardCapTokens: number;
}
```

## Plan d’exécution

Les tools ne suivent pas l’ordre brut de la réponse LLM. Indépendants → parallèle ; dépendants → séquentiel après prérequis ; cycles détectés avant exécution.

## Voir aussi

- [Vérification](/fr/architecture/verification)
- [Multi-agent](/fr/architecture/multi-agent)
- [Chaîne d’appels core](/fr/architecture/core-call-chain)
