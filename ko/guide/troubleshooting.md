# 문제 해결

> monorepo: `npx tsx packages/core/src/cliEntry.ts` · 빌드 후: `commander`

## 프로바이더 없음

```bash
echo $OPENAI_API_KEY
npx tsx packages/core/src/cliEntry.ts doctor
```

## 레이트리밋 / 타임아웃

`COMMANDER_MAX_CONCURRENCY=1` · `COMMANDER_TIMEOUT_MS=120000` · 두 번째 키

## 멈춤 / 서킷 브레이커

```bash
npx tsx packages/core/src/cliEntry.ts status
npx tsx packages/core/src/cliEntry.ts doctor --reset
```

## 디버그

```bash
export COMMANDER_DEBUG=true
npx tsx packages/core/src/cliEntry.ts run "task"
```

[FAQ](/ko/guide/faq)
