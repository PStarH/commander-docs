# Core Call Chain

**Core Call Chain.** このページは Commander アーキテクチャの構成要素を説明します。monorepo に沿った日本語の運用ドキュメントで、コードブロックは英語のままです。

製品メトリクス: **25** プロバイダー · **5** トポロジ · **18** tools · **6700+** テスト。

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · ビルド後: `commander`

## 主な内容

### 1. Deliberation

運用では **1. Deliberation** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/architecture/core-call-chain)を参照してください。

### 2. Effort Scaling

運用では **2. Effort Scaling** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/architecture/core-call-chain)を参照してください。

### 3. Topology Routing

運用では **3. Topology Routing** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/architecture/core-call-chain)を参照してください。

### 4. Atomization

運用では **4. Atomization** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/architecture/core-call-chain)を参照してください。

### 5. Execution

運用では **5. Execution** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/architecture/core-call-chain)を参照してください。

### 6. Quality Gates

運用では **6. Quality Gates** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/architecture/core-call-chain)を参照してください。

### 7. Completion

運用では **7. Completion** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/architecture/core-call-chain)を参照してください。

## 例（コードは英語のまま）

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

## 運用

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
