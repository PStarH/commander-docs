# Solución de problemas

> Monorepo: `npx tsx packages/core/src/cliEntry.ts <cmd>` · Tras build: `commander <cmd>`

## Instalación

```bash
pnpm install && pnpm build
```

## Proveedor no disponible

```bash
echo $OPENAI_API_KEY
npx tsx packages/core/src/cliEntry.ts doctor
```

## Rate limit / timeout

- Espera, `COMMANDER_MAX_CONCURRENCY=1`, segunda key  
- `COMMANDER_TIMEOUT_MS=120000`  

## Cuelgue / circuit breaker

```bash
npx tsx packages/core/src/cliEntry.ts status
npx tsx packages/core/src/cliEntry.ts doctor --reset
```

## Resultados malos

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
```

## Debug

```bash
export COMMANDER_DEBUG=true
npx tsx packages/core/src/cliEntry.ts run "task"
```

[FAQ](/es/guide/faq) · [Issues](https://github.com/PStarH/Commander/issues)
