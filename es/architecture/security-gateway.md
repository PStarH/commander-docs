# Gateway de seguridad

Documentación en español de **Gateway de seguridad**, alineada con el monorepo y la guía inglesa.

## Entrada rápida

```
entry_1 → SHA256(prev_hash | entry_1) → hash_1
entry_2 → SHA256(hash_1 | entry_2) → hash_2
```

```typescript
// buildSandboxedLoadContext() — only for third-party plugins
const sandboxContext = {
  registerHook: enforcer.wrapRegisterHook(...),
  readFile: enforcer.wrapReadFile(...),
  writeFile: enforcer.wrapWriteFile(...),  // mode 0o600
  fetch: enforcer.wrapFetch(...),          // domain + port check
  getEnvVar: enforcer.wrapGetEnvVar(...),
  getConfig: enforcer.wrapGetConfig(...),
  log: enforcer.wrapLog(...),
};
// hookManager is NOT included — prevents privilege escalation
```

| Layer | Name | Purpose |
|-------|------|---------|
| 1 | Zero-Trust Signature | Integrity verification + replay prevention |
| 2 | Authentication | API Key validation with timing-safe comparison |
| 3 | Rate Limiting | Global token bucket + tiered IP limits |
| 4 | Input Scanning | Content injection detection + input validation |
| 5 | Cost Pre-Check | Bill explosion prevention (pre-call estimation) |
| 6 | Request Processing | Business logic execution |
| 7 | Output Scanning | DLP data leak prevention + cost recording |


| Pattern | Example |
|---------|---------|
| API Key | `sk-...`, `sk-ant-...` |
| JWT | `eyJ...` |
| Private Key (PEM) | `-----BEGIN PRIVATE KEY-----` |
| Credit Card (Luhn) | `4111 1111 1111 1111` |
| SSN | `123-45-6789` |
| Email | `user@example.com` |
| Phone | `+1-555-0123` |
| Internal IP | `10.0.0.1`, `192.168.1.1` |
| Database Connection String | `mongodb://user:pass@host:port` |
| AWS/GCP/Azure Credentials | `AKIA...`, `AIza...` |
| China ID Card (checksum) | `110101199003077735` |
| Bank Account | Numeric with branch code |


## Notas

- CLI monorepo: `cliEntry.ts` · tras build: `commander`  
- Métricas: 25 proveedores · 5 topologías · 18 tools · 6700+ tests  
- Firmas API exactas: monorepo / [API overview](/es/api/overview)  

## Relacionado

- [Arquitectura](/es/architecture/overview)  
- [Inicio rápido](/es/guide/getting-started)  
