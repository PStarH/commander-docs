# Arbre de décision topologique

**Arbre de décision topologique.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

## Référence rapide

```
Tâche simple et bien définie ?
├── OUI → SINGLE
└── NON → Sous-tâches indépendantes ?
    ├── OUI → DISPATCH
    └── NON → Dépendent-elles les unes des autres ?
        ├── OUI → CHAIN
        └── NON → Lead agent clair ?
            ├── OUI → ORCHESTRATOR
            └── NON → REVIEW
```

## Détails

| Topologie    | Quand                                    | Agents |
| ------------ | ---------------------------------------- | ------ |
| SINGLE       | Simple, bien bornée                      | 1      |
| CHAIN        | Transformations multi-étapes dépendantes | 2–3    |
| DISPATCH     | Sous-tâches parallélisables              | 2–10   |
| ORCHESTRATOR | Décomposition claire                     | 3–8    |
| REVIEW       | Haut risque, validation croisée          | 2–5    |

## Score de complexité

| Score  |     Auto     |
| :----: | :----------: |
|  0–20  |    SINGLE    |
| 20–40  |    CHAIN     |
| 40–60  |   DISPATCH   |
| 60–80  | ORCHESTRATOR |
| 80–100 |    REVIEW    |

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
```

## Voir aussi

- [Multi-agent](/fr/architecture/multi-agent)
- [Explorateur de topologie](/fr/guide/topology-explorer)
- [Exécuter des tâches](/fr/guide/usage/running-tasks)
