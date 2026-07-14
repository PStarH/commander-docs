# Cookbook : audit de sécurité

```bash
export COMMANDER_MODE=read-only
npx tsx packages/core/src/cliEntry.ts plan "audit this repository for security vulnerabilities"
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities" --stream
```

[Sécurité](/fr/guide/security)
