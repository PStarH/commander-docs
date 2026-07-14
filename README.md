# Commander Docs

Documentation site for [Commander](https://github.com/PStarH/Commander) — multi-agent orchestration engine.

**Live:** [https://pstarh.github.io/commander-docs/](https://pstarh.github.io/commander-docs/)

## Stack

- [VitePress](https://vitepress.dev/) 1.6
- Custom home page (Vue + GSAP)
- Deployed to GitHub Pages (`base: /commander-docs/`)

## Develop

```bash
npm install
npm run dev      # http://localhost:5173/commander-docs/
```

## Build & preview

```bash
npm run build
npm run preview
```

## Deploy

Push to `master` triggers [.github/workflows/deploy.yml](.github/workflows/deploy.yml) → GitHub Pages.

```bash
git checkout master
git add -A && git commit -m "docs: ..."
git push origin master
```

## Structure

```
guide/           Getting started, usage, advanced, SDK
architecture/    Runtime, reliability, security, systems
api/             Orchestration component reference
deployment.md    Docker / VM / production
community.md     Contributing & roadmap
.vitepress/      Config + theme
```

## Content rules

- **Metrics:** 25 providers · 5 topologies · 18 built-in tools · 6700+ tests (match product README / `@commander/core`)
- **CLI from source:** `npx tsx packages/core/src/cliEntry.ts …`
- **CLI after build:** `commander …`
- **Internal links in Vue:** always use `withBase()` — raw `/guide/...` breaks on GH Pages
- **themeConfig.logo:** `/logo.svg` (VitePress prefixes `base` automatically — do not hardcode `/commander-docs/`)

## Related

- Product: https://github.com/PStarH/Commander
- Docs repo: https://github.com/PStarH/commander-docs
