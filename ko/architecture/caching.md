# 캐싱

Commander는 LLM 호출을 줄이고 응답을 빠르게 하며 중복 계산을 막기 위해 **다층 캐시**를 둡니다. 모든 캐시는 **테넌트 단위로 격리**됩니다.

## 캐시 계층

```
Tool Call
  │
  ├─ SingleFlightRequestCache  ── 동일 동시 요청 중복 제거
  │   (첫 요청만 실행, 나머지는 결과 대기)
  │
  ├─ ToolResultCache           ── SHA-256 정확 매칭
  │   (결정적 도구: 파일 읽기, 코드 검색 등)
  │
  └─ SemanticCache             ── 의미 유사도 캐시
      (의미가 비슷한 비결정적 LLM 호출)
```

## ToolResultCache

키는 `(tenantId + tool + args)` 의 SHA-256 해시입니다.

```typescript
const cache = new ToolResultCache({ basePath: '/data/cache' });

const key = cache.hashKey(tenantId, toolName, args);
const cached = await cache.get(key);

if (cached) return cached;

const result = await executeTool(toolName, args);
await cache.set(key, result);
```

- 결정적 도구(파일 읽기, 코드 검색, grep)에 적합  
- 테넌트 키 격리로 크로스 테넌트 유출 방지  
- TTL 설정 가능  
- 스토리지 쿼터 초과 시 LRU 축출  

## SemanticCache

비결정적 작업(LLM 호출)에는 임베딩 유사도를 씁니다.

```typescript
const semanticCache = new SemanticCache({ similarityThreshold: 0.95 });

const similar = await semanticCache.find(input, tenantId);
if (similar) return similar.result;

await semanticCache.store(input, result, tenantId);
```

- 코사인 유사도 비교  
- 임계값↑ = 오탐↓ / 히트↓ · 임계값↓ = 히트↑  
- TTL + LRU 조합 축출  

## SingleFlightRequestCache

동일 키의 **동시 중복 실행**(thundering herd)을 막습니다.

```typescript
const singleFlight = new SingleFlightRequestCache();

const [a, b, c] = await Promise.all([
  singleFlight.execute('key-1', () => expensiveOperation()),
  singleFlight.execute('key-1', () => expensiveOperation()),
  singleFlight.execute('key-1', () => expensiveOperation()),
]);
// expensiveOperation 은 한 번만 실행
```

여러 에이전트/런이 동시에 같은 도구·LLM을 요청할 때 특히 유용합니다.

## 통합 순서

도구 실행 파이프라인에서:

1. **SingleFlight** — 진행 중 요청 중복 제거  
2. **ToolResultCache** — 정확 매칭 히트  
3. **SemanticCache** — 유사 의미 히트  
4. 모두 미스일 때만 실제 LLM/도구 실행  

패키지는 monorepo `packages/core` 기준입니다. 설치는 clone + `pnpm install` 이 주 경로입니다.

## 관련

- [멀티 테넌시](/ko/architecture/multi-tenancy)  
- [에이전트 런타임](/ko/architecture/agent-runtime)  
- [도구](/ko/architecture/tools)  
