# Inspector Agent

**Inspector Agent.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| Metric | Warning | Critical |
|--------|---------|----------|
| Response Time | >1000ms | >5000ms |
| Error Rate | >5% | >20% |
| Memory Usage | >90% | >95% |
| Queue Depth | >100 | >500 |
| Success Rate | <80% | <50% |


## 主な節

### Types

**Types** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### API

**API** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Auto-Detection Thresholds

**Auto-Detection Thresholds** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

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

## 運用チェック

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 関連

- [アーキテクチャ概要](/ja/architecture/overview)
- [本番準備](/ja/architecture/production-readiness)
- [セキュリティ](/ja/guide/security)
- [クイックスタート](/ja/guide/getting-started)
