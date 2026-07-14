# Cookbook

End-to-end recipes. Each page: **goal → commands → expected signals → failure modes**.

| Recipe | Time | What you practice |
|--------|------|-------------------|
| [Security audit a repo](/guide/cookbook/security-audit) | ~10 min | DISPATCH-style analysis, streaming, gates |
| [Refactor a module safely](/guide/cookbook/refactor-module) | ~15 min | Plan mode → run → review |
| [CI full-auto lint fix](/guide/cookbook/ci-full-auto) | ~15 min | Non-interactive mode, exit codes |

## Conventions

All recipes assume you are in the Commander monorepo root after `pnpm install`, with one API key exported.

```bash
# Source checkout
npx tsx packages/core/src/cliEntry.ts <command>

# After building @commander/core
commander <command>
```

New to Commander? Start with [Quick Start](/guide/getting-started).
