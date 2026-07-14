# Python SDK

**Python SDK.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Method | Description |
|--------|-------------|
| `client.run(prompt, ...)` | Execute an agent task |
| `client.plan(task, ...)` | Zero-cost deliberation (no LLM call) |
| `client.stream(session_id)` | SSE event stream for a running session |
| `client.memory_write(content, ...)` | Write to memory |
| `client.memory_query(...)` | Query memory |
| `client.memory_stats()` | Memory statistics |
| `client.health()` | Liveness probe |
| `client.health_detailed()` | Detailed component health |
| `client.system_status()` | System status |
| `client.metrics()` | OpenMetrics text |


## Contenu principal

### Installation

En pratique, **Installation** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/sdk-python) pour le détail exhaustif.

### Quick Start

En pratique, **Quick Start** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/sdk-python) pour le détail exhaustif.

### API Reference

En pratique, **API Reference** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/sdk-python) pour le détail exhaustif.

### Streaming

En pratique, **Streaming** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/sdk-python) pour le détail exhaustif.

### Sync Wrapper

En pratique, **Sync Wrapper** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/sdk-python) pour le détail exhaustif.

### Configuration

En pratique, **Configuration** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/sdk-python) pour le détail exhaustif.

### Architecture

En pratique, **Architecture** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/sdk-python) pour le détail exhaustif.

### Development

En pratique, **Development** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/sdk-python) pour le détail exhaustif.

## Exemples (code inchangé)

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander/packages/python-sdk
pip install -e ".[dev]"
```

```bash
pip install commander-ai
```

```python
import asyncio
from commander import CommanderClient

async def main():
    async with CommanderClient(
        api_key="cmd-...",
        base_url="http://localhost:4000",
    ) as client:
        # Zero-cost planning
        plan = await client.plan("audit repository for security vulnerabilities")
        print(f"Topology: {plan.topology}")
        print(f"Budget: ${plan.estimate.cost_budget_usd:.2f}")

        # Execute
        result = await client.run("list all Python files")
        print(f"Status: {result.status}")

asyncio.run(main())
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
