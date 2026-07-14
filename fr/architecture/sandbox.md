# Sandbox de sécurité

Le sandbox Commander isole chaque exécution et alloue les ressources via un ordonnanceur Petri net.

## Architecture

```
sandbox/
├── execPolicy.ts / approval.ts / profiles.ts / platforms.ts
├── manager.ts / executionRouter.ts / lane.ts
├── seccompBpf.ts / teeEnclave.ts / petriNetScheduler.ts
├── networkProxy.ts / backends/ (local, ssh, docker)
└── types.ts
```

## Profils

| Profil | Shell | Écriture | Réseau | Usage |
|--------|-------|----------|--------|-------|
| **READ_ONLY** | Non | Lecture | Bloqué | Revue, entrée non fiable |
| **WORKSPACE_WRITE** | Sandboxé | Projet | OK | Dev |
| **FULL_ACCESS** | Complet | Tout | OK | CI/CD |
| **HARDENED** | Non | Refusé | Bloqué | Code non fiable |

## ExecPolicy

```typescript
interface ExecPolicy {
  allowShell: boolean;
  allowNetwork: boolean;
  allowFileWrite: boolean;
  allowFileDelete: boolean;
  allowedPaths: string[];
  deniedPaths: string[];
  maxExecutionTime: number;
  maxMemory: number;
}
```

## Petri net

| Place | Capacité | Rôle |
|-------|----------|------|
| `pending` | Illimitée | File d’attente |
| `v8_slots` | 10 | Isolates V8 |
| `seccomp_slots` | 4 | seccomp-BPF |
| `wasm_slots` | 2 | WASM |
| `tee_slots` | 1 | TEE |
| `executing` / `completed` | Illimitées | En cours / finis |

Transitions `admit_*` / `complete_*`. Analyse deadlock / saturation avant admission.

## Backends

local · ssh · docker.

## Ops

```bash
export COMMANDER_MODE=read-only
npx tsx packages/core/src/cliEntry.ts plan "audit this repo"
```

Pour du code non fiable : HARDENED + réseau bloqué.

## Voir aussi

- [Sécurité](/fr/guide/security)  
- [Security Gateway](/fr/architecture/security-gateway)  
- [Tools](/fr/architecture/tools)  
