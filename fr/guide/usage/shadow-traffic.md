# Shadow Traffic

**Shadow Traffic.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Field | Default | Description |
|-------|---------|-------------|
| `enabled` | `false` | Enable shadow proxy |
| `endpoint` | `http://localhost:9999` | Shadow runner URL |
| `sampleRate` | `0.1` | Fraction of requests to mirror (0–1) |
| `scrubPii` | `true` | Strip PII before forwarding |
| `ignoreFields` | `["Authorization", "x-api-key", ...]` | Headers to always redact |
| `diffMode` | `status_cost_latency` | What to compare: `status_cost_latency` or `full_output` |
| `timeoutMs` | `5000` | Shadow request timeout |


## Contenu principal

### Use Cases

En pratique, **Use Cases** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/usage/shadow-traffic) pour le détail exhaustif.

### Quick Start

En pratique, **Quick Start** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/usage/shadow-traffic) pour le détail exhaustif.

### Configuration

En pratique, **Configuration** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/usage/shadow-traffic) pour le détail exhaustif.

### Drift Detection

En pratique, **Drift Detection** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/usage/shadow-traffic) pour le détail exhaustif.

### PII Scrubbing

En pratique, **PII Scrubbing** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/usage/shadow-traffic) pour le détail exhaustif.

### Troubleshooting

En pratique, **Troubleshooting** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/usage/shadow-traffic) pour le détail exhaustif.

### Programmatic API

En pratique, **Programmatic API** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/usage/shadow-traffic) pour le détail exhaustif.

## Exemples (code inchangé)

```bash
cat > .commander/shadow-config.json <<EOF
{
  "enabled": true,
  "endpoint": "http://localhost:9999",
  "sampleRate": 0.1,
  "scrubPii": true,
  "diffMode": "status_cost_latency",
  "timeoutMs": 5000
}
EOF
```

```bash
npx tsx packages/core/src/cli/commands/shadow.ts runner --port=9999 &
```

```bash
export COMMANDER_SHADOW_ENABLED=true
npx tsx packages/core/src/cli/index.ts serve
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
