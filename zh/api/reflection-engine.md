# 反思引擎

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/api/reflection-engine)



Post-execution self-reflection and pattern detection for continuous improvement.

## Types


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

## API


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
