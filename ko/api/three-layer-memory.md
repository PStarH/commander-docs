# 3계층 메모리

> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요.영어 버전: [English](/api/three-layer-memory)



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
