# Cookbook : CI full-auto lint

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors in this repository" --stream
```

## Règles CI

1. Branche jetable / PR — jamais force-push sur main  
2. Secrets minimaux  
3. Dry-run local d’abord  
4. Logs en artefacts  

Schéma Actions : cloner Commander, `pnpm install`, lancer `cliEntry.ts` avec `OPENAI_API_KEY`, afficher `git diff`.

[FAQ](/fr/guide/faq) · [Déploiement](/fr/deployment)
