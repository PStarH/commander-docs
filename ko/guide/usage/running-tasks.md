# 작업 실행

필요에 따라 여러 실행 방식을 제공합니다.

> **monorepo CLI:** `npx tsx packages/core/src/cliEntry.ts …`  
> **빌드 후:** `commander …`

## 빠른 작업

```bash
npx tsx packages/core/src/cliEntry.ts "what does this function do?"
```

분석 → 토폴로지 선택 → 실행 → 결과를 한 번에 반환합니다.

## 전체 파이프라인

```bash
npx tsx packages/core/src/cliEntry.ts run "implement user authentication with JWT"
```

1. 심의 · 2. 노력 스케일 · 3. 토폴로지 · 4. 원자화 · 5. 실행 · 6. 검증(5 품질 게이트)

## 플랜

```bash
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module"
```

파일 변경 없이 복잡도·토폴로지·에이전트·예산을 표시합니다.

## 워치(SSE)

```bash
npx tsx packages/core/src/cliEntry.ts watch "debug the failing test"
```

## 승인 모드

| 모드 | 동작 |
|------|------|
| `plan` | 계획만 |
| `read-only` | 읽기 |
| `auto-edit` | 자동 편집 |
| `full-auto` | 완전 자율(CI) |
| `suggest` | 제안 후 대기 |

```bash
export COMMANDER_MODE=auto-edit
```

## 관련

- [플랜 모드](/ko/guide/usage/plan-mode) · [워치](/ko/guide/usage/watch-mode) · [명령](/ko/guide/commands)
