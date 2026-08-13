# Console web

**Console web.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

## Démarrer

### Dev (monorepo)

```bash
cd Commander
pnpm install
export OPENAI_API_KEY=sk-...   # ou un autre fournisseur
pnpm gui
```

| Service        | URL typique           |
| -------------- | --------------------- |
| API            | http://localhost:4000 |
| Web (Vite dev) | http://localhost:5173 |

`pnpm gui` démarre API + Web et tente d’ouvrir le navigateur.

### Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
```

| Service     | URL                   |
| ----------- | --------------------- |
| API         | http://localhost:4000 |
| Web (Nginx) | http://localhost:3000 |

## Ce que vous obtenez

| Zone           | Rôle                                                                                 |
| -------------- | ------------------------------------------------------------------------------------ |
| **Dashboard**  | Rapport de mission, tendances tokens, topologie live, roster d’agents, mission board |
| **Chat**       | Exécutions conversationnelles avec stream agent en temps réel                        |
| **Governance** | File d’approbation, politiques, journal d’audit                                      |
| **DLQ**        | Dead letter queue : inspecter + rejouer                                              |
| **Security**   | Vues conformité / posture (orientées ISO 42001 / NIST AI RMF)                        |
| **Execution**  | Flux d’exécution live, panneau de risque d’hallucination                             |
| **Agents**     | Roster + arbre de lignée                                                             |

Les libellés exacts évoluent avec le package `apps/web` — lisez ceci comme une **carte produit**, pas une spec pixel-perfect.

Routes en direct (package `apps/web`) : `/`, `/agents`, `/missions`, `/execution`, `/memory`, `/governance`, `/security`, `/slo`, `/chat`, `/dlq`, `/audit`, `/cost`, `/knowledge`, `/alerts`, `/onboarding`, `/users`, `/settings`, `/settings/sso`, `/workflows`, `/poc`, `/research`, et `/actions` (Action Gateway).

## Aperçu

![Console web Commander — mission board, topologie live, flux d’exécution, chat](/console-mockup.svg)

## Health checks

Serveur de santé ops — port par défaut `8081`, surchargeable via `COMMANDER_OPS_HEALTH_PORT` :

```bash
curl http://localhost:8081/health   # → 200 {"status":"ok"}
curl http://localhost:8081/ready    # → 200 (ready) / 503 (fail-closed)
```

Le client console utilise la base API sur `:4000` (défaut, `VITE_API_BASE_URL`).

## Auth

La console signe ses requêtes API avec un jeton bearer persisté dans `localStorage` sous `commander.auth.token`. Quand un jeton est présent, un interceptor fetch global ajoute :

```http
Authorization: Bearer <token>
```

Une réponse `401` efface le jeton stocké et notifie l'app pour se ré-authentifier. Ne commitez jamais les jetons ; rotatez-les en cas de fuite.

## Console vs CLI

| Utilisez la console quand…                     | Utilisez la CLI quand…            |
| ---------------------------------------------- | --------------------------------- |
| Vous voulez topologie visuelle et approbations | Scripts, CI, hôtes SSH only       |
| Déboguer de longs runs multi-agents            | `plan` / `run --stream` ponctuels |
| Ops (DLQ, audit)                               | Automatisation et packaging       |

## Dépannage

| Problème         | Action                                                         |
| ---------------- | -------------------------------------------------------------- |
| UI blanche       | API sur `:4000` ; CORS dans la console navigateur              |
| 401              | Ré-authentifiez-vous dans la console — le jeton stocké est effacé automatiquement |
| Pas de modèles   | Exporter une clé provider dans le shell qui a lancé `pnpm gui` |
| Conflit de ports | Arrêter les services sur 4000/5173/3000                        |

Plus : [Dépannage](/fr/guide/troubleshooting) · [Déploiement](/fr/deployment).

## Voir aussi

- [Démarrage rapide](/fr/guide/getting-started)
- [Installation](/fr/guide/installation)
- [Agent SDK](/fr/guide/sdk) (alternative programmatique)
