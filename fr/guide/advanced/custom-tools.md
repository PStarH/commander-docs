# Tools custom

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Tools custom**.

## Entrée rapide

```typescript
import { ToolRegistry } from '@commander/core';

class MyTool {
  name = 'my_tool';
  description = 'Does something useful';
  // schema de argumentos + execute(...)
}

ToolRegistry.register(new MyTool(), 'custom');
```

```bash
# Las tools built-in ya están registradas en el runtime
npx tsx packages/core/src/cliEntry.ts run "use tools to inspect the repo" --stream
```

| Práctica | Por qué |
|----------|---------|
| Schema estricto | Evita tool calls basura del modelo |
| Timeouts | Tools colgadas matan el run |
| Idempotencia | Reintentos seguros |
| Compensación | Si muta estado, registra rollback |
| Aprobación | Tools peligrosas → modo `suggest` / policy |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
