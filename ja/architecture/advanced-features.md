# 高度なエンジン機能

Commander は高度な実行制御のためのエンジン部品をいくつか含みます。

## Speculative Executor

複数パスを並列実行し最良を選びます。

```typescript
import { SpeculativeExecutor } from '@commander/core';

const executor = new SpeculativeExecutor();
const results = await executor.executeSpeculative(task, {
  strategies: [
    { provider: 'deepseek', temperature: 0.3 },
    { provider: 'openai', temperature: 0.5 },
    { provider: 'anthropic', temperature: 0.7 },
  ],
  selector: 'quality',
});
```

## Entropy Gater

エントロピーで低信頼出力を落とします。

```typescript
import { EntropyGater } from '@commander/core';

const gater = new EntropyGater({ threshold: 0.7 });
const filtered = gater.filter(agentOutputs);
```

## Cycle Detector

タスクグラフの循環依存を検出・解消します。

```typescript
import { CycleDetector } from '@commander/core';

const detector = new CycleDetector();
if (detector.hasCycle(taskGraph)) {
  const broken = detector.breakCycles(taskGraph);
}
```

## Context Window Manager

トークン予算内に収めるようメッセージを圧縮・スライディング。`ContextCompactor` / `TokenGovernor` と連携。

## いつ使うか

通常は CLI/SDK の `run` で十分。カスタム・プランナーや研究計測で上記を直接組み合わせます。

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --stream
```

## 関連

- [投機実行](/ja/architecture/speculative-execution)  
- [エージェントランタイム](/ja/architecture/agent-runtime)  
- [検証](/ja/architecture/verification)  
