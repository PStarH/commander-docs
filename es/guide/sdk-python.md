# Python SDK

Cliente HTTP fino (`commander-ai`) hacia el API server de Commander — no es un runtime Python in-process.

## Instalación (monorepo)

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander/packages/python-sdk
pip install -e ".[dev]"
```

Cuando esté en PyPI: `pip install commander-ai`.

## Inicio rápido

```python
import asyncio
from commander import CommanderClient

async def main():
    async with CommanderClient(
        api_key="cmd-...",
        base_url="http://localhost:4000",
    ) as client:
        plan = await client.plan("audit repository for security vulnerabilities")
        print(plan)
        result = await client.run("list all Python files")
        print(result.status)

asyncio.run(main())
```

## API principal

| Método | Descripción |
|--------|-------------|
| `run` / `plan` | Ejecutar / deliberar |
| `stream` | SSE del session |
| `memory_*` | Memoria |
| `health` / `metrics` | Ops |

Arranca el server con `pnpm gui` o Docker ([Despliegue](/es/deployment)).

## Relacionado

- [Agent SDK TS](/es/guide/sdk)  
- [API overview](/es/api/overview)
