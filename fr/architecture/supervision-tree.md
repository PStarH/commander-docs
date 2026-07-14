# Arbre de supervision

Commander implémente un **arbre de supervision style Erlang/OTP** pour isoler les pannes. Plutôt que de catcher chaque erreur dans l’agent, on laisse crasher et le superviseur redémarre — « Let It Crash ».

## Pourquoi

- **Isolation** — un crash d’agent ne tue pas le système  
- **Récupération auto** — sans intervention humaine  
- **Escalade** — si un enfant boucle en crash, le parent est notifié  
- **Arrêt propre** — enfants arrêtés en ordre inverse de démarrage  

## Architecture

```
Root Supervisor (one_for_one)
   ├── Agent 1
   ├── Agent 2
   └── Agent N
```

## Stratégies de restart

| Stratégie | Comportement | Quand |
|-----------|--------------|-------|
| `one_for_one` | Redémarre seulement l’enfant crashé | Indépendants |
| `one_for_all` | Redémarre tous | Co-dépendants |
| `rest_for_one` | Crashé + enfants démarrés après | Ordre de démarrage |

## Configuration

```typescript
import { Supervisor } from '@commander/core';

const supervisor = new Supervisor({
  id: 'agent-pool',
  strategy: 'one_for_one',
  maxRestarts: 10,
  maxRestartIntervalMs: 60000,
  defaultShutdownMs: 5000,
  publishEvents: true,
});
```

## Enfants

```typescript
const handle = await supervisor.startChild({
  id: 'agent-1',
  start: async () => {
    const runtime = await createAgentRuntime({ /* config */ });
    return runtime;
  },
});
```

Au-delà de `maxRestarts`, escalade ou arrêt du pool. Événements optionnels sur MessageBus.

## Voir aussi

- [Agent Runtime](/fr/architecture/agent-runtime)  
- [Resilience](/fr/architecture/resilience)  
- [Multi-agent](/fr/architecture/multi-agent)  
