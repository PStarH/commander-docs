# Three-Layer Memory

**Three-Layer Memory.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 참고 표

| Layer | Max Entries | Max Memory | Decay |
|-------|-------------|------------|-------|
| Working | 50 | 100KB | None |
| Episodic | 500 | 500KB | Time-based |
| Long-term | 10000 | 5MB | None |


## 주요 내용

### Types

운영 시 **Types** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/three-layer-memory)를 보세요.

### API

운영 시 **API** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/three-layer-memory)를 보세요.

### Layer Configuration

운영 시 **Layer Configuration** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/api/three-layer-memory)를 보세요.

## 예제 (코드는 영어 유지)

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

## 운영

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## 관련

- [아키텍처 개요](/ko/architecture/overview)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [보안](/ko/guide/security)
- [빠른 시작](/ko/guide/getting-started)
