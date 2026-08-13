# Contributing to the docs

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/guide/contributing)



Thank you for improving Commander documentation.

## Repos


| Repo | Role |
|------|------|
| [Commander](https://github.com/PStarH/Commander) | Product, CLI, SDK, tests |
| [commander-docs](https://github.com/PStarH/commander-docs) | This VitePress site |

## Local docs dev


```bash
git clone https://github.com/PStarH/commander-docs.git
cd commander-docs
npm install
npm run dev      # http://localhost:5173/commander-docs/
npm run check    # content guards
npm run build
```

## Content rules


1. **Metrics:** `25 providers` · `5 topologies` · `18 built-in tools` · `6700+ tests`  
2. **CLI from source:** `npx tsx packages/core/src/cliEntry.ts …`  
3. **CLI after build:** `commander …`  
4. **Vue internal links:** always `withBase()` (GH Pages base `/commander-docs/`)  
5. **themeConfig.logo:** `/logo.svg` only — never hardcode `/commander-docs/`  
6. **Localhost URLs** in install docs are fine; CI allows them as dead-link exceptions  

## i18n


- English is the source of truth under `/guide`, `/architecture`, `/api`  
- Chinese entry path: `/zh/` (Quick Start, Why, FAQ, cookbook samples)  
- When you change EN quick-start commands, update `zh/guide/getting-started.md` if applicable  

## PR checklist


- [ ] `npm run check` passes  
- [ ] `npm run build` passes  
- [ ] No new `cli.ts` / wrong provider counts / 17-tools strings  
- [ ] Screenshots or demos use accurate product claims  

## 安全


Do **not** open public issues for vulnerabilities. See [Security](/zh/guide/security).

## Product code contributions


Use the main [Commander](https://github.com/PStarH/Commander) repository for runtime, tools, and providers. Docs-only changes belong here.
