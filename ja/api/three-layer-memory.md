# 3 層メモリ

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/api/three-layer-memory)



Manages working, episodic, and long-term memory with embedding-based retrieval.

## Types


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

## API


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

## Layer Configuration


| Layer | Max Entries | Max Memory | Decay |
|-------|-------------|------------|-------|
| Working | 50 | 100KB | None |
| Episodic | 500 | 500KB | Time-based |
| Long-term | 10000 | 5MB | None |
