# Démarrage rapide

Faites tourner Commander en environ cinq minutes. Une seule clé API. Pas de constructeur de graphes. Pas de YAML.

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

Commander **détecte automatiquement** le fournisseur. Liste complète : [Fournisseurs](/fr/guide/providers).

### 3. Plan (sans risque)

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
```

Vous devriez voir complexité, topologie et allocation d’agents **sans modifier de fichiers**.

### 4. Exécuter avec stream

```bash
npx tsx packages/core/src/cliEntry.ts run "explain the architecture of this repository" --stream
```

Vous devriez voir en direct pensées d’agents, appels d’outils et portes de qualité.

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

## Après le build : binaire `commander`

```bash
pnpm --filter @commander/core build
commander run "audit this repo" --stream
```

## En cas d’échec

| Symptôme | Correctif |
|----------|-----------|
| `Provider not available` | `echo $OPENAI_API_KEY` — la clé doit être exportée dans **ce** shell. Puis `npx tsx packages/core/src/cliEntry.ts doctor` |
| `Cannot find module` / workspace | Depuis la racine du dépôt avec **pnpm**, puis `pnpm install` et `pnpm -r build` |
| Blocage / pas de sortie | Essayez `plan` d’abord ; `COMMANDER_DEBUG=true` ; réseau / fournisseur |
| Rate limit | Attendez, baissez la concurrence (`COMMANDER_MAX_CONCURRENCY=1`) ou ajoutez une 2ᵉ clé |
| Circuit breaker ouvert | Attendez ~30 s ou `npx tsx packages/core/src/cliEntry.ts doctor --reset` |
| Hors ligne uniquement | Ollama : `export OLLAMA_BASE_URL=http://localhost:11434` |

Guide complet : [Dépannage](/fr/guide/troubleshooting).

## Que s’est-il passé ?

1. **Classification** de la tâche (CODING / RESEARCH / ANALYSIS / FACTUAL)  
2. **Choix** d’une topologie (SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW)  
3. **Exécution** d’un ou plusieurs agents avec outils  
4. **Vérification** via cinq portes de qualité  

Détails : [Arbre de décision des topologies](/fr/guide/usage/topology-decision-tree) · [Architecture](/fr/architecture/overview).

## Suite

| Objectif | Aller vers |
|----------|------------|
| Recettes concrètes | [Cookbook](/fr/guide/cookbook/) |
| Pourquoi pas le framework X ? | [Pourquoi Commander](/fr/guide/why-commander) |
| Intégrer en TypeScript | [Agent SDK](/fr/guide/sdk) |
| Déployer sur une VM | [Déploiement](/fr/deployment) · [Installation](/fr/guide/installation) |
| Référence CLI | [Commandes](/fr/guide/commands) |
