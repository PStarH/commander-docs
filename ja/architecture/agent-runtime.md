# エージェントランタイム

Commander の心臓部である実行エンジンです。`AgentRuntime` は単一エージェントのライフサイクル全体を管理します。LLM 呼び出し、ツール実行、検証、チェックポイント、再試行 — すべて設定可能なトークン・ステップ予算の中で。

## 構造

```
AgentRuntime.execute(ctx)
  │
  ├─ acquireSlot()        ← 同時実行セマフォ
  ├─ [Tenant check]       ← rate limit + 同時実行クォータ
  ├─ resolve storage      ← テナントスコープのメモリ + キャッシュ
  │
  ├─ [Retry loop: 0..maxRetries]
  │   ├─ callWithTimeout()       ← LLM プロバイダー
  │   ├─ [Tool execution loop]
  │   │   ├─ planner.plan()      ← 依存関係を意識した計画
  │   │   ├─ executeTool()       ← StepErrorBoundary → tool.execute()
  │   │   └─ cache.set()
  │   ├─ verification.check()    ← 5 品質ゲート
  │   └─ checkpoint()            ← atomic 保存
  │
  ├─ releaseSlot()
  └─ flush traces + samples
```

## メインループ

1. **スロット取得** — 最大同時 run を超えない
2. **テナント検証** — rate limit・同時実行クォータ
3. **LLM 呼び出し** — タイムアウト設定可
4. **ツール実行** — `ToolPlanner` が依存を解析し並列可能なものを同時実行
5. **検証** — 5 ゲート失敗時は再試行
6. **チェックポイント** — 各ステップで atomic 永続化
7. **トレーシング** — 実行トレースと LLM サンプルを flush

## 主要コンポーネント

| コンポーネント       | ファイル                        | 役割                          |
| -------------------- | ------------------------------- | ----------------------------- |
| `AgentRuntime`       | `runtime/agentRuntime.ts`       | メインループ                  |
| `ToolPlanner`        | `runtime/toolPlanner.ts`        | 依存関係付きツール計画        |
| `ToolOrchestrator`   | `runtime/toolOrchestrator.ts`   | 計画の実行                    |
| `StepErrorBoundary`  | `runtime/stepErrorBoundary.ts`  | ステップ単位 skip/retry/abort |
| `StepTimeoutManager` | `runtime/stepTimeoutManager.ts` | ステップタイムアウト          |
| `ContextCompactor`   | `runtime/contextCompactor.ts`   | トークン意識の圧縮            |
| `ContextWindow`      | `runtime/contextWindow.ts`      | スライディングウィンドウ      |
| `TokenGovernor`      | `runtime/tokenGovernor.ts`      | トークン予算                  |
| `CycleDetector`      | `runtime/cycleDetector.ts`      | 無限ループ検出                |
| `ToolOutputManager`  | `runtime/toolOutputManager.ts`  | ツール出力の予算管理          |

## 設定

```typescript
interface AgentRuntimeConfig {
  maxStepsPerRun: number;
  maxRetries: number;
  timeoutMs: number;
  maxConcurrency: number;
  budgetHardCapTokens: number;
}
```

## 実行計画

ツールは LLM 応答順そのままでありません。独立ツールは並列、依存ツールは前提の後に順次。循環依存は実行前に検出します。

## 関連

- [検証パイプライン](/ja/architecture/verification)
- [マルチエージェント](/ja/architecture/multi-agent)
- [コア呼び出しチェーン](/ja/architecture/core-call-chain)
