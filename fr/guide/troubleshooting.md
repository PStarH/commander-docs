# Dépannage

**Dépannage.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

> **CLI :** depuis le monorepo  
> `npx tsx packages/core/src/cliEntry.ts <command>`  
> Après build de `@commander/core` : `commander <command>`.

## Installation

### Échec de `pnpm install`

```bash
pnpm install
pnpm build
```

Depuis la **racine** du monorepo pour tous les workspaces.

### Erreurs TypeScript après install

```bash
pnpm build
npx tsc --noEmit
```

## Fournisseurs

### Provider not available

```bash
echo $OPENAI_API_KEY
npx tsx packages/core/src/cliEntry.ts doctor
```

La clé doit être exportée dans **ce** shell.

### Rate limited

- Attendre et réessayer (backoff auto)
- Plusieurs providers en fallback
- `export COMMANDER_MAX_CONCURRENCY=1`

### Timeout

- Réseau / provider
- Provider plus rapide (Groq, Together)
- `export COMMANDER_TIMEOUT_MS=120000`

## Exécution

### Hang

```bash
npx tsx packages/core/src/cliEntry.ts status
npx tsx packages/core/src/cliEntry.ts doctor
```

### Circuit breaker open

Attendre ~30s ou :

```bash
npx tsx packages/core/src/cliEntry.ts doctor --reset
```

### Mauvais résultats

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
npx tsx packages/core/src/cliEntry.ts plan "task"
```

## Docker

```bash
docker info
docker compose build --no-cache
```

## Debug

```bash
export COMMANDER_DEBUG=true
npx tsx packages/core/src/cliEntry.ts run "task" --stream
```

## Voir aussi

- [Démarrage rapide](/fr/guide/getting-started)
- [Installation](/fr/guide/installation)
- [Fournisseurs](/fr/guide/providers)
