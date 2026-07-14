# Core Call Chain

**Core Call Chain.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 주요 내용

### 1. Deliberation

운영 시 **1. Deliberation** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/architecture/core-call-chain)를 보세요.

### 2. Effort Scaling

운영 시 **2. Effort Scaling** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/architecture/core-call-chain)를 보세요.

### 3. Topology Routing

운영 시 **3. Topology Routing** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/architecture/core-call-chain)를 보세요.

### 4. Atomization

운영 시 **4. Atomization** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/architecture/core-call-chain)를 보세요.

### 5. Execution

운영 시 **5. Execution** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/architecture/core-call-chain)를 보세요.

### 6. Quality Gates

운영 시 **6. Quality Gates** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/architecture/core-call-chain)를 보세요.

### 7. Completion

운영 시 **7. Completion** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/architecture/core-call-chain)를 보세요.

## 예제 (코드는 영어 유지)

```bash
CLI / HTTP / API
  │
  ├─ deliberation.ts     ← "What kind of task is this?"
  │   └─ TaskComplexityAnalyzer
```

```bash
  ├─ effortScaler.ts     ← "How many agents?"
```

```bash
  ├─ topologyRouter.ts   ← "Which topology fits?"
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
