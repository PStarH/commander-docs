# Orchestration multi-agents

**Orchestration multi-agents.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

## Topologies canoniques

| Topologie        | Description                                           | Alias legacy                      |
| ---------------- | ----------------------------------------------------- | --------------------------------- |
| **SINGLE**       | Un agent gère toute la tâche                          | —                                 |
| **CHAIN**        | Pipeline séquentiel                                   | SEQUENTIAL                        |
| **DISPATCH**     | Sous-tâches indépendantes en parallèle, puis synthèse | PARALLEL                          |
| **ORCHESTRATOR** | Lead décompose, délègue, synthétise                   | HIERARCHICAL / HYBRID             |
| **REVIEW**       | Générer → critiquer → affiner                         | DEBATE / ENSEMBLE / EVALUATOR-OPT |

## Sélection

Le moteur de délibération (`deliberation.ts`) classifie chaque tâche :

| Complexité                       | Dépendances   | Topologie    |
| -------------------------------- | ------------- | ------------ |
| Trivial                          | Aucune        | SINGLE       |
| Low                              | Séquentielles | CHAIN        |
| Low                              | Indépendantes | DISPATCH     |
| Medium / High                    | Mixtes        | ORCHESTRATOR |
| High-risk / Critical / Iterative | Toute         | REVIEW       |

## Détails

- **SINGLE** — demandes simples et bien bornées
- **CHAIN** — transformations multi-étapes via artefacts
- **DISPATCH** — travail parallélisable
- **ORCHESTRATOR** — lead + spécialistes, reroutage adaptatif
- **REVIEW** — solutions indépendantes, validation croisée, raffinement

## Scaling

`effortScaler.ts` : simple 1 · modéré 2–5 · complexe 5–10 · research 10–20.

## Communication

Message bus · handoff d’agents (inbox persistante) · système d’artefacts · mémoire trois couches.

## Voir aussi

- [Arbre de décision topologique](/fr/guide/usage/topology-decision-tree)
- [Agent Runtime](/fr/architecture/agent-runtime)
- [Chaîne d’appels core](/fr/architecture/core-call-chain)
