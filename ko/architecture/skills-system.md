# Skills System

**Skills System.** Commander monorepo 구성 요소에 대한 한국어 운영 문서입니다. 코드·식별자는 영어를 유지하며, CLI는 `npx tsx packages/core/src/cliEntry.ts` 를 우선합니다. 제품 지표: 25 프로바이더 · 5 토폴로지 · 18 tools · 6700+ 테스트.

## 참고 표

| Metric | Description |
|--------|-------------|
| **Effectiveness** | How often using the skill improves outcomes |
| **Precision** | How accurately the skill guides the agent |
| **Completeness** | Whether the skill covers all necessary aspects |
| **Safety** | No harmful or insecure instructions |
| **Freshness** | How recently the skill was updated |


## 주요 섹션

### Architecture

**Architecture** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### What is a Skill?

**What is a Skill?** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Managing Skills

**Managing Skills** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Skill Quality

**Skill Quality** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Security Scanning

**Security Scanning** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

### Creating a Skill

**Creating a Skill** 는 monorepo 구현과 품질 게이트·DLQ·서킷 브레이커와 함께 동작합니다. 전체 명세는 영문 소스와 코드(`packages/core`)를 참고하세요.

## 예제

```
skills/
├── skillManager.ts       ← Skill lifecycle management
├── skillCurator.ts       ← Skill curation and organization
├── skillInjector.ts      ← Inject skills into agent prompts
├── skillStore.ts         ← Persistent skill storage
├── skillQualityScorer.ts ← Quality scoring for skills
├── skillSecurityScanner.ts ← Security scanning for skill content
├── skillViewTool.ts      ← Tool for viewing/loading skills
├── metaLearnerBridge.ts  ← Bridge to MetaLearner for skill optimization
├── types.ts              ← Shared types
└── index.ts              ← Public exports
```
```bash
# List available skills
npx tsx packages/core/src/cliEntry.ts skill list

# View a skill's content
npx tsx packages/core/src/cliEntry.ts skill view <skill-name>

# Create a new skill
npx tsx packages/core/src/cliEntry.ts skill create <skill-name>

# Pin a skill (always loaded)
npx tsx packages/core/src/cliEntry.ts skill pin <skill-name>
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
