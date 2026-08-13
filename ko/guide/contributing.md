# Contributing to the docs

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/guide/contributing)



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

## 보안


Do **not** open public issues for vulnerabilities. See [Security](/ko/guide/security).

## Product code contributions


Use the main [Commander](https://github.com/PStarH/Commander) repository for runtime, tools, and providers. Docs-only changes belong here.
