# Quick start

> This page is synchronized from the canonical English documentation. 简体中文 navigation is available; commands and product limits are identical in every locale.

## Prerequisites

Use Node.js 22 and pnpm 9. The initial simulated demo requires no provider credentials. Enterprise customers should start with [Shadow Phase A](https://github.com/PStarH/Commander/blob/codex/release-20260810/docs/pilot/shadow/README.md), which evaluates historical observations without external actions.

```bash
git clone --branch codex/release-20260810 --single-branch https://github.com/PStarH/Commander.git
cd Commander
corepack enable
pnpm install --frozen-lockfile
pnpm build
pnpm demo:l4-a
```

## Optional provider-backed development

Configure a provider credential through your secret-management process before running the command below. Task content may leave your machine, provider fees may apply, and enabled tools can change local state. This is not the enterprise Shadow evaluation.

```bash
pnpm exec tsx packages/core/src/cliEntry.ts run "summarize this repository"
```

For the local web console, run `pnpm gui`. The local API is served on port
`4000`; the web interface is served on port `3000` for the Compose deployment.

## Next steps

- [Deployment](/deployment) for local configuration and health checks.
- [Security and privacy](/security) before connecting external systems.
- [Support and limits](/support) for the current product boundary.
