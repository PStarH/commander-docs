# Community

Commander is open source and community-driven. Here's how to get involved.

## Get Involved

- **GitHub**: [github.com/PStarH/Commander](https://github.com/PStarH/Commander) — star, fork, report issues, contribute PRs
- **Discord**: Coming soon — general discussion, help, showcase, development
- **Twitter**: Coming soon

## Contributing

We welcome contributions of all sizes — bug fixes, documentation improvements, new features, and tool integrations.

### Quick Start for Contributors

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
npx tsx --test packages/core/tests/*.test.ts  # All green required
```

### Areas to Contribute

- **New tools**: Add built-in tools for filesystem, web, code analysis, etc.
- **LLM providers**: Integrate additional providers via the provider interface
- **Topologies**: Implement new orchestration patterns
- **Documentation**: Improve guides, API docs, and examples
- **Bug fixes**: Issues tagged `good-first-issue` are a great starting point

### Guidelines

- All tests must pass (`# fail 0`)
- TypeScript strict mode — no `as any` or `@ts-ignore` in production code
- Follow existing code patterns and conventions
- Add tests for new functionality
- Keep commits atomic and well-described

## Roadmap

| Area | Coming Soon |
|------|-------------|
| **Cloud Platform** | Managed API, usage dashboard, API key management |
| **Enterprise** | SSO/SAML, audit logs, VPC deployment, SLA support |
| **Community** | Discord server, contributor guides, showcase gallery |
| **Ecosystem** | More LLM providers, tool integrations, template projects |

## Stay Updated

- ⭐ Star the [GitHub repo](https://github.com/PStarH/Commander) to track progress
- Watch the [changelog](/guide/changelog) for release notes
- Join Discord (coming soon) for community discussions
