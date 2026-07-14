# Configuration

**Configuration.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

## Entrée rapide

```json
{
  "provider": "auto",
  "model": "auto",
  "mode": "balanced",
  "topology": "auto",
  "budget": "auto",
  "mcpServers": []
}
```

```bash
export COMMANDER_MODE=plan
npx tsx packages/core/src/cliEntry.ts config
npx tsx packages/core/src/cliEntry.ts mode read-only
```

| Variable | Default | Descripción |
|----------|---------|-------------|
| `COMMANDER_MODE` | `auto-edit` | `plan`, `read-only`, `auto-edit`, `full-auto`, `suggest` |
| `COMMANDER_DEBUG` | `false` | Logging verbose |
| `COMMANDER_LOG_LEVEL` | `info` | `debug`, `info`, `warn`, `error` |
| `COMMANDER_MAX_CONCURRENCY` | `5` | Máx. ejecuciones concurrentes de agentes |
| `COMMANDER_TIMEOUT_MS` | `120000` | Timeout por defecto (ms) |


| Variable | Default | Descripción |
|----------|---------|-------------|
| `PORT` | `4000` | Puerto HTTP |
| `HOST` | `0.0.0.0` | Host HTTP |
| `CORS_ORIGIN` | `*` | Orígenes CORS |
| `RATE_LIMIT_WINDOW_MS` | `60000` | Ventana de rate limit |
| `RATE_LIMIT_MAX` | `100` | Máx. requests por ventana |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
