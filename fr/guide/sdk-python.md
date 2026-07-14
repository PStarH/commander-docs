# Python SDK

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Python SDK**.

## Entrée rapide

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander/packages/python-sdk
pip install -e ".[dev]"
```

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

| Método | Descripción |
|--------|-------------|
| `run` / `plan` | Ejecutar / deliberar |
| `stream` | SSE del session |
| `memory_*` | Memoria |
| `health` / `metrics` | Ops |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
