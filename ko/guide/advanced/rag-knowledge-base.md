# RAG 지식 베이스

Commander에는 외부 서비스 없이 지식 검색을 제공하는 선택적 **RAG (Retrieval-Augmented Generation)** 플러그인이 포함됩니다.

## 개요

`builtin-rag`는 카테고리 `integration`의 `CommanderPlugin`이며 **기본 비활성**입니다.

- 문서 수집 (청크 + 임베딩)
- 빠른 유사도 검색용 HNSW 벡터 인덱스
- (선택) LLM 호출 전 컨텍스트 자동 주입
- OpenAI 또는 로컬 임베딩 (제로 의존 fallback)

## 활성화

```bash
# CLI (빌드 후 commander, 또는 monorepo 엔트리)
npx tsx packages/core/src/cliEntry.ts plugin enable rag

# 또는 .commander.json
{
  "plugins": {
    "builtin-rag": { "enabled": true }
  }
}
```

## 설정

| 옵션             | 기본                         | 설명                |
| ---------------- | ---------------------------- | ------------------- |
| `kbPath`         | `.commander/knowledge-base/` | 문서·벡터 저장 경로 |
| `embeddingModel` | `text-embedding-3-small`     | OpenAI 임베딩 모델  |
| `chunkSize`      | `512`                        | 청크 문자 수        |
| `chunkOverlap`   | `50`                         | 청크 겹침           |
| `maxResults`     | `5`                          | 최대 검색 결과      |
| `autoInject`     | `false`                      | LLM 전 자동 주입    |

## 임베딩 전략

1. **OpenAI** — `OPENAI_API_KEY`가 있을 때 (`text-embedding-3-small`)
2. **로컬** — 오프라인용 제로 의존 fallback

## 벡터 검색

`memory/hnswIndex.ts`의 HNSW를 사용합니다.

- **1000+** 엔티티: 근사 최근접 이웃
- 더 작으면 brute-force 정확 검색
- `bruteForceThreshold` 기본 1000

## 문서 수집

```
Document → Chunk (512, overlap 50) → Embed → Index (HNSW) → Persist
```

- `kb-documents.json` — 메타데이터
- `kb-vectors.json` — 청크 + 임베딩
- 쓰기는 temp + rename으로 atomic

## API (활성 시)

| Endpoint                     | Method   | 용도      |
| ---------------------------- | -------- | --------- |
| `/api/knowledge-base`        | `GET`    | 문서 목록 |
| `/api/knowledge-base`        | `POST`   | 업로드    |
| `/api/knowledge-base/:id`    | `DELETE` | 삭제      |
| `/api/knowledge-base/search` | `POST`   | 검색      |

## 관련

- [플러그인 시스템](/ko/guide/advanced/plugin-system)
- [Three-layer memory](/ko/api/three-layer-memory)
- [보안](/ko/guide/security)
