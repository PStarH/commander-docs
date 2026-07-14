# Community

Commander is open source (MIT) and built in public. Here is how to get involved today.

## Get involved

| Channel | Status | Link |
|---------|--------|------|
| **GitHub** | Live | [github.com/PStarH/Commander](https://github.com/PStarH/Commander) — issues, PRs, stars |
| **Discussions** | Use GitHub Issues | Feature ideas and Q&A via [Issues](https://github.com/PStarH/Commander/issues) |
| **Docs** | Live | This site + PRs on [commander-docs](https://github.com/PStarH/commander-docs) |
| **Discord / Twitter** | Planned | Not live yet — follow the repo for announcements |

## Contributing

We welcome contributions of all sizes — bug fixes, docs, providers, tools, and topologies.

### Quick start for contributors

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
# Prefer project scripts when available:
pnpm test:all   # or: cd packages/core && npx tsx --test tests/*.test.ts
```

### Areas that help most

- **New tools** — filesystem, web, code analysis, integrations
- **LLM providers** — via the provider registration interface
- **Topologies** — new orchestration patterns with tests
- **Documentation** — guides, API accuracy, examples
- **Bug fixes** — issues tagged `good-first-issue`

### Guidelines

- All tests must pass (`# fail 0`)
- TypeScript strict mode — no `as any` or `@ts-ignore` in production code
- Follow existing patterns; add tests for new behavior
- Keep commits atomic and well-described
- Docs live in [commander-docs](https://github.com/PStarH/commander-docs) — open PRs against `master`

## Roadmap

| Area | Status | Details |
|------|--------|---------|
| **Event Sourcing** | Shipped (0.2.x) | WAL + hash chain, deterministic replay, snapshot recovery |
| **Enterprise Security** | Shipped (0.2.x) | 7-layer gateway, DLP, capability tokens, plugin sandboxing |
| **RAG Knowledge Base** | Shipped (0.2.x) | Optional plugin, HNSW vector search |
| **Unified Audit Log** | Shipped (0.2.x) | Cross-source aggregation, query/export API |
| **Petri Net Scheduler** | Shipped (0.2.x) | Formal resource allocation, deadlock detection |
| **Recovery Bootstrapper** | Shipped (0.2.x) | Zombie run detection, automatic recovery on startup |
| **npm publish** | In progress | `@commander/core`, `@commander/sdk` public packages |
| **Cloud Platform** | Planned | Managed API, usage dashboard, API key management |
| **Enterprise SSO** | Planned | SSO/SAML, VPC deployment, SLA support |
| **Community spaces** | Planned | Discord, showcase gallery |
| **Ecosystem** | Planned | More providers, tools, template projects |

## Trust signals

[![CI](https://img.shields.io/github/actions/workflow/status/PStarH/Commander/ci.yml?style=flat-square&label=CI)](https://github.com/PStarH/Commander/actions)
[![License](https://img.shields.io/github/license/PStarH/Commander?style=flat-square)](https://github.com/PStarH/Commander/blob/master/LICENSE)
[![Docs](https://img.shields.io/badge/docs-live-22C55E?style=flat-square)](https://pstarh.github.io/commander-docs/)
[![Stars](https://img.shields.io/github/stars/PStarH/Commander?style=social)](https://github.com/PStarH/Commander/stargazers)

## Contribute docs

See [Contributing](/guide/contributing) for local setup, content rules, and i18n notes.

## Showcase

List your project on the [Showcase](/guide/showcase) page (PR welcome).

## Stay updated

- Star [Commander](https://github.com/PStarH/Commander)
- Watch [changelog](/guide/changelog) for release notes
- Open an issue when something in the docs is wrong — we treat that as a first-class bug
- Security reports: [Security](/guide/security) (private email — not public issues)
- 中文入口: [简体中文](/zh/)

## Docs for AI assistants

- [`llms.txt`](https://pstarh.github.io/commander-docs/llms.txt) — short index  
- [`llms-full.txt`](https://pstarh.github.io/commander-docs/llms-full.txt) — full route outline
