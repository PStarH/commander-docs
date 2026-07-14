# Cookbook : CI full-auto lint fix

**Cookbook : CI full-auto lint fix.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

**Temps :** ~15 min à brancher · **Risque :** haute autonomie — isoler dans un job avec revue PR

## Règles de conception CI

1. Branche jetable ou workflow PR — jamais de force-push sur main par l’agent
2. Exporter **uniquement** les secrets nécessaires au job
3. `COMMANDER_MODE=full-auto` seulement après dry-run sur un dépôt d’exemple
4. Conserver les logs en artefacts CI

## 1. Dry-run local

```bash
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors in this repository" --stream
```

Vérifiez le code de sortie et que le git diff est acceptable.

## 2. Esquisse GitHub Actions

```yaml
name: Commander lint fix
on:
  workflow_dispatch:
  # ou schedule / pull_request

jobs:
  fix:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 9
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: pnpm
      - name: Install Commander
        run: |
          git clone --depth 1 https://github.com/PStarH/Commander.git /tmp/Commander
          cd /tmp/Commander && pnpm install
      - name: Run Commander
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          COMMANDER_MODE: full-auto
        run: |
          cd $GITHUB_WORKSPACE
          npx tsx /tmp/Commander/packages/core/src/cliEntry.ts run "fix all lint errors" --stream
      - name: Show diff
        run: git diff --stat
```

Adaptez les chemins si vous vendor Commander en submodule ou (plus tard) package publié. **Le chemin principal aujourd’hui est le clone monorepo.**

## 3. Checklist de succès

- [ ] Job non interactif (pas de prompts TTY)
- [ ] Logs avec délibération + stream
- [ ] Diff revu par un humain avant merge
- [ ] Secrets non imprimés dans les logs

## Modes de panne

| Problème           | Action                                                 |
| ------------------ | ------------------------------------------------------ |
| Hang interactif    | `full-auto` ; désactiver les prompts d’approbation     |
| Rate limits        | Sérialiser les jobs ; cache ; prompt plus étroit       |
| Edits destructeurs | Prompt étroit (« eslint only », globs) ; exiger une PR |

## Voir aussi

- [FAQ — CI/CD](/fr/guide/faq)
- [Déploiement](/fr/deployment)
- [Dépannage](/fr/guide/troubleshooting)
