# Pourquoi Commander

**Pourquoi Commander.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

**Pas de constructeur de graphes. Pas de YAML. Pas de « on espère que les agents ont bien bossé ».**  
Une clé API → classification de la tâche → choix de topologie → stream de chaque décision → vérification de chaque sortie.

## En un coup d’œil

| Dimension        | Commander                                                                                 | Frameworks agents typiques                           |
| ---------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **Démarrage**    | Tâche en langage naturel + une clé API                                                    | Construire un graphe, écrire des workflows YAML/JSON |
| **Topologie**    | 5 topologies canoniques auto-choisies (SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW) | Vous câblez les arêtes vous-même                     |
| **Visibilité**   | SSE live : pensées, tools, portes de qualité                                              | Logs après coup, ou exécutions opaques               |
| **Qualité**      | 5 couches (hallucination, cohérence, complétude, exactitude, sécurité)                    | Optionnel / à bricoler                               |
| **Fournisseurs** | 25, auto-détection + failover                                                             | Souvent 1–2 fournisseurs de premier ordre            |
| **Production**   | Circuit breakers, DLQ, saga, checkpoints WAL, multi-tenant                                | Démo d’abord ; l’ops arrive plus tard                |
| **Intégration**  | CLI, SDK TypeScript, API HTTP, client Python                                              | Souvent une seule surface                            |
| **Tests**        | 6700+                                                                                     | Très variable                                        |

## Quand choisir Commander

**Choisissez Commander si vous :**

- devez **voir** ce que font les agents pendant l’exécution
- voulez topologie et nombre d’agents choisis pour vous, pas peaufinés à la main à chaque fois
- tenez au **failover**, aux checkpoints et à l’auditabilité en production
- préférez CLI / SDK à un constructeur de graphes visuel
- gérez des charges sensibles ou multi-tenant

**Regardez ailleurs si vous :**

- n’avez besoin que d’une complétion chat avec tools
- voulez un SaaS entièrement managé sans self-host (le cloud est encore sur la [roadmap](/fr/community))
- préférez un framework Python pur in-process, sans runtime Node

## Face aux approches courantes

### vs assistants de code « un agent + tools »

Les assistants de code optimisent un modèle, un fil. Commander optimise des **équipes d’agents**, l’échelle auto (1–20) et le travail multi-étapes **vérifié**. Assistant pour les edits rapides ; Commander quand il faut recherche parallèle, revue ou orchestration.

### vs orchestrateurs à graphe (style LangGraph)

Les graphes sont puissants quand vous **voulez** dessiner chaque arête. Commander échange cela contre :

1. Une délibération qui choisit la topologie selon classe de tâche + complexité
2. Une observabilité streamée par défaut
3. Des primitives d’ops (breakers, DLQ, compensation) sans couche plateforme séparée

Vous pouvez toujours forcer topologie et nombre d’agents.

### vs bibliothèques multi-agents type « crew »

Les crews excellent en prompts de rôle et patterns de collaboration. Commander ajoute :

- Topologies canoniques avec arbre de décision
- Failover fournisseurs sur 25 backends
- Portes de qualité et chemins de récupération production
- Web Console + API HTTP pour l’ops, pas seulement des scripts

## Preuves (honnêtes)

| Affirmation       | Où la trouver                                                           |
| ----------------- | ----------------------------------------------------------------------- |
| 25 fournisseurs   | [Fournisseurs](/fr/guide/providers), `providerRegistry.ts`              |
| 5 topologies      | [Arbre de décision topologique](/fr/guide/usage/topology-decision-tree) |
| 18 tools intégrés | [Tools](/fr/architecture/tools)                                         |
| 6700+ tests       | CI / [Benchmarks](/fr/guide/benchmarks)                                 |
| Streaming         | [Agent Runtime](/fr/architecture/agent-runtime), `run --stream` / watch |
| Posture sécurité  | [Sécurité](/fr/guide/security)                                          |

Les benchmarks sont des scripts reproductibles dans le monorepo — pas des captures marketing. Voir [Benchmarks](/fr/guide/benchmarks).

## Goût en 60 secondes

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "explain this repository architecture" --stream
```

Succès : classification de délibération → choix de topologie → étapes agents → portes de qualité dans le stream.

## Suite

- [Démarrage rapide](/fr/guide/getting-started) — checklist 5 minutes
- [Cookbook](/fr/guide/cookbook/) — recettes de bout en bout
- [Vue d’architecture](/fr/architecture/overview) — comment le moteur fonctionne
