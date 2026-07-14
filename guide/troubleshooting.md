# Troubleshooting

Common issues and their solutions.

> **CLI note:** From a monorepo checkout use  
> `npx tsx packages/core/src/cliEntry.ts <command>`  
> After building `@commander/core`, use `commander <command>` instead.

## Installation issues

### `pnpm install` fails

```
Error: Cannot find module '@commander/core'
```

**Solution:** Run from the monorepo root and install all workspaces:

```bash
pnpm install
pnpm build
```

### TypeScript errors after install

```
error TS2307: Cannot find module 'xyz'
```

**Solution:**

```bash
pnpm build
# or
npx tsc --noEmit
```

## Provider issues

### "Provider not available"

Commander can't find a valid API key. Check:

```bash
# Verify the key is set
echo $OPENAI_API_KEY

# Run diagnostics
npx tsx packages/core/src/cliEntry.ts doctor
```

### "Rate limited" errors

You're hitting provider rate limits. Solutions:

- Wait and retry (Commander auto-retries with backoff)
- Use multiple providers with a fallback chain
- Reduce concurrency: `export COMMANDER_MAX_CONCURRENCY=1`

### "Timeout" errors

The LLM provider took too long to respond.

- Check your network connection
- Try a faster provider (Groq, Together)
- Increase timeout: `export COMMANDER_TIMEOUT_MS=120000`

## Execution issues

### Task hangs or never completes

```bash
npx tsx packages/core/src/cliEntry.ts status
npx tsx packages/core/src/cliEntry.ts doctor
```

### "Circuit breaker open"

The circuit breaker tripped due to repeated failures. Wait ~30s for automatic recovery, or:

```bash
npx tsx packages/core/src/cliEntry.ts doctor --reset
```

### Agent produces wrong results

Force a stricter topology:

```bash
# Canonical topologies: single | chain | dispatch | orchestrator | review
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
npx tsx packages/core/src/cliEntry.ts plan "task"
```

## Build issues

### Docker build fails

```bash
docker info
docker compose build --no-cache
```

### Test failures

```bash
cd packages/core
npx tsx --test tests/integration.test.ts
npx tsx --test tests/*.test.ts
```

## Debug mode

```bash
export COMMANDER_DEBUG=true
npx tsx packages/core/src/cliEntry.ts run "task"
```

This enables verbose output across modules, including:

- LLM provider selection and calls
- Tool execution with full arguments
- Agent deliberation steps
- Cache hits and misses
- Circuit breaker state changes

## Still stuck?

- [FAQ](/guide/faq)
- [GitHub Issues](https://github.com/PStarH/Commander/issues)
- [Architecture overview](/architecture/overview)
