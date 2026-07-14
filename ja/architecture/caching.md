# Caching

**Caching.** Commander monorepo の構成要素に関する日本語運用ドキュメントです。コードと識別子は英語のまま。CLI は `npx tsx packages/core/src/cliEntry.ts` を優先。製品メトリクス: 25 プロバイダー · 5 トポロジ · 18 tools · 6700+ テスト。

## 主な節

### Cache Layers

**Cache Layers** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### ToolResultCache

**ToolResultCache** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### SemanticCache

**SemanticCache** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### SingleFlightRequestCache

**SingleFlightRequestCache** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

### Integration

**Integration** は monorepo 実装と品質ゲート・DLQ・サーキットブレーカーと連動します。詳細は英語ソースと `packages/core` を参照してください。

## 例

```
Tool Call
  │
  ├─ SingleFlightRequestCache  ── Deduplicates concurrent identical requests
  │   (First request executes, subsequent wait for result)
  │
  ├─ ToolResultCache           ── SHA-256 exact-match cache
  │   (Deterministic tools: read file, search code, etc.)
  │
  └─ SemanticCache             ── Similarity-based semantic cache
      (Non-deterministic LLM calls with similar meaning)
```
```typescript
const cache = new ToolResultCache({ basePath: '/data/cache' });

const key = cache.hashKey(tenantId, toolName, args);
const cached = await cache.get(key);

if (cached) return cached;

const result = await executeTool(toolName, args);
await cache.set(key, result);
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
