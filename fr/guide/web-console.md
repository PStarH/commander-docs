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

## Aperçu

![Console web Commander — mission board, topologie live, flux d’exécution, chat](/console-mockup.svg)

## Health checks

```bash
curl http://localhost:4000/health
curl http://localhost:4000/health/detailed
curl http://localhost:4000/readyz
curl http://localhost:4000/metrics
```

## Auth

Si `COMMANDER_API_KEY` est défini, les clients API (console comprise) doivent envoyer :

```http
Authorization: Bearer <COMMANDER_API_KEY>
```

Ne commitez jamais la clé. En cas de fuite, rotatez immédiatement.

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
| 401              | Même `COMMANDER_API_KEY` côté API et client                    |
| Pas de modèles   | Exporter une clé provider dans le shell qui a lancé `pnpm gui` |
| Conflit de ports | Arrêter les services sur 4000/5173/3000                        |

Plus : [Dépannage](/fr/guide/troubleshooting) · [Déploiement](/fr/deployment).

## Voir aussi

- [Démarrage rapide](/fr/guide/getting-started)
- [Installation](/fr/guide/installation)
- [Agent SDK](/fr/guide/sdk) (alternative programmatique)
