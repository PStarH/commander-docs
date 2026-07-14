# Inspector Agent

**Inspector Agent.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 참고 표

| Metric | Warning | Critical |
|--------|---------|----------|
| Response Time | >1000ms | >5000ms |
| Error Rate | >5% | >20% |
| Memory Usage | >90% | >95% |
| Queue Depth | >100 | >500 |
| Success Rate | <80% | <50% |


## 주요 내용

### Types

운영 시 **Types** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/inspector-agent)를 보세요.

### API

운영 시 **API** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/inspector-agent)를 보세요.

### Auto-Detection Thresholds

운영 시 **Auto-Detection Thresholds** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/inspector-agent)를 보세요.

## 예제 (코드는 영어 유지)

```typescript
type IssueSeverity = 'critical' | 'high' | 'medium' | 'low' | 'info';
type IssueCategory = 'performance' | 'reliability' | 'security' | 'memory' | 'coordination' | 'configuration';

interface Issue {
  id: string;
  category: IssueCategory;
  severity: IssueSeverity;
  title: string;
  description: string;
  status: 'open' | 'acknowledged' | 'resolved' | 'ignored';
  suggestions: string[];
}

interface InspectionReport {
  id: string;
  timestamp: string;
  overallHealth: number;
  overallStatus: 'healthy' | 'degraded' | 'unhealthy';
  components: ComponentHealth[];
  openIssues: Issue[];
  recommendations: string[];
}
```

```typescript
const inspector = new InspectorAgent();

// Update component health status
inspector.updateComponent(
  name: string,
  status: 'healthy' | 'degraded' | 'unhealthy',
  score: number,
  metrics?: Record<string, number>
): void;

// Detect an issue
const issue = inspector.detectIssue(
  category: IssueCategory,
  severity: IssueSeverity,
  title: string,
  description: string,
  suggestions?: string[]
): Issue;

// Auto-detect issues from metrics
inspector.autoDetect(componentName: string, metrics: Record<string, number>): Issue[];

// Run full inspection
inspector.inspect(): InspectionReport;

// Get health trend
inspector.getHealthTrend(): {
  trend: 'improving' | 'declining' | 'stable';
  change: number;
  history: Array<{ timestamp: string; health: number }>;
};
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
