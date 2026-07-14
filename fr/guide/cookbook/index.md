# Cookbook

**Cookbook.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

| Recette                                                                  | Temps   | Ce que vous pratiquez                    |
| ------------------------------------------------------------------------ | ------- | ---------------------------------------- |
| [Audit de sécurité d’un dépôt](/fr/guide/cookbook/security-audit)        | ~10 min | Analyse type DISPATCH, streaming, portes |
| [Refactoriser un module en sécurité](/fr/guide/cookbook/refactor-module) | ~15 min | Plan → run → review                      |
| [CI full-auto lint fix](/fr/guide/cookbook/ci-full-auto)                 | ~15 min | Mode non interactif, codes de sortie     |

## Conventions

Toutes les recettes supposent le monorepo Commander après `pnpm install`, avec une clé API exportée.

```bash
# Checkout source
npx tsx packages/core/src/cliEntry.ts <command>

# Après build de @commander/core
commander <command>
```

Nouveau sur Commander ? Commencez par le [démarrage rapide](/fr/guide/getting-started).
