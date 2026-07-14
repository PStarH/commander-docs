# Gateway de sécurité

Défense en profondeur autour des agents, tools et données.

1. Auth / rate limit / tenant  
2. Validation d’entrée  
3. DLP / motifs sensibles  
4. Politique des tools (irréversibles bloquées ou approuvées)  
5. Sandbox d’exécution  
6. Scan des sorties (injection)  
7. Audit / hash chain  

## Opérateur

```bash
export COMMANDER_MODE=read-only
export COMMANDER_API_KEY="long-random-secret"
export COMMANDER_SECURITY_PROFILE=standard  # strict | standard | permissive | hardened
```

## Lié

- [Guide Sécurité](/fr/guide/security)  
- [Sandbox](/fr/architecture/sandbox)  
- [Multi-tenant](/fr/architecture/multi-tenancy)
