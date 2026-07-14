# Installation

**Installation.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 참고 표

| Feature           | Setting                                     |
| ----------------- | ------------------------------------------- |
| CPU/Memory limits | 2 CPU / 4GB API, 0.5 CPU / 256MB web        |
| Logging           | JSON-file driver, 10MB max, 3 rotated files |
| Restart policy    | `always` (auto-restart)                     |
| Health checks     | 30s interval, 10s timeout, 5 retries        |
| Rate limiting     | Configurable per-tenant window/max          |
| Multi-tenancy     | Optional `TENANT_PROVIDER=simple`           |


## 주요 내용

### Prerequisites

운영 시 **Prerequisites** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/installation)를 보세요.

### Local development (recommended)

운영 시 **Local development (recommended)** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/installation)를 보세요.

### Docker

운영 시 **Docker** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/installation)를 보세요.

### Production (VM / VPS)

운영 시 **Production (VM / VPS)** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/installation)를 보세요.

### CI/CD

운영 시 **CI/CD** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/installation)를 보세요.

### Verify installation

운영 시 **Verify installation** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/installation)를 보세요.

### Next

운영 시 **Next** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/installation)를 보세요.

## 예제 (코드는 영어 유지)

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

```bash
# API :4000 + Web :5173 + open browser
pnpm gui
```

```bash
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

## 운영

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 관련

- [아키텍처 개요](/ko/architecture/overview)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [보안](/ko/guide/security)
- [빠른 시작](/ko/guide/getting-started)
