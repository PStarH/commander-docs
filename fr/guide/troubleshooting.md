# Dépannage

> Monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Fournisseur indisponible

```bash
echo $OPENAI_API_KEY
npx tsx packages/core/src/cliEntry.ts doctor
```

## Rate limit / timeout

- Attendre, `COMMANDER_MAX_CONCURRENCY=1`, 2ᵉ clé  
- `COMMANDER_TIMEOUT_MS=120000`  

## Hang / circuit breaker

```bash
npx tsx packages/core/src/cliEntry.ts status
npx tsx packages/core/src/cliEntry.ts doctor --reset
```

## Mauvais résultats

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
npx tsx packages/core/src/cliEntry.ts plan "task"
```

## Debug

```bash
export COMMANDER_DEBUG=true
npx tsx packages/core/src/cliEntry.ts run "task"
```

[FAQ](/fr/guide/faq) · [Issues](https://github.com/PStarH/Commander/issues) · [Architecture](/fr/architecture/overview)
