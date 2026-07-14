# Enterprise Security Gateway

**Enterprise Security Gateway.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Layer | Name | Purpose |
|-------|------|---------|
| 1 | Zero-Trust Signature | Integrity verification + replay prevention |
| 2 | Authentication | API Key validation with timing-safe comparison |
| 3 | Rate Limiting | Global token bucket + tiered IP limits |
| 4 | Input Scanning | Content injection detection + input validation |
| 5 | Cost Pre-Check | Bill explosion prevention (pre-call estimation) |
| 6 | Request Processing | Business logic execution |
| 7 | Output Scanning | DLP data leak prevention + cost recording |


## Contenu principal

### 7-Layer Defense

En pratique, **7-Layer Defense** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/security-gateway) pour le détail exhaustif.

### Data Loss Prevention (DLP)

En pratique, **Data Loss Prevention (DLP)** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/security-gateway) pour le détail exhaustif.

### Capability Tokens

En pratique, **Capability Tokens** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/security-gateway) pour le détail exhaustif.

### Audit Chain Ledger

En pratique, **Audit Chain Ledger** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/security-gateway) pour le détail exhaustif.

### Agent Lineage

En pratique, **Agent Lineage** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/security-gateway) pour le détail exhaustif.

### Additional Security Components

En pratique, **Additional Security Components** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/security-gateway) pour le détail exhaustif.

### Plugin Permission Enforcement

En pratique, **Plugin Permission Enforcement** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/architecture/security-gateway) pour le détail exhaustif.

## Exemples (code inchangé)

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

## Opérations

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## Voir aussi

- [Vue d’architecture](/fr/architecture/overview)
- [Prêt production](/fr/architecture/production-readiness)
- [Sécurité](/fr/guide/security)
- [Démarrage rapide](/fr/guide/getting-started)
