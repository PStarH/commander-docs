# Security Sandbox

Commander's sandbox system provides secure execution isolation for all operations.

## Architecture

```
sandbox/
├── execPolicy.ts        ← Execution policy definitions
├── approval.ts          ← Approval workflow for sensitive operations
├── profiles.ts          ← Security profiles (strict, standard, permissive)
├── platforms.ts         ← Platform-specific sandbox configurations
├── manager.ts           ← Sandbox lifecycle management
├── executionRouter.ts   ← Route executions to appropriate backends
├── lane.ts              ← Execution lane management
├── backends/            ← Sandbox backend implementations
└── types.ts             ← Shared types
```

## Security Profiles

| Profile | Shell Access | File Write | Network | Best For |
|---------|-------------|-----------|---------|----------|
| **strict** | None | Read-only | Blocked | Code review, untrusted input |
| **standard** | Allowed (sandboxed) | Project files | Allowed | Development |
| **permissive** | Full | Any | Allowed | CI/CD, automation |

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

## Platform Support

| Platform | Sandbox Method |
|----------|---------------|
| macOS | Native sandbox + seccomp |
| Linux | Docker / seccomp-bpf |
| Windows | Windows Sandbox / WSL |

## Usage

Set the security profile via environment:

```bash
export COMMANDER_SECURITY_PROFILE=strict
npx tsx cli.ts run "review this code"
```
