# Sécurité

**Vulnérabilités :** pas d’issues publiques — **sampan090611@gmail.com** (accusé ~48 h).

## Contrôles

```bash
export COMMANDER_MODE=read-only
export COMMANDER_API_KEY="long-random-secret"
export OLLAMA_BASE_URL=http://localhost:11434
```

Mitigations : scan d’injection, DLP, breakers, failover, isolation multi-tenant, npm audit.

[Gateway](/fr/architecture/security-gateway) · [Sandbox](/fr/architecture/sandbox)
