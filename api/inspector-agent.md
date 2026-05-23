# Inspector Agent

System health monitoring and issue detection across all Commander components.

## Types

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

## API

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

## Auto-Detection Thresholds

| Metric | Warning | Critical |
|--------|---------|----------|
| Response Time | >1000ms | >5000ms |
| Error Rate | >5% | >20% |
| Memory Usage | >90% | >95% |
| Queue Depth | >100 | >500 |
| Success Rate | <80% | <50% |
