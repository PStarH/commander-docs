# Pourquoi Commander

Commander s’adresse aux ingénieurs qui refusent de traiter les systèmes multi-agents comme une boîte noire.

**Pas de constructeur de graphes. Pas de YAML. Pas d’« espérons que ça a marché ».**  
Une clé API → classifier la tâche → choisir la topologie → streamer chaque décision → vérifier chaque sortie.

## En un coup d’œil

| Dimension | Commander | Frameworks multi-agents typiques |
|-----------|-----------|----------------------------------|
| **Démarrage** | Tâche en langage naturel + une clé | Construire un graphe, écrire du YAML/JSON |
| **Topologie** | 5 topologies canoniques auto-sélectionnées (SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW) | Vous câblez les arêtes |
| **Visibilité** | SSE live : pensées, outils, portes de qualité | Logs après coup ou runs opaques |
| **Qualité** | 5 couches (hallucination, cohérence, complétude, exactitude, sécurité) | Optionnel / maison |
| **Fournisseurs** | 25 avec auto-détection et bascule | Souvent 1–2 de premier rang |
| **Production** | Circuit breakers, DLQ, saga, checkpoints WAL, multi-tenant | Démo d’abord ; ops ensuite |
| **Intégration** | CLI, SDK TypeScript, API HTTP, client Python | Souvent une seule surface |
| **Tests** | 6700+ | Très variable |

## Quand choisir Commander

**Choisissez Commander si vous :**

- Devez **voir** ce que font les agents pendant l’exécution  
- Voulez que topologie et nombre d’agents soient choisis pour vous  
- Tenez au **failover**, aux checkpoints et à l’auditabilité en production  
- Préférez CLI / SDK à un constructeur de graphes  
- Gérez des charges sensibles ou multi-tenant  

**Regardez ailleurs si vous :**

- N’avez besoin que d’un chat completion avec tools  
- Voulez du SaaS géré sans self-host (le cloud reste sur la [roadmap](/fr/community))  
- Préférez des frameworks 100 % Python in-process, sans runtime Node  

## Face aux approches courantes

### Face aux assistants « un agent + tools »

Les assistants de code optimisent un modèle et un fil. Commander optimise des **équipes d’agents**, une échelle automatique (1–20) et un travail multi-étapes **vérifié**.

### Face aux orchestrateurs à graphes (style LangGraph)

Les graphes excellent quand vous **voulez** dessiner chaque arête. Commander échange cela contre :

1. Une délibération qui choisit la topologie selon classe et complexité  
2. Une observabilité stream par défaut  
3. Des primitives d’ops (breakers, DLQ, compensation) sans autre couche plateforme  

Vous pouvez toujours forcer topologie et nombre d’agents.

### Face aux librairies type « crew »

Les crews excellent sur les rôles et la collaboration. Commander ajoute :

- Topologies canoniques avec arbre de décision  
- Failover sur 25 backends  
- Portes de qualité et chemins de récupération production  
- Console web + API HTTP pour l’ops, pas seulement les scripts  

## Preuves (honnêtes)

| Affirmation | Où ça vit |
|-------------|-----------|
| 25 fournisseurs | [Fournisseurs](/fr/guide/providers), `providerRegistry.ts` |
| 5 topologies | [Arbre de topologie](/fr/guide/usage/topology-decision-tree) |
| 18 tools intégrés | [Tools](/fr/architecture/tools) |
| 6700+ tests | CI / [Benchmarks](/fr/guide/benchmarks) |
| Streaming | [Agent Runtime](/fr/architecture/agent-runtime), `run --stream` |
| Posture sécurité | [Sécurité](/fr/guide/security) |

Les benchmarks sont des scripts reproductibles du monorepo — pas des captures marketing. Voir [Benchmarks](/fr/guide/benchmarks).

## Goût en 60 secondes

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "explain this repository architecture" --stream
```

Succès : classification → topologie → étapes d’agents → portes de qualité dans le stream.

## Suite

- [Démarrage rapide](/fr/guide/getting-started)  
- [Cookbook](/fr/guide/cookbook/)  
- [Architecture](/fr/architecture/overview)  
