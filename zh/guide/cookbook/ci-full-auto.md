# Cookbook: CI full-auto lint fix

> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。完整英文版：[English](/guide/cookbook/ci-full-auto)



**Goal:** Run Commander non-interactively in CI to fix lint (or similar) issues.

**Time:** ~15 minutes to wire · **Risk:** high autonomy — isolate to a job with PR review

## Design rules for CI


1. Use a **throwaway branch** or PR workflow — never force-push to main from the agent  
2. Export **only** the secrets the job needs  
3. Prefer `COMMANDER_MODE=full-auto` only after a dry run on a sample repo  
4. Capture logs as CI artifacts  

## 1. Local dry run


```bash
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors in this repository" --stream
```

Confirm exit code and that git diff is acceptable.

## 2. GitHub Actions sketch


```yaml
name: Commander lint fix
on:
  workflow_dispatch:
  # or schedule / pull_request as you prefer

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
      # Optional: open PR with stefanzweifel/git-auto-commit-action or create-pull-request
```

Adapt paths if you vendor Commander as a submodule or published package.

## 3. Success checklist


- [ ] Job is non-interactive (no TTY prompts)  
- [ ] Logs include deliberation + stream  
- [ ] Diff reviewed by human before merge  
- [ ] Secrets not printed in logs  

## 失败模式


| Issue | Action |
|-------|--------|
| Interactive hang | Ensure `full-auto`; disable approval prompts via mode/env |
| Provider rate limits | Serialize jobs; cache; smaller scope prompt |
| Destructive edits | Narrow prompt (“eslint only”, path globs); require PR |

## 相关


- [FAQ — CI/CD](/zh/guide/faq)  
- [Deployment](/zh/deployment)  
- [Troubleshooting](/zh/guide/troubleshooting)  
