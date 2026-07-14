# Contribuir a la documentación

## Repos

| Repo | Rol |
|------|-----|
| [Commander](https://github.com/PStarH/Commander) | Producto |
| [commander-docs](https://github.com/PStarH/commander-docs) | Este sitio VitePress |

## Local

```bash
git clone https://github.com/PStarH/commander-docs.git
cd commander-docs
npm install
npm run dev
npm run check
npm run build
```

## Reglas de contenido

1. Métricas: **25** providers · **5** topologías · **18** tools · **6700+** tests  
2. CLI monorepo: `npx tsx packages/core/src/cliEntry.ts`  
3. Vue: siempre `withBase()`  
4. Logo: `/logo.svg` sin base duplicada  
5. **Prosa nativa por locale** — prohibido inglés + banner  

## i18n

Locales: `en` (fuente), `zh`, `ja`, `ko`, `es`, `fr`.  
Al cambiar quick start EN, actualiza las entradas locales.

## PR

- [ ] `npm run check`  
- [ ] `npm run build`  
- [ ] Sin `cli.ts` ni métricas viejas
