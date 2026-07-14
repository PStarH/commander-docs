# リフレクションエンジン

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/api/reflection-engine)



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
