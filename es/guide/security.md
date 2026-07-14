# Seguridad

Resumen para operadores. Profundidad: [Gateway](/es/architecture/security-gateway), [Sandbox](/es/architecture/sandbox), [Multi-tenant](/es/architecture/multi-tenancy).

## Reportar vulnerabilidades

**No uses issues públicos.** Escribe a **sampan090611@gmail.com** con impacto, paths, reproducción y PoC. Acuse en ~48 h.

## Amenazas y mitigaciones

| Amenaza | Mitigación |
|---------|------------|
| Inyección | Escaneo de tools, sanitizers, gates de irreversibilidad |
| Secretos | DLP, logs sin secretos |
| Agentes desbocados | Modos de aprobación, tokens, timeouts, breakers |
| Proveedor caído | Failover, rate limits, cuotas |
| Cross-tenant | Aislamiento de storage/memoria/caché |
| Supply chain | npm audit; keys fuera del git |

## Controles

```bash
export COMMANDER_MODE=read-only
export COMMANDER_API_KEY="long-random-secret"
export OLLAMA_BASE_URL=http://localhost:11434
```

Modos: `plan` · `read-only` · `suggest` · `auto-edit` · `full-auto`.

## Benchmarks

```bash
pnpm benchmark:redteam
pnpm benchmark:agentdojo
```

## Checklist producción

- [ ] API key fuerte  
- [ ] Modo de aprobación correcto  
- [ ] Secrets en vault/env  
- [ ] Health/metrics  
- [ ] DLQ/compensación  
- [ ] Backups  

Ver [Seguridad del monorepo](https://github.com/PStarH/Commander/blob/master/SECURITY.md).
