# Sandbox de seguridad

Documentación en español de **Sandbox de seguridad**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

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

| Profile | Shell Access | File Write | Network | Best For |
|---------|-------------|-----------|---------|----------|
| **READ_ONLY** (strict) | None | Read-only | Blocked | Code review, untrusted input |
| **WORKSPACE_WRITE** (standard) | Allowed (sandboxed) | Project files | Allowed | Development |
| **FULL_ACCESS** (permissive) | Full | Any | Allowed | CI/CD, automation |
| **HARDENED** | None | Denied | Blocked | Untrusted code execution |


| Place | Capacity | Purpose |
|-------|----------|---------|
| `pending` | Unbounded | Requests waiting for execution |
| `v8_slots` | 10 | V8 isolate execution slots |
| `seccomp_slots` | 4 | seccomp-BPF sandbox slots |
| `wasm_slots` | 2 | WebAssembly execution slots |
| `tee_slots` | 1 | Trusted Execution Environment slots |
| `executing` | Unbounded | Currently executing requests |
| `completed` | Unbounded | Finished requests |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
