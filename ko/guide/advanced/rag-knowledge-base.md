# RAG Knowledge Base

Commander includes a built-in optional RAG (Retrieval-Augmented Generation) plugin that provides knowledge base search capabilities without requiring external services. The `builtin-rag` plugin is a `CommanderPlugin` with category `integration`, **disabled by default**. It provides:

이 문서는 Commander에서 **RAG Knowledge Base** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
# Enable via CLI
commander plugin enable rag

# Or in .commander.json
{
  "plugins": {
    "builtin-rag": { "enabled": true }
  }
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
