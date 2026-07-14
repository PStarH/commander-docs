# 문제 해결

자주 만나는 문제와 해결.

> **CLI:** monorepo 체크아웃에서는  
> `npx tsx packages/core/src/cliEntry.ts <command>`  
> `@commander/core` 빌드 후에는 `commander <command>`.

## 설치

### `pnpm install` 실패

```bash
pnpm install
pnpm build
```

레포 **루트**에서 workspace 전체를 설치하세요.

### 설치 후 TypeScript 오류

```bash
pnpm build
npx tsc --noEmit
```

## 프로바이더

### Provider not available

```bash
echo $OPENAI_API_KEY
npx tsx packages/core/src/cliEntry.ts doctor
```

키가 **현재 셸**에 export 되어 있어야 합니다.

### Rate limited

- 대기 후 재시도 (자동 backoff)
- 여러 키/프로바이더 fallback
- `export COMMANDER_MAX_CONCURRENCY=1`

### Timeout

- 네트워크 / 프로바이더
- 더 빠른 프로바이더 (Groq, Together)
- `export COMMANDER_TIMEOUT_MS=120000`

## 실행

### Hang

```bash
npx tsx packages/core/src/cliEntry.ts status
npx tsx packages/core/src/cliEntry.ts doctor
```

### Circuit breaker open

~30초 대기 또는:

```bash
npx tsx packages/core/src/cliEntry.ts doctor --reset
```

### 결과가 이상함

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
npx tsx packages/core/src/cliEntry.ts plan "task"
```

## Docker

```bash
docker info
docker compose build --no-cache
```

## 디버그

```bash
export COMMANDER_DEBUG=true
npx tsx packages/core/src/cliEntry.ts run "task" --stream
```

## 관련

- [빠른 시작](/ko/guide/getting-started)
- [설치](/ko/guide/installation)
- [프로바이더](/ko/guide/providers)
