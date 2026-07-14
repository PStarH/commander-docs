# Sandbox de seguridad

Perfiles de ejecución que limitan lo que un agente puede hacer (filesystem, red, syscalls según plataforma).

Úsalo cuando:

- Ejecutas shell / scripts no confiables  
- Multi-tenant con aislamiento fuerte  
- Compliance exige contención  

```bash
# el runtime aplica perfiles según configuración del monorepo
npx tsx packages/core/src/cliEntry.ts run "review this code"
```

[Gateway](/es/architecture/security-gateway)
