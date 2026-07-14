# Runtime agents

Boucle **LLM → tools → vérification → retry**, avec streaming SSE optionnel.

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --stream
```

Fiabilité : timeouts, cache tools, breakers, checkpoints.

[Providers](/fr/guide/providers) · [Vérification](/fr/architecture/verification)
