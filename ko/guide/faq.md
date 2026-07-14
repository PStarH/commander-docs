# FAQ

## Commander란?

5개 정규 토폴로지로 여러 AI 에이전트를 조율하는 엔진입니다. 25 프로바이더, 18 내장 도구, 6700+ 테스트.

## 일반 AI 코딩 도구와 차이는?

단일 에이전트가 아니라 **자동 토폴로지·라이브 SSE·품질 게이트·프로덕션 인프라**를 제공합니다.

## API 키가 여러 개 필요?

아니요. **하나면 충분**합니다.

## 오프라인?

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```

## 파일 수정?

모드로 제어: `plan` / `read-only` / `suggest` / `auto-edit` / `full-auto`.

## CI?

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors"
```

## 5 토폴로지

SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW — [결정 트리](/ko/guide/usage/topology-decision-tree)

[문제 해결](/ko/guide/troubleshooting) · [보안](/ko/guide/security)
