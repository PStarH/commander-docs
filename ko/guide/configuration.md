# Configuration

**Configuration.** 이 페이지는 Commander 아키텍처 구성 요소를 설명합니다. monorepo 구조에 맞춘 한국어 운영 문서이며, 코드 블록은 영어 그대로입니다.

제품 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

CLI monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 참고 표

| Variable | Default | Description |
|----------|---------|-------------|
| `COMMANDER_MODE` | `auto-edit` | Approval mode: `plan`, `read-only`, `auto-edit`, `full-auto`, `suggest` |
| `COMMANDER_DEBUG` | `false` | Enable verbose debug logging |
| `COMMANDER_LOG_LEVEL` | `info` | Log level: `debug`, `info`, `warn`, `error` |
| `COMMANDER_LOG_PERSIST` | `false` | Enable log persistence to disk (auto-degrades to Error-only when backlog >10000) |
| `COMMANDER_MAX_CONCURRENCY` | `5` | Maximum concurrent agent executions |
| `COMMANDER_TIMEOUT_MS` | `120000` | Default execution timeout (ms) |


## 주요 내용

### Environment Variables

운영 시 **Environment Variables** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/configuration)를 보세요.

### CLI Configuration

운영 시 **CLI Configuration** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/configuration)를 보세요.

### Provider Config

운영 시 **Provider Config** 는 품질 게이트·DLQ·서킷 브레이커와 함께 씁니다. 소스는 monorepo, 전체 명세는 [영문 레퍼런스](/guide/configuration)를 보세요.

## 예제 (코드는 영어 유지)

```json
{
  "provider": "auto",
  "model": "auto",
  "mode": "balanced",
  "topology": "auto",
  "budget": "auto",
  "mcpServers": [],
  "a2a": {
    "server": {
      "enabled": false,
      "port": 3002,
      "host": "127.0.0.1"
    },
    "remoteAgents": []
  }
}
```

```bash
export OPENAI_API_KEY=sk-...        # Primary: OpenAI | Fallback: DeepSeek → GLM → MiMo
export ANTHROPIC_API_KEY=sk-ant-... # Anthropic Claude
export GOOGLE_API_KEY=...           # Google Gemini
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
