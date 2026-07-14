# Chaîne d’appels core

Chemin d’une requête de l’entrée jusqu’au résultat vérifié.

## Entrées

CLI · SDK · HTTP (`/execute`, V2 `/v1/runs`)

## Étapes

1. Environnement (keys, mode, tenant)  
2. Délibération (classe, complexité)  
3. Scale d’effort (1–20 agents)  
4. Routeur de topologie  
5. Atomisation  
6. Runtime agents (LLM ↔ tools)  
7. Vérification (5 portes)  
8. Synthèse  
9. Persistance / métriques  

## Récupération

| Échec | Mécanisme |
|-------|-----------|
| Fournisseur down | Fallback + circuit breaker |
| Tool mutante | Compensation / saga |
| Crash | Checkpoint WAL + resume |
| Mauvaise qualité | Retry avec contexte de gate |

[Runtime](/fr/architecture/agent-runtime) · [Multi-agents](/fr/architecture/multi-agent)
