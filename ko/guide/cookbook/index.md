# 쿡북

엔드투엔드 레시피입니다. 각 페이지 구성: **목표 → 명령 → 기대 신호 → 실패 모드**.

| 레시피                                                       | 시간  | 연습하는 것                       |
| ------------------------------------------------------------ | ----- | --------------------------------- |
| [저장소 보안 감사](/ko/guide/cookbook/security-audit)        | ~10분 | DISPATCH형 분석, 스트리밍, 게이트 |
| [모듈을 안전하게 리팩터](/ko/guide/cookbook/refactor-module) | ~15분 | Plan → run → review               |
| [CI 풀오토 린트 수정](/ko/guide/cookbook/ci-full-auto)       | ~15분 | 비대화형 모드, exit code          |

## 공통 전제

모든 레시피는 `pnpm install` 이후 Commander 모노레포 루트에 있고, API 키 하나가 export 되어 있다고 가정합니다.

```bash
# 소스 체크아웃
npx tsx packages/core/src/cliEntry.ts <command>

# @commander/core 빌드 후
commander <command>
```

Commander가 처음이라면 [빠른 시작](/ko/guide/getting-started)부터.
