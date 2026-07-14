# Explorateur interactif de topologie

**Explorateur interactif de topologie.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

## Arbre de décision

```
La tâche est-elle une question claire avec un seul responsable ?
  OUI → SINGLE
  NON ↓
Le travail forme-t-il un pipeline strict (A puis B puis C) ?
  OUI → CHAIN
  NON ↓
Des spécialistes peuvent-ils travailler en parallèle puis fusionner ?
  OUI → DISPATCH
  NON ↓
Un lead doit-il déléguer et replanifier ?
  OUI → ORCHESTRATOR
  NON ↓
La qualité / le risque exige-t-il une critique ?
  OUI → REVIEW
  sinon → commencez par DISPATCH ou `commander plan`
```

## Cartes de topologie

### SINGLE

| | |
|--|--|
| **Agents** | 1 |
| **Idéal pour** | FAQ, explication simple, transform one-shot |
| **Coût** | Le plus bas |
| **Risque** | Pas de peer review |

```bash
npx tsx packages/core/src/cliEntry.ts plan "what does this function do?"
```

### CHAIN

Pipeline séquentiel analyser → implémenter → vérifier. Coût moyen.

```bash
npx tsx packages/core/src/cliEntry.ts plan "migrate the auth module then update callers"
```

### DISPATCH

Spécialistes en parallèle + synthétiseur. Ideal pour research et audits.

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
```

### ORCHESTRATOR

Lead + workers. Gros travaux ambigus multi-modules.

```bash
npx tsx packages/core/src/cliEntry.ts plan "redesign the billing system end to end"
```

### REVIEW

Producteur + critique. Haute criticité / sécurité.

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
```

## Sélecteur rapide

| Si votre tâche est… | Essayez |
|---------------------|---------|
| Une question, une réponse | **SINGLE** |
| Étapes ordonnées dépendantes | **CHAIN** |
| Plusieurs enquêtes indépendantes | **DISPATCH** |
| Périmètre inconnu ; besoin d’un manager | **ORCHESTRATOR** |
| Correctness > vitesse | **REVIEW** |

## Forcer une topologie

```bash
npx tsx packages/core/src/cliEntry.ts run "your task" --topology dispatch --stream
```

Noms canoniques : `single` · `chain` · `dispatch` · `orchestrator` · `review`.

## Lié

- [Arbre de décision](/fr/guide/usage/topology-decision-tree)
- [Exécuter des tâches](/fr/guide/usage/running-tasks)
- [Pourquoi Commander](/fr/guide/why-commander)
- [Architecture multi-agents](/fr/architecture/multi-agent)
