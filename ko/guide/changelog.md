# Changelog

Commander 아키텍처 구성 요소에 대한 한국어 문서입니다. monorepo 구현과 정렬됩니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 주요 내용

### v0.2.1-pre (Unreleased)

운영 시 **v0.2.1-pre (Unreleased)** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/changelog)를 보세요.

### v0.2.0 (2026-05-19)

운영 시 **v0.2.0 (2026-05-19)** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/changelog)를 보세요.

### v0.1.0 (2026-05-17)

운영 시 **v0.1.0 (2026-05-17)** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/changelog)를 보세요.

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
