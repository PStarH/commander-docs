# Python SDK

Client HTTP fin (`commander-ai`) vers l’API server — pas un runtime Python in-process.

## Installation (monorepo)

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander/packages/python-sdk
pip install -e ".[dev]"
```

PyPI (quand publié) : `pip install commander-ai`.

## Démarrage

```python
import asyncio
from commander import CommanderClient

async def main():
    async with CommanderClient(api_key="cmd-...", base_url="http://localhost:4000") as client:
        plan = await client.plan("audit repository")
        print(plan)
        result = await client.run("list all Python files")
        print(result.status)

asyncio.run(main())
```

## Méthodes

`run` · `plan` · `stream` · `memory_*` · `health` · `metrics`

Démarrez l’API avec `pnpm gui` ou Docker.

[SDK TS](/fr/guide/sdk) · [Déploiement](/fr/deployment) · [API](/fr/api/overview)
