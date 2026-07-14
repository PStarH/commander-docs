# Security Sandbox

**Security Sandbox.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Profile | Shell Access | File Write | Network | Best For |
|---------|-------------|-----------|---------|----------|
| **READ_ONLY** (strict) | None | Read-only | Blocked | Code review, untrusted input |
| **WORKSPACE_WRITE** (standard) | Allowed (sandboxed) | Project files | Allowed | Development |
| **FULL_ACCESS** (permissive) | Full | Any | Allowed | CI/CD, automation |
| **HARDENED** | None | Denied | Blocked | Untrusted code execution |


## Contenu principal

### Architecture

En pratique, **Architecture** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/sandbox) pour le détail exhaustif.

### Security Profiles

En pratique, **Security Profiles** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/sandbox) pour le détail exhaustif.

### Execution Policies

En pratique, **Execution Policies** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/sandbox) pour le détail exhaustif.

### Petri Net Scheduler

En pratique, **Petri Net Scheduler** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/sandbox) pour le détail exhaustif.

### Trusted Execution Environment (TEE)

En pratique, **Trusted Execution Environment (TEE)** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/sandbox) pour le détail exhaustif.

### seccomp-BPF (Linux)

En pratique, **seccomp-BPF (Linux)** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/sandbox) pour le détail exhaustif.

### Approval Workflow

En pratique, **Approval Workflow** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/sandbox) pour le détail exhaustif.

### Platform Support

En pratique, **Platform Support** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/sandbox) pour le détail exhaustif.

### Utilisation

En pratique, **Usage** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/sandbox) pour le détail exhaustif.

## Exemples (code inchangé)

```
sandbox/
├── execPolicy.ts           ← Execution policy definitions
├── approval.ts             ← Approval workflow for sensitive operations
├── profiles.ts             ← Security profiles (READ_ONLY, WORKSPACE_WRITE, FULL_ACCESS, HARDENED)
├── platforms.ts            ← Platform-specific sandbox configurations
├── manager.ts              ← Sandbox lifecycle management
├── executionRouter.ts      ← Route executions to appropriate backends
├── lane.ts                 ← Execution lane management
├── seccompBpf.ts           ← seccomp-BPF system call filtering (Linux)
├── teeEnclave.ts           ← Trusted Execution Environment sandbox
├── petriNetScheduler.ts    ← Petri net resource allocation
├── networkProxy.ts         ← Network proxy sandbox
├── backends/               ← Sandbox backend implementations
│   ├── localBackend.ts     ← Local execution
│   ├── sshBackend.ts       ← Remote SSH execution
│   └── dockerExecBackend.ts ← Docker container execution
└── types.ts                ← Shared types
```

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

```typescript
import { ApprovalManager } from '@commander/core';

const approval = new ApprovalManager();

// Operations that trigger approval:
// - File deletion
// - External network requests
// - Shell commands with sudo
// - Modifying git configuration
```

## Opérations

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## Voir aussi

- [Vue d’architecture](/fr/architecture/overview)
- [Prêt production](/fr/architecture/production-readiness)
- [Sécurité](/fr/guide/security)
- [Démarrage rapide](/fr/guide/getting-started)
