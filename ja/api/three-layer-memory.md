# Three-Layer Memory

**Three-Layer Memory.** このページは Commander アーキテクチャの構成要素を説明します。monorepo に沿った日本語の運用ドキュメントで、コードブロックは英語のままです。

製品メトリクス: **25** プロバイダー · **5** トポロジ · **18** tools · **6700+** テスト。

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · ビルド後: `commander`

## 参照表

| Layer | Max Entries | Max Memory | Decay |
|-------|-------------|------------|-------|
| Working | 50 | 100KB | None |
| Episodic | 500 | 500KB | Time-based |
| Long-term | 10000 | 5MB | None |


## 主な内容

### Types

運用では **Types** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/api/three-layer-memory)を参照してください。

### API

運用では **API** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/api/three-layer-memory)を参照してください。

### Layer Configuration

運用では **Layer Configuration** を品質ゲート・DLQ・サーキットブレーカーと併用します。ソースは monorepo、詳細は[英語リファレンス](/api/three-layer-memory)を参照してください。

## 例（コードは英語のまま）

```typescript
type MemoryLayer = 'working' | 'episodic' | 'longterm';

interface MemoryEntry {
  id: string;
  layer: MemoryLayer;
  content: string;
  context: string;
  importance: number;      // 0-1
  createdAt: string;
  lastAccessedAt: string;
  accessCount: number;
  decayScore: number;
  tags: string[];
  metadata: Record<string, any>;
}

interface MemoryQuery {
  layer?: MemoryLayer;
  keywords?: string[];
  context?: string;
  importanceThreshold?: number;
  limit?: number;
  since?: string;
}
```

```typescript
const memory = new ThreeLayerMemory(config?: Partial<Record<MemoryLayer, LayerConfig>>);

// Add memory
const entry = memory.add(
  content: string,
  layer: MemoryLayer,
  context?: string,
  importance?: number,
  tags?: string[],
  metadata?: Record<string, any>
): MemoryEntry;

// Query memories
memory.query(query: MemoryQuery): MemoryEntry[];

// Promote to long-term
memory.promoteToLongTerm(id: string): boolean;

// Search related
memory.searchRelated(content: string, limit?: number): MemoryEntry[];

// Apply time decay (episodic layer)
memory.applyTimeDecay(hoursElapsed: number): number;
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
