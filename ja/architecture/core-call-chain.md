# コア呼び出しチェーン

すべての Commander 実行は構造化パイプラインに従います。

## 1. 審議 (Deliberation)

```
CLI / HTTP / API → deliberation.ts → TaskComplexityAnalyzer
```

複雑度・依存・ドメインから実行戦略を決めます。

## 2. 努力スケーリング

```
effortScaler.ts  ← エージェント数 1–20
```

## 3. トポロジ・ルーティング

```
topologyRouter.ts  ← SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW
```

## 4. 原子化

```
atomizer.ts  ← ROMA 風のサブタスク分解
```

## 5. 実行

```
agentRuntime.execute
  → slot / tenant / storage
  → retry: LLM → tools → 5 gates → checkpoint
  → release / traces
```

## 6. 検証と合成

ゲート通過後に合成。失敗時は再試行・DLQ・補償。

## ローカルで追う

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo"
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

## 関連

- [アーキテクチャ概要](/ja/architecture/overview)  
- [マルチエージェント](/ja/architecture/multi-agent)  
- [エージェントランタイム](/ja/architecture/agent-runtime)  
- [検証](/ja/architecture/verification)  
