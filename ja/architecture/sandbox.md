# セキュリティサンドボックス

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/architecture/sandbox)



Commander's sandbox system provides secure execution isolation for all operations, with formal resource allocation via Petri net scheduling.

## Architecture


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

## Security Profiles


| Profile | Shell Access | File Write | Network | Best For |
|---------|-------------|-----------|---------|----------|
| **READ_ONLY** (strict) | None | Read-only | Blocked | Code review, untrusted input |
| **WORKSPACE_WRITE** (standard) | Allowed (sandboxed) | Project files | Allowed | Development |
| **FULL_ACCESS** (permissive) | Full | Any | Allowed | CI/CD, automation |
| **HARDENED** | None | Denied | Blocked | Untrusted code execution |

## Execution Policies


Policies control what operations are permitted:

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

## Petri Net Scheduler


The sandbox uses a Petri net model for formal resource allocation, ensuring deadlock-free concurrent execution:

| Place | Capacity | Purpose |
|-------|----------|---------|
| `pending` | Unbounded | Requests waiting for execution |
| `v8_slots` | 10 | V8 isolate execution slots |
| `seccomp_slots` | 4 | seccomp-BPF sandbox slots |
| `wasm_slots` | 2 | WebAssembly execution slots |
| `tee_slots` | 1 | Trusted Execution Environment slots |
| `executing` | Unbounded | Currently executing requests |
| `completed` | Unbounded | Finished requests |

Transitions: `admit_<tier>` (pending + slot → executing) and `complete_<tier>` (executing → completed + slot returned).

The scheduler includes deadlock analysis (true deadlock, unsafe, saturated, safe) and safe-state verification before admitting new requests.

## Trusted Execution Environment (TEE)


The TEE sandbox uses Node.js `worker_threads` for isolated V8 Isolates, replacing `new Function()` to prevent code injection:

- Code executes in an isolated worker thread
- No access to main process memory or modules
- Communication via message passing only
- Enforced CPU and memory limits

## seccomp-BPF (Linux)


On Linux, the sandbox uses seccomp-BPF for system call filtering:

- Allowlist approach: only approved syscalls are permitted
- Per-profile filter customization
- Blocks `ptrace`, `process_vm_readv`, and other escalation vectors

## Approval Workflow


Sensitive operations require human approval:

```typescript
import { ApprovalManager } from '@commander/core';

const approval = new ApprovalManager();

// Operations that trigger approval:
// - File deletion
// - External network requests
// - Shell commands with sudo
// - Modifying git configuration
```

The approval system defaults to fail-closed — unknown or high-risk tools are denied unless explicitly approved.

## Platform Support


| Platform | Sandbox Method |
|----------|---------------|
| macOS | Native sandbox + seccomp |
| Linux | Docker / seccomp-BPF / TEE |
| Windows | Windows Sandbox / WSL |

## 使い方


Set the security profile via environment:

```bash
export COMMANDER_SECURITY_PROFILE=strict
npx tsx packages/core/src/cliEntry.ts run "review this code"
```
