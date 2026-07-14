# Reflection Engine

**Reflection Engine.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 주요 내용

### Types

운영 시 **Types** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/reflection-engine)를 보세요.

### API

운영 시 **API** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/reflection-engine)를 보세요.

## 예제 (코드는 영어 유지)

```typescript
type ReflectionType = 'post_execution' | 'pre_planning' | 'error_analysis' | 'pattern_detection';

interface Reflection {
  id: string;
  type: ReflectionType;
  context: string;
  question: string;
  answer?: string;
  quality: number;         // 0-1
  actionable: boolean;
  insights: string[];
  recommendations: string[];
  relatedOutcome?: 'success' | 'partial' | 'failure';
}

interface ReflectionStats {
  totalSessions: number;
  averageQuality: number;
  patternCount: number;
  topPatterns: ReflectionPattern[];
  improvementTrend: 'improving' | 'declining' | 'stable';
}
```

```typescript
const engine = new ReflectionEngine();

// Start/complete session
const sessionId = engine.startSession(taskId: string): string;
engine.completeSession(sessionId: string, outcome?: 'success' | 'partial' | 'failure'): void;

// Add reflection
const reflection = engine.addReflection(
  sessionId: string,
  context: string,
  question: string,
  answer?: string
): Reflection;

// Get recommendations
engine.getRecommendations(reflectionId?: string): string[];

// Generate report
engine.generateReport(sessionId: string): string;
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
