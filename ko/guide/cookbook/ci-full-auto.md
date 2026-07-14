# 쿡북: CI 풀오토 린트 수정

**목표:** CI에서 비대화형으로 Commander를 돌려 린트(또는 유사) 이슈를 고칩니다.

**시간:** 연동 ~15분 · **위험:** 높은 자율성 — PR 리뷰가 있는 잡으로 격리

## CI 설계 규칙

1. **일회용 브랜치** 또는 PR 워크플로 — 에이전트가 main에 force-push 금지
2. 잡에 필요한 **시크릿만** export
3. 샘플 레포 dry-run 후에만 `COMMANDER_MODE=full-auto`
4. 로그를 CI 아티팩트로 보관

## 1. 로컬 dry-run

```bash
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors in this repository" --stream
```

exit code와 git diff가 수용 가능한지 확인합니다.

## 2. GitHub Actions 스케치

```yaml
name: Commander lint fix
on:
  workflow_dispatch:
  # 또는 schedule / pull_request

jobs:
  fix:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 9
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: pnpm
      - name: Install Commander
        run: |
          git clone --depth 1 https://github.com/PStarH/Commander.git /tmp/Commander
          cd /tmp/Commander && pnpm install
      - name: Run Commander
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          COMMANDER_MODE: full-auto
        run: |
          cd $GITHUB_WORKSPACE
          npx tsx /tmp/Commander/packages/core/src/cliEntry.ts run "fix all lint errors" --stream
      - name: Show diff
        run: git diff --stat
      # 선택: stefanzweifel/git-auto-commit-action 또는 create-pull-request
```

Commander를 submodule 또는 (향후) 게시 패키지로 벤더링하면 경로를 맞추세요. **현재 주 경로는 모노레포 clone입니다.**

## 3. 성공 체크리스트

- [ ] 잡이 비대화형 (TTY 프롬프트 없음)
- [ ] 로그에 심의 + 스트림 포함
- [ ] merge 전 사람이 diff 리뷰
- [ ] 시크릿이 로그에 출력되지 않음

## 실패 모드

| 문제                  | 조치                                                 |
| --------------------- | ---------------------------------------------------- |
| 대화형 행             | `full-auto` 확인; 승인 프롬프트 비활성               |
| 프로바이더 rate limit | 잡 직렬화; 캐시; 프롬프트 범위 축소                  |
| 파괴적 편집           | 프롬프트 좁히기 (“eslint only”, path globs); PR 필수 |

## 관련

- [FAQ — CI/CD](/ko/guide/faq)
- [배포](/ko/deployment)
- [문제 해결](/ko/guide/troubleshooting)
