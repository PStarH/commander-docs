# Cookbook : audit de sécurité d’un dépôt

**Cookbook : audit de sécurité d’un dépôt.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

**Temps :** ~10 min · **Risque :** surtout en lecture (préférez `read-only` ou `plan`)

## 1. Préparation

```bash
cd /path/to/Commander   # racine du monorepo
export OPENAI_API_KEY=sk-...   # ou toute clé supportée
```

Limiter les écritures pendant l’apprentissage :

```bash
export COMMANDER_MODE=read-only
```

## 2. Plan d’abord

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repository for security vulnerabilities, secrets, and risky dependencies"
```

**Attendu :** classification (souvent ANALYSIS), score de complexité, topologie (souvent DISPATCH ou REVIEW), rôles d’agents.

## 3. Exécuter en stream

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities, secrets, and risky dependencies" --stream
```

**Dans le stream, attendez :**

- Bannière de délibération (classe de tâche + topologie)
- Plusieurs agents ou tools séquentiels (grep, package audit, etc.)
- Lignes de portes qualité (ACCURACY / COMPLETENESS / SAFETY …)
- Une synthèse de findings

## 4. Forcer la topologie (optionnel)

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities" --stream --topology review
```

REVIEW force un style produce → critique quand vous voulez plus de scrutiny.

## 5. Checklist de succès

- [ ] Le plan affiche une topologie sans crash
- [ ] Le stream montre activité agent/tool
- [ ] La synthèse liste des findings concrets ou « aucun » avec périmètre
- [ ] Pas de hang sans explication (>2 min, zéro événement)

## Modes de panne

| Problème        | Action                                            |
| --------------- | ------------------------------------------------- |
| Pas de provider | `doctor` ; vérifier l’env du shell courant        |
| Audit creux     | Pointer un vrai codebase ; préciser le prompt     |
| Porte SAFETY    | Attendu si patterns type secrets — signal utile   |
| Coût / latence  | `plan` seul, ou provider rapide (Groq) pour trier |

## Voir aussi

- [Sécurité](/fr/guide/security)
- [Arbre de décision topologique](/fr/guide/usage/topology-decision-tree)
- [Watch Mode](/fr/guide/usage/watch-mode)
