# Contributing to the docs

**Contributing to the docs.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 참고 표

| Repo | Role |
|------|------|
| [Commander](https://github.com/PStarH/Commander) | Product, CLI, SDK, tests |
| [commander-docs](https://github.com/PStarH/commander-docs) | This VitePress site |


## 주요 내용

### Repos

운영 시 **Repos** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/contributing)를 보세요.

### Local docs dev

운영 시 **Local docs dev** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/contributing)를 보세요.

### Content rules

운영 시 **Content rules** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/contributing)를 보세요.

### i18n

운영 시 **i18n** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/contributing)를 보세요.

### PR checklist

운영 시 **PR checklist** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/contributing)를 보세요.

### Security

운영 시 **Security** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/contributing)를 보세요.

### Product code contributions

운영 시 **Product code contributions** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/contributing)를 보세요.

## 예제 (코드는 영어 유지)

```bash
git clone https://github.com/PStarH/commander-docs.git
cd commander-docs
npm install
npm run dev      # http://localhost:5173/commander-docs/
npm run check    # content guards
npm run build
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
