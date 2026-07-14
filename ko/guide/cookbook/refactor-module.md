# 쿡북: 모듈을 안전하게 리팩터

**목표:** plan 모드로 리팩터를 미리 본 뒤, 통제된 승인으로 실행합니다.

**시간:** 약 15분 · **위험:** 파일 쓰기 — `plan` / `suggest`부터

## 1. 준비

```bash
cd /path/to/your-project   # 또는 dry-run용 Commander 모노레포
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=plan
```

실제 앱에 돌릴 때는 깨끗한 브랜치:

```bash
git checkout -b chore/commander-refactor
git status
```

## 2. plan 미리보기

```bash
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module to reduce duplication; keep public API stable"
```

**기대:** 토폴로지(대개 CHAIN 또는 ORCHESTRATOR), 단계, 도구, 예산 — **파일 수정 없음**.

점검:

- 의도한 모듈만 건드리는가?
- 위험한 변경에 REVIEW가 더 맞는가?

## 3. suggest 모드 (사람 개입)

```bash
export COMMANDER_MODE=suggest
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module to reduce duplication; keep public API stable" --stream
```

모드에 따라 터미널 승인 프롬프트로 편집을 승인/거부합니다.

## 4. auto-edit (plan을 신뢰할 때)

```bash
export COMMANDER_MODE=auto-edit
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module to reduce duplication; keep public API stable" --stream
```

## 5. 로컬 검증

```bash
git diff
# 프로젝트별:
pnpm test   # 또는 npm test / cargo test / 등
```

## 6. 성공 체크리스트

- [ ] 쓰기 전에 plan이 타당했음
- [ ] diff가 의도 파일로 제한됨
- [ ] 테스트 / 타입체크 통과
- [ ] 필요 시 `git checkout -- .`로 되돌릴 수 있음

## 실패 모드

| 문제                        | 조치                                        |
| --------------------------- | ------------------------------------------- |
| 과도한 편집                 | `plan` / `suggest` 유지; 프롬프트 범위 축소 |
| 잘못된 모듈                 | 경로를 명시: `packages/foo/src/auth/*`      |
| 불안정한 멀티 에이전트 병합 | `--topology chain` 또는 `--topology review` |

## 관련

- [Plan 모드](/ko/guide/usage/plan-mode)
- [작업 실행](/ko/guide/usage/running-tasks)
- [FAQ의 승인 모드](/ko/guide/faq)
