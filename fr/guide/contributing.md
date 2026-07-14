# Contributing to the docs

**Contributing to the docs.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Référence

| Repo | Role |
|------|------|
| [Commander](https://github.com/PStarH/Commander) | Product, CLI, SDK, tests |
| [commander-docs](https://github.com/PStarH/commander-docs) | This VitePress site |


## Contenu principal

### Repos

En pratique, **Repos** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/contributing) pour le détail exhaustif.

### Local docs dev

En pratique, **Local docs dev** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/contributing) pour le détail exhaustif.

### Content rules

En pratique, **Content rules** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/contributing) pour le détail exhaustif.

### i18n

En pratique, **i18n** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/contributing) pour le détail exhaustif.

### PR checklist

En pratique, **PR checklist** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/contributing) pour le détail exhaustif.

### Security

En pratique, **Security** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/contributing) pour le détail exhaustif.

### Product code contributions

En pratique, **Product code contributions** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/contributing) pour le détail exhaustif.

## Exemples (code inchangé)

```bash
git clone https://github.com/PStarH/commander-docs.git
cd commander-docs
npm install
npm run dev      # http://localhost:5173/commander-docs/
npm run check    # content guards
npm run build
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
