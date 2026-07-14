# Démarrage rapide

**Démarrage rapide.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

## Critères de réussite

Vous avez terminé lorsque **les trois** sont vrais :

1. `pnpm install` se termine sans erreur
2. Vous avez lancé une tâche et vu **délibération + topologie** (plan ou stream)
3. Le processus s’est terminé avec un résultat (ou une erreur claire de `doctor`, pas un blocage silencieux)

## Prérequis

- **Node.js** 18+ (22 recommandé)
- **pnpm** 8+ (9+ de préférence — monorepo workspaces)
- Une clé API LLM (OpenAI, Anthropic, DeepSeek, Groq, …)

> Utilisez **pnpm**, pas seulement npm : c’est un monorepo multi-paquets.

## Liste de 5 minutes

### 1. Cloner et installer

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

Optionnel mais recommandé :

```bash
pnpm -r build
```

### 2. Définir une clé API

```bash
export OPENAI_API_KEY=sk-...
# ou : ANTHROPIC_API_KEY / DEEPSEEK_API_KEY / GROQ_API_KEY / ...
```

Commander **détecte automatiquement** le fournisseur. Liste : [Fournisseurs](/fr/guide/providers).

### 3. Plan (sans risque)

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
```

Vous devez voir complexité, topologie et allocation d’agents **sans** muter de fichiers.

### 4. Run avec stream

```bash
npx tsx packages/core/src/cliEntry.ts run "explain the architecture of this repository" --stream
```

Pensées d’agents, appels d’outils et portes de qualité en live.

### 5. (Optionnel) Console web

```bash
pnpm gui
```

- API : `http://localhost:4000`
- Web : souvent `http://localhost:5173` (dev) ou `http://localhost:3000` (Docker)

Voir [Console web](/fr/guide/web-console).

### 6. (Optionnel) Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000
```

## Après build : binaire `commander` (optionnel)

Tant que npm n’est pas le chemin principal, préférez l’entrée monorepo :

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

Après un build local de core, un bin `commander` peut être disponible depuis le workspace :

```bash
pnpm --filter @commander/core build
commander run "audit this repo" --stream
```

## Si ça échoue

| Symptôme                         | Action                                                                 |
| -------------------------------- | ---------------------------------------------------------------------- |
| `Provider not available`         | `echo $OPENAI_API_KEY` — clé exportée dans **ce** shell. Puis `doctor` |
| `Cannot find module` / workspace | Depuis la racine avec **pnpm**, puis `pnpm install` et `pnpm -r build` |
| Hang / pas de sortie             | Essayer `plan` d’abord ; `COMMANDER_DEBUG=true` ; réseau / provider    |
| Rate limited                     | Attendre, `COMMANDER_MAX_CONCURRENCY=1`, ou une 2ᵉ clé                 |
| Circuit breaker open             | Attendre ~30s ou `doctor --reset`                                      |
| Offline only                     | Ollama : `export OLLAMA_BASE_URL=http://localhost:11434`               |

Guide complet : [Dépannage](/fr/guide/troubleshooting).

## Que s’est-il passé ?

1. **Classification** de la tâche (CODING / RESEARCH / ANALYSIS / FACTUAL)
2. **Choix** d’une topologie (SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW)
3. **Exécution** d’un ou plusieurs agents avec tools
4. **Vérification** via cinq portes de qualité

Détails : [Arbre de décision topologique](/fr/guide/usage/topology-decision-tree) · [Architecture](/fr/architecture/overview).

## Chemins suivants

| Objectif                      | Aller vers                                                             |
| ----------------------------- | ---------------------------------------------------------------------- |
| Recettes réelles              | [Cookbook](/fr/guide/cookbook/)                                        |
| Pourquoi pas le framework X ? | [Pourquoi Commander](/fr/guide/why-commander)                          |
| Embed TypeScript              | [Agent SDK](/fr/guide/sdk)                                             |
| Déployer sur une VM           | [Déploiement](/fr/deployment) · [Installation](/fr/guide/installation) |
| Référence CLI                 | [Commandes](/fr/guide/commands)                                        |
