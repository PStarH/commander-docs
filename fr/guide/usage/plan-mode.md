# Mode plan

Page localisée (fr) — contenu aligné sur la documentation anglaise / espagnole pour **Mode plan**.

## Entrée rapide

```bash
# Activar modo plan
npx tsx packages/core/src/cliEntry.ts mode plan

# Luego cualquier tarea
npx tsx packages/core/src/cliEntry.ts run "refactor the database layer"

# O plan de un solo disparo
npx tsx packages/core/src/cliEntry.ts plan "implement search feature"
```

```
┃ → Deliberating task...
┃ → Complexity: HIGH (score: 72/100)
┃ → Topology: ORCHESTRATOR
┃ → Agents: 4 (1 lead + 3 specialists)
┃ → Provider: deepseek (fallback: openai → anthropic)
┃ → Token budget: 100,000
┃
┃ → Subtasks:
┃   1. Analyze existing database schema
┃   2. Design migration plan
┃   3. Implement changes (parallel: 2 agents)
┃   4. Verify and test
```



## Notes

- CLI monorepo : `packages/core/src/cliEntry.ts` · après build : `commander`  
- Métriques produit : 25 fournisseurs · 5 topologies · 18 tools · 6700+ tests  
- Pour le détail exhaustif, le monorepo et la version anglaise restent la source de vérité des signatures API  

## Lié

- [Vue d’architecture](/fr/architecture/overview)  
- [Démarrage rapide](/fr/guide/getting-started)  
- [Commandes](/fr/guide/commands)  
