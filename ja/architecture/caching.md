# キャッシュ

Commander は LLM 呼び出しを減らし、応答を速くし、重複計算を防ぐために **多層キャッシュ** を持ちます。すべてのキャッシュは **テナント単位で隔離** されます。

## キャッシュ層

```
Tool Call
  │
  ├─ SingleFlightRequestCache  ── 同一の同時リクエストを重複排除
  │   (最初だけ実行、他は結果待ち)
  │
  ├─ ToolResultCache           ── SHA-256 完全一致
  │   (決定的ツール: ファイル読み、コード検索など)
  │
  └─ SemanticCache             ── 意味類似キャッシュ
      (意味が近い非決定的 LLM 呼び出し)
```

## ToolResultCache

キーは `(tenantId + tool + args)` の SHA-256 です。

```typescript
const cache = new ToolResultCache({ basePath: '/data/cache' });

const key = cache.hashKey(tenantId, toolName, args);
const cached = await cache.get(key);

if (cached) return cached;

const result = await executeTool(toolName, args);
await cache.set(key, result);
```

- 決定的ツール（読み取り、検索、grep）向け  
- テナントキー隔離でクロステナント漏洩を防止  
- TTL 設定可  
- クォータ超過時は LRU 追い出し  

## SemanticCache

非決定的処理（LLM）には埋め込み類似度を使います。

```typescript
const semanticCache = new SemanticCache({ similarityThreshold: 0.95 });

const similar = await semanticCache.find(input, tenantId);
if (similar) return similar.result;

await semanticCache.store(input, result, tenantId);
```

- コサイン類似度  
- 閾値↑ = 誤ヒット↓ / ヒット↓ · 閾値↓ = ヒット↑  
- TTL + LRU  

## SingleFlightRequestCache

同一キーの **同時重複実行**（thundering herd）を防ぎます。

```typescript
const singleFlight = new SingleFlightRequestCache();

const [a, b, c] = await Promise.all([
  singleFlight.execute('key-1', () => expensiveOperation()),
  singleFlight.execute('key-1', () => expensiveOperation()),
  singleFlight.execute('key-1', () => expensiveOperation()),
]);
// expensiveOperation は 1 回だけ
```

複数エージェントが同時に同じツール/LLM を叩くときに特に有効です。

## 統合順

1. **SingleFlight** — 進行中の重複排除  
2. **ToolResultCache** — 完全一致  
3. **SemanticCache** — 類似意味  
4. すべてミスのときだけ実実行  

パッケージは monorepo `packages/core` 前提。導入は clone + `pnpm install` が主経路です。

## 関連

- [マルチテナント](/ja/architecture/multi-tenancy)  
- [エージェントランタイム](/ja/architecture/agent-runtime)  
- [ツール](/ja/architecture/tools)  
