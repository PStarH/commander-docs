# Commander

> This page is synchronized from the canonical English documentation. Français navigation is available; commands and product limits are identical in every locale.

Commander is a local-first tool for orchestrating multi-agent engineering work.
It runs on your machine, streams task activity, and lets you choose the level
of automation appropriate for the task.

## Enterprise evaluation

Commander is alpha. The current enterprise evaluation is [Shadow Phase A](https://github.com/PStarH/Commander/blob/codex/release-20260810/docs/pilot/shadow/README.md): a customer-operated evaluation of historical observations against a pinned policy. It does not execute or authorize external actions. Live Kubernetes rollback remains frozen.

## Development product paths

- **Local CLI:** the supported default for one developer or a local team.
- **Web console:** a local interface served with the API.
- **Enterprise Gateway:** an alpha `/v1` server path. It is not a
  production-proven multi-tenant SaaS.

Start with [Quick start](/getting-started), then use [Deployment](/deployment)
for a supported local installation. Read [Security and privacy](/security)
before connecting customer data or third-party tools.

## What this site promises

This site documents supported commands, configuration boundaries, and known
limits. It does not treat simulated benchmarks, CI fixtures, or compliance
reporting scaffolds as production evidence or certification.
