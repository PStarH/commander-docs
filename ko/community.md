# Community

**Community.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 참고 표

| Channel | Status | Link |
|---------|--------|------|
| **GitHub** | Live | [github.com/PStarH/Commander](https://github.com/PStarH/Commander) — issues, PRs, stars |
| **Discussions** | Use GitHub Issues | Feature ideas and Q&A via [Issues](https://github.com/PStarH/Commander/issues) |
| **Docs** | Live | This site + PRs on [commander-docs](https://github.com/PStarH/commander-docs) |
| **Discord / Twitter** | Planned | Not live yet — follow the repo for announcements |


## 주요 내용

### Get involved

운영 시 **Get involved** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/community)를 보세요.

### Contributing

운영 시 **Contributing** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/community)를 보세요.

### Roadmap

운영 시 **Roadmap** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/community)를 보세요.

### Trust signals

운영 시 **Trust signals** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/community)를 보세요.

### Contribute docs

운영 시 **Contribute docs** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/community)를 보세요.

### Showcase

운영 시 **Showcase** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/community)를 보세요.

### Stay updated

운영 시 **Stay updated** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/community)를 보세요.

### Docs for AI assistants

운영 시 **Docs for AI assistants** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/community)를 보세요.

## 예제 (코드는 영어 유지)

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
# Prefer project scripts when available:
pnpm test:all   # or: cd packages/core && npx tsx --test tests/*.test.ts
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
