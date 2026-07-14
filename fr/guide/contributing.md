# Contribuer à la documentation

## Repos

| Repo | Rôle |
|------|------|
| [Commander](https://github.com/PStarH/Commander) | Produit |
| [commander-docs](https://github.com/PStarH/commander-docs) | Site VitePress |

## Local

```bash
git clone https://github.com/PStarH/commander-docs.git
cd commander-docs
npm install
npm run dev
npm run check
npm run build
```

## Règles

1. Métriques : **25** providers · **5** topologies · **18** tools · **6700+** tests  
2. CLI monorepo : `npx tsx packages/core/src/cliEntry.ts`  
3. Vue : toujours `withBase()`  
4. Logo : `/logo.svg` sans double base  
5. **Prose native par locale** — interdit : anglais + bannière  

Locales : `en`, `zh`, `ja`, `ko`, `es`, `fr`.

[Communauté](/fr/community)
