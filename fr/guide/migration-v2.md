# Migration Architecture V2

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Migration Architecture V2**.

## Entrée rapide

```bash
npx tsx packages/core/src/cliEntry.ts plan "your task"
npx tsx packages/core/src/cliEntry.ts run "your task" --stream
```

| Plano | Responsabilidad |
|-------|-----------------|
| Gateway | Acepta runs, WorkGraphs, pause/resume/cancel — no ejecuta agentes en V2 puro |
| Worker | Reclama steps, ejecuta, reporta |
| Kernel | Tablas `commander_*` en Postgres |


| Variable | Default | Significado |
|----------|---------|-------------|
| `COMMANDER_V2_MODE` | `0` | `1` activa V2 |
| `DATABASE_URL` | — | **Requerido** en V2 |
| `COMMANDER_LEGACY_EXECUTION` | `0` | Puente temporal |
| `COMMANDER_WORKER_*` | — | kind, auth, concurrency, tenants |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
