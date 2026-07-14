# 구성

Commander is configured through environment variables and configuration files. Commander supports a `.commander.json` config file in your project root:

이 문서는 Commander에서 **구성** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

```bash
| Field | Default | Description |
|-------|---------|-------------|
| `provider` | `auto` | Primary LLM provider |
| `model` | `auto` | Model name |
| `mode` | `balanced` | Execution mode: `fast`, `balanced`, `thorough` |
| `topology` | `auto` | Orchestration topology: `auto`, `single`, `chain`, `dispatch`, `orchestrator`, `review` |
| `budget` | `auto` | Token budget (integer ≥1000 or `auto`) |
| `mcpServers` | `[]` | MCP server configurations |
```

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
