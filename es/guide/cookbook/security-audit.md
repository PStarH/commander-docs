# Cookbook: auditoría de seguridad

```bash
export COMMANDER_MODE=read-only
npx tsx packages/core/src/cliEntry.ts plan "audit this repository for security vulnerabilities, secrets, and risky dependencies"
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities, secrets, and risky dependencies" --stream
```

Éxito: topología en plan, stream con tools/gates, resumen de hallazgos.

[Seguridad](/es/guide/security)
