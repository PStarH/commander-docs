# Solución de problemas

Problemas habituales y cómo resolverlos.

> **CLI:** en el monorepo use  
> `npx tsx packages/core/src/cliEntry.ts <command>`  
> Tras compilar `@commander/core`, use `commander <command>`.

## Instalación

### Falla `pnpm install`

```
Error: Cannot find module '@commander/core'
```

**Solución:** desde la raíz del monorepo:

```bash
pnpm install
pnpm build
```

### Errores de TypeScript tras instalar

```bash
pnpm build
# o
npx tsc --noEmit
```

## Proveedores

### «Provider not available»

Commander no encuentra una API key válida:

```bash
echo $OPENAI_API_KEY
npx tsx packages/core/src/cliEntry.ts doctor
```

### Rate limited

- Espere y reintente (backoff automático)
- Use varios proveedores con cadena de fallback
- Baje concurrencia: `export COMMANDER_MAX_CONCURRENCY=1`

### Timeout

- Red / proveedor
- Proveedor más rápido (Groq, Together)
- `export COMMANDER_TIMEOUT_MS=120000`

## Ejecución

### La tarea se cuelga

```bash
npx tsx packages/core/src/cliEntry.ts status
npx tsx packages/core/src/cliEntry.ts doctor
```

### «Circuit breaker open»

Espere ~30s o:

```bash
npx tsx packages/core/src/cliEntry.ts doctor --reset
```

### Resultados incorrectos

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
npx tsx packages/core/src/cliEntry.ts plan "task"
```

## Docker

```bash
docker info
docker compose build --no-cache
```

## Debug

```bash
export COMMANDER_DEBUG=true
npx tsx packages/core/src/cliEntry.ts run "task" --stream
```

## Relacionado

- [Inicio rápido](/es/guide/getting-started)
- [Instalación](/es/guide/installation)
- [Proveedores](/es/guide/providers)
