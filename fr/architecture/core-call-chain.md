# Chaîne d’appels core

Chemin d’une requête de l’entrée jusqu’au résultat vérifié.

## Entrées

- CLI (`cliEntry.ts` / `commander`)  
- SDK (`CommanderClient.run` / `plan`)  
- HTTP (`/execute`, Architecture V2 `/v1/runs`)  

## Étapes

1. **Environnement** — keys, mode d’approbation, tenant  
2. **Délibération** — classe la tâche, estime la complexité  
3. **Scale d’effort** — 1 à 20 agents  
4. **Routeur de topologie** — SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW  
5. **Atomisation** — sous-tâches si besoin  
6. **Runtime agents** — boucle LLM ↔ tools  
7. **Vérification** — cinq portes de qualité  
8. **Synthèse** — fusion multi-agents  
9. **Persistance** — checkpoints, event log, métriques  

## Échecs et recovery

| Échec | Mécanisme |
|-------|-----------|
| Fournisseur down | Fallback + circuit breaker |
| Tool mutante | Saga / compensation |
| Crash process | Checkpoint SQLite WAL + resume |
| Mauvaise qualité | Retry avec contexte de gate |

## Lié

- [Runtime](/fr/architecture/agent-runtime)  
- [Multi-agents](/fr/architecture/multi-agent)  
- [Vérification](/fr/architecture/verification)
