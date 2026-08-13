# FAQ

## Commander란?

5개 정규 토폴로지로 여러 AI 에이전트를 조율하는 엔진입니다. 25 프로바이더, 18 내장 도구.

## 일반 AI 코딩 도구와 차이는?

단일 에이전트가 아니라 **자동 토폴로지·라이브 스트림·품질 게이트·프로덕션 인프라**를 제공합니다.

## 오픈소스?

네, MIT.

## API 키가 여러 개 필요?

아니요. **하나면 충분**합니다.

## 오프라인?

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```

## CI?

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors"
```

자세한 내용: [영문 FAQ](/guide/faq).
