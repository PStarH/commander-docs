# Sécurité

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Sécurité**.

## Entrée rapide

```bash
export COMMANDER_MODE=read-only
export COMMANDER_API_KEY="long-random-secret"
export OLLAMA_BASE_URL=http://localhost:11434
```

```bash
pnpm benchmark:redteam
pnpm benchmark:agentdojo
```

| Amenaza | Mitigación |
|---------|------------|
| Inyección | Escaneo de tools, sanitizers, gates de irreversibilidad |
| Secretos | DLP, logs sin secretos |
| Agentes desbocados | Modos de aprobación, tokens, timeouts, breakers |
| Proveedor caído | Failover, rate limits, cuotas |
| Cross-tenant | Aislamiento de storage/memoria/caché |
| Supply chain | npm audit; keys fuera del git |


## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
