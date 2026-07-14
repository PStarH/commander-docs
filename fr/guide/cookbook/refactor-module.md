# Cookbook : refactoriser un module en sécurité

**Cookbook : refactoriser un module en sécurité.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

**Temps :** ~15 min · **Risque :** écrit des fichiers — commencez en `plan` / `suggest`

## 1. Préparation

```bash
cd /path/to/your-project   # ou monorepo Commander pour un dry-run
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=plan
```

Sur une vraie app, branche propre :

```bash
git checkout -b chore/commander-refactor
git status
```

## 2. Prévisualiser le plan

```bash
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module to reduce duplication; keep public API stable"
```

**Attendu :** topologie (souvent CHAIN ou ORCHESTRATOR), étapes, tools, budget — **aucune édition de fichier**.

Vérifiez :

- Le plan ne touche-t-il que les modules visés ?
- REVIEW est-il plus adapté pour un changement risqué ?

## 3. Mode suggest (humain dans la boucle)

```bash
export COMMANDER_MODE=suggest
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module to reduce duplication; keep public API stable" --stream
```

Approuvez / refusez les edits selon les prompts du terminal (si l’UI d’approbation est active pour votre mode).

## 4. auto-edit (quand le plan est digne de confiance)

```bash
export COMMANDER_MODE=auto-edit
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module to reduce duplication; keep public API stable" --stream
```

## 5. Vérifier localement

```bash
git diff
# spécifique au projet :
pnpm test   # ou npm test / cargo test / etc.
```

## 6. Checklist de succès

- [ ] Le plan était correct avant toute écriture
- [ ] Le diff est limité aux fichiers prévus
- [ ] Tests / typecheck passent
- [ ] Vous pouvez `git checkout -- .` pour annuler

## Modes de panne

| Problème                | Action                                                    |
| ----------------------- | --------------------------------------------------------- |
| Edits trop agressifs    | Rester en `plan` / `suggest` ; réduire le scope du prompt |
| Mauvais module          | Nommer les chemins : `packages/foo/src/auth/*`            |
| Merge multi-agent flaky | Forcer `--topology chain` ou `--topology review`          |

## Voir aussi

- [Mode plan](/fr/guide/usage/plan-mode)
- [Exécuter des tâches](/fr/guide/usage/running-tasks)
- [Modes d’approbation dans la FAQ](/fr/guide/faq)
