# Plan Mode

**Plan Mode.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 주요 내용

### Why Use Plan Mode

운영 시 **Why Use Plan Mode** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/usage/plan-mode)를 보세요.

### 사용법

운영 시 **Usage** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/usage/plan-mode)를 보세요.

### Plan Output

운영 시 **Plan Output** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/usage/plan-mode)를 보세요.

### Visual Indicator

운영 시 **Visual Indicator** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/usage/plan-mode)를 보세요.

## 예제 (코드는 영어 유지)

```bash
# Set plan mode
npx tsx packages/core/src/cliEntry.ts mode plan

# Then run any task
npx tsx packages/core/src/cliEntry.ts run "refactor the database layer"

# Or use the --plan flag for one-off plan mode
npx tsx packages/core/src/cliEntry.ts plan "implement search feature"
```

```
┃ → Deliberating task...
┃ → Complexity: HIGH (score: 72/100)
┃ → Topology: ORCHESTRATOR
┃ → Agents: 4 (1 lead + 3 specialists)
┃ → Provider: deepseek (fallback: openai → anthropic)
┃ → Token budget: 100,000
┃
┃ → Subtasks:
┃   1. Analyze existing database schema
┃   2. Design migration plan
┃   3. Implement changes (parallel: 2 agents)
┃   4. Verify and test
┃
┃ → Estimated duration: 45s
┃ → Total tools calls: ~12
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
