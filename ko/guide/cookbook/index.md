# 쿡북

엔드투엔드 레시피입니다. 각 페이지: **목표 → 명령 → 기대 신호 → 실패 모드**.

| 레시피 | 시간 | 연습 |
|--------|------|------|
| [저장소 보안 감사](/ko/guide/cookbook/security-audit) | ~10분 | DISPATCH형 분석, 스트림, 게이트 |
| [모듈 안전 리팩터](/ko/guide/cookbook/refactor-module) | ~15분 | Plan → run → review |
| [CI 풀오토 린트 수정](/ko/guide/cookbook/ci-full-auto) | ~15분 | 비대화형, exit code |

## 공통 전제

`pnpm install` 후 monorepo 루트, API 키 1개 export.

```bash
npx tsx packages/core/src/cliEntry.ts <command>
# 빌드 후: commander <command>
```

처음이라면 [빠른 시작](/ko/guide/getting-started).

## 관련

- [왜 Commander](/ko/guide/why-commander)  
- [토폴로지 의사결정 트리](/ko/guide/usage/topology-decision-tree)  
- [웹 콘솔](/ko/guide/web-console)  
