# Cookbook

**Cookbook.** Commander monorepo 구성 요소에 대한 한국어 운영 문서입니다. 코드·식별자는 영어를 유지하며, CLI는 `npx tsx packages/core/src/cliEntry.ts` 를 우선합니다. 제품 지표: 25 프로바이더 · 5 토폴로지 · 18 tools · 6700+ 테스트.

## 참고 표

| Recipe | Time | What you practice |
|--------|------|-------------------|
| [Security audit a repo](/guide/cookbook/security-audit) | ~10 min | DISPATCH-style analysis, streaming, gates |
| [Refactor a module safely](/guide/cookbook/refactor-module) | ~15 min | Plan mode → run → review |
| [CI full-auto lint fix](/guide/cookbook/ci-full-auto) | ~15 min | Non-interactive mode, exit codes |


## 주요 섹션

### Conventions

**Conventions** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

## 예제

```bash
# Source checkout
npx tsx packages/core/src/cliEntry.ts <command>

# After building @commander/core
commander <command>
```

## 운영 체크

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
