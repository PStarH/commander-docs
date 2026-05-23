# Troubleshooting

Common issues and their solutions.

## Installation Issues

### `pnpm install` fails
```
Error: Cannot find module '@commander/core'
```
**Solution**: Ensure you're in the project root and have all dependencies:
```bash
pnpm install
pnpm build
```

### TypeScript errors after install
```
error TS2307: Cannot find module 'xyz'
```
**Solution**:
```bash
pnpm build
# or
npx tsc --noEmit
```

## Provider Issues

### "Provider not available"
Commander can't find a valid API key. Check:
```bash
# Verify the key is set
echo $OPENAI_API_KEY

# Run diagnostics
npx tsx cli.ts doctor
```

### "Rate limited" errors
You're hitting provider rate limits. Solutions:
- Wait and retry (Commander auto-retries with backoff)
- Use multiple providers with fallback chain
- Reduce concurrency: `export COMMANDER_MAX_CONCURRENCY=1`

### "Timeout" errors
The LLM provider took too long to respond.
- Check your network connection
- Try a faster provider (Groq, Together)
- Increase timeout: `export COMMANDER_TIMEOUT_MS=120000`

## Execution Issues

### Task hangs or never completes
```bash
# Check system status
npx tsx cli.ts status

# Check for provider issues
npx tsx cli.ts doctor
```

### "Circuit breaker open"
The circuit breaker has tripped due to repeated failures. Wait 30 seconds for automatic recovery, or:
```bash
# Reset circuit breakers
npx tsx cli.ts doctor --reset
```

### Agent produces wrong results
Try a different topology:
```bash
npx tsx cli.ts run "task" --topology debate
npx tsx cli.ts run "task" --topology ensemble
```

## Build Issues

### Docker build fails
```bash
# Ensure Docker is running
docker info

# Try building with no cache
docker compose build --no-cache
```

### Test failures
```bash
# Run a specific test file
npx tsx --test tests/integration.test.ts

# Check for pre-existing failures
npx tsx --test tests/*.test.ts --grep "my test"
```

## Debug Mode

Enable verbose logging for detailed diagnostics:
```bash
export COMMANDER_DEBUG=true
npx tsx cli.ts run "task"
```

This enables debug output across all 74+ modules, including:
- LLM provider selection and calls
- Tool execution with full arguments
- Agent deliberation steps
- Cache hits and misses
- Circuit breaker state changes
