# 도구 (Tools)

Commander는 코드베이스에 더 많은 클래스가 있어도, LLM에 기본적으로 **18개 내장 도구**를 노출합니다. 캐시·에러 처리·롤백을 염두에 둔 프로덕션용 설계입니다.

## 파일시스템

| Tool | 내부 이름 | 용도 |
|------|-----------|------|
| `read` | `file_read` | 파일 읽기 (라인/오프셋) |
| `write` | `file_write` | 생성·덮어쓰기 |
| `edit` | `file_edit` | 정확 문자열 치환 |
| `glob` / `file_search` | `file_search` | 패턴 검색 |
| `grep` / `file_list` | `file_list` | 내용 검색·디렉터리 목록 |

## 코드 인텔리전스

| Tool | 용도 |
|------|------|
| `ast_grep_search` | AST 인식 검색 |
| `patches` | 구조화 패치 적용 |
| `refine` / `fix` | AI 리파인·수정 |
| `lsp_*` | 진단, 심볼, 참조, rename |

## 웹 & 리서치

| Tool | 용도 |
|------|------|
| `websearch` / `webfetch` | 검색·URL fetch |
| `browser_*` | 브라우저 렌더 |
| `context7_*` | 라이브러리 문서 |

## 코드 실행

| Tool | 용도 |
|------|------|
| `bash` / `shell_execute` | 샌드박스 셸 |
| `python` / `execute_script` | 격리 실행 |

## 메모리 & 지속성

| Tool | 용도 |
|------|------|
| `memory_store` / `memory_recall` / `memory_list` | 영속 메모리 |
| `knowledge_search` | RAG 검색 (builtin-rag) |

## 버전 관리 · 미디어

| Tool | 용도 |
|------|------|
| `git` | status, diff, log, commit |
| `look_at` / `vision_analyze` | 이미지 분석 |
| `pdf_extract` / `screenshot` | PDF·스크린샷 |

## 오케스트레이션

| Tool | 용도 |
|------|------|
| `task` / `agent` | 서브 에이전트 위임 |
| `a2a_delegate` | A2A 위임 |
| `skill` / `meta` / `verify` | 스킬·메타·검증 |
| `todowrite` / `question` | 작업 추적·질문 |
| `mcp` / `saga` / `checkpoint` | MCP·사가·체크포인트 |

## 프로덕션 기능

모든 도구에 공통:

- **SHA-256 결과 캐시** — 테넌트 키 격리  
- **Compensation registry** — mutation 실패 롤백  
- **Circuit breaker** — 다운스트림 보호  
- **Step error boundary** — skip/retry/abort  
- **Tool call repair** — 잘못된 호출 자동 수정  
- **DLP 스캔** — 입력 6종 민감 패턴  

## 커스텀 도구

```typescript
import { Tool, ToolContext } from '@commander/core';

class MyCustomTool implements Tool {
  name = 'my-tool';
  description = 'Does something useful';

  async execute(context: ToolContext, args: any) {
    return { success: true, data: {} };
  }
}

runtime.registerTool('my-tool', new MyCustomTool());
```

> monorepo workspace 설치가 주 경로입니다.  
> CLI: `npx tsx packages/core/src/cliEntry.ts`

## 관련

- [에이전트 런타임](/ko/architecture/agent-runtime)  
- [커스텀 도구](/ko/guide/advanced/custom-tools)  
- [MCP](/ko/architecture/mcp)  
- [보안](/ko/guide/security)  
