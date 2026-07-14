# 플러그인 시스템

Commander 플러그인은 런타임 훅으로 동작을 확장합니다. 서드파티 플러그인은 **샌드박스 로드 컨텍스트**로 권한 상승을 막습니다.

## 개요

- **19개 훅 포인트** — LLM 전후, 도구 전후, 런 전후 등  
- **권한 상한** — 메인 시스템을 넘지 못함  
- **타임아웃** — 플러그인별 `maxExecutionTimeMs`  
- **내장 예** — `builtin-rag` (기본 비활성)  

## 활성화 예 (RAG)

```bash
npx tsx packages/core/src/cliEntry.ts plugin enable rag
```

또는 `.commander.json`:

```json
{
  "plugins": {
    "builtin-rag": { "enabled": true }
  }
}
```

## 커스텀 플러그인

`CommanderPlugin` 인터페이스를 구현하고 매니저에 등록합니다. 로드는 샌드박스 경로를 통과해야 하며, 네트워크·파일 권한은 프로파일에 따릅니다.

## 보안

- 플러그인 코드 스캔 · 권한 선언  
- 실행 타임아웃 · 예외 격리  
- 메인 프로세스 권한 초과 금지  

상세: [Sandbox](/ko/architecture/sandbox) · [보안](/ko/guide/security).

## 관련

- [RAG 지식 베이스](/ko/guide/advanced/rag-knowledge-base)  
- [확장 포인트](/ko/architecture/extension-points)  
- [프로덕션 준비](/ko/architecture/production-readiness)  
