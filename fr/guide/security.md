# Sécurité

**Sécurité.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

## Signaler une vulnérabilité

**N’ouvrez pas d’issue GitHub publique pour un bug de sécu.**

Envoyez un mail à **sampan090611@gmail.com** avec :

- Type et impact
- Chemins / commits
- Étapes de reproduction
- PoC si possible

Accusé de réception sous **48 h** (voir [SECURITY.md](https://github.com/PStarH/Commander/blob/master/SECURITY.md) du produit).

## Modèle de menace (résumé)

| Menace                  | Mitigations                                                 |
| ----------------------- | ----------------------------------------------------------- |
| Injection prompt / tool | Scan des sorties tools, sanitizers, portes de réversibilité |
| Fuite de secrets        | DLP, logs structurés sans secrets                           |
| Agents incontrôlés      | Modes d’approbation, budgets tokens, timeouts, breakers     |
| Panne / abus provider   | Failover, rate limits, quotas tenant                        |
| Fuite inter-tenant      | Isolation storage / mémoire / cache / rate limits           |
| Supply chain            | CI npm audit ; pas de clés dans git                         |

## Contrôles à configurer

### 1. Modes d’approbation

| Mode        | Quand                         |
| ----------- | ----------------------------- |
| `plan`      | Aperçu seul                   |
| `read-only` | Analyse / audit               |
| `suggest`   | Humain approuve les écritures |
| `auto-edit` | Dev local de confiance        |
| `full-auto` | CI avec revue PR              |

```bash
export COMMANDER_MODE=read-only
```

### 2. Auth API

```bash
export COMMANDER_API_KEY="long-random-secret"
```

Bearer obligatoire. N’exposez pas `:4000` sans TLS + auth.

### 3. Binding réseau

API plutôt localhost. En prod : TLS et auth sur le reverse proxy ([Déploiement](/fr/deployment)).

### 4. Code sensible

Préférez **Ollama / vLLM** :

```bash
export OLLAMA_BASE_URL=http://localhost:11434
```

### 5. Multi-tenant prod

Activer provider tenant et quotas — [Multi-tenancy](/fr/architecture/multi-tenancy).

## Benchmarks sécu (monorepo)

```bash
pnpm benchmark:redteam
pnpm benchmark:agentdojo
```

Voir [Benchmarks](/fr/guide/benchmarks).

## Voir aussi

- [Production readiness](/fr/architecture/production-readiness)
- [Console web](/fr/guide/web-console)
- [FAQ](/fr/guide/faq)
