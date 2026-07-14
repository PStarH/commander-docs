# Interactive Topology Explorer

**Interactive Topology Explorer.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 参照表

| | |
|--|--|
| **Agents** | 1 |
| **Best for** | FAQ, simple explain, one-shot transform |
| **Cost** | Lowest |
| **Risk** | No peer review |


## 主な節

### Decision tree

**Decision tree** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Topology cards

**Topology cards** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Quick chooser

**Quick chooser** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Force a topology

**Force a topology** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Related

**Related** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```
Is the task a single clear question with one owner?
  YES → SINGLE
  NO  ↓
Does work form a strict pipeline (A then B then C)?
  YES → CHAIN
  NO  ↓
Can specialists work in parallel then merge?
  YES → DISPATCH
  NO  ↓
Does a lead need to delegate and re-plan?
  YES → ORCHESTRATOR
  NO  ↓
Is quality / risk high enough to require critique?
  YES → REVIEW
  else → start with DISPATCH or ask `commander plan`
```
```bash
npx tsx packages/core/src/cliEntry.ts plan "what does this function do?"
# often → SINGLE
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
