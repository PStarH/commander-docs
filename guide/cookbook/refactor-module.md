# Cookbook: Refactor a module safely

**Goal:** Use plan mode to preview a refactor, then execute with controlled approval.

**Time:** ~15 minutes · **Risk:** writes files — start in `plan` / `suggest`

## 1. Setup

```bash
cd /path/to/your-project   # or the Commander monorepo for a dry run
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=plan
```

If you run against a real app, use a clean git branch:

```bash
git checkout -b chore/commander-refactor
git status
```

## 2. Preview the plan

```bash
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module to reduce duplication; keep public API stable"
```

**Expect:** topology (often CHAIN or ORCHESTRATOR), steps, tools, budget — **no file edits**.

Review:

- Does the plan touch only the modules you intend?  
- Is REVIEW topology appropriate for a risky change?  

## 3. Suggest mode (human in the loop)

```bash
export COMMANDER_MODE=suggest
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module to reduce duplication; keep public API stable" --stream
```

Approve/deny edits according to your terminal prompts (if approval UI is active for your mode).

## 4. Auto-edit (when you trust the plan)

```bash
export COMMANDER_MODE=auto-edit
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module to reduce duplication; keep public API stable" --stream
```

## 5. Verify locally

```bash
git diff
# project-specific:
pnpm test   # or npm test / cargo test / etc.
```

## 6. Success checklist

- [ ] Plan looked correct before any write  
- [ ] Diff is limited to intended files  
- [ ] Tests / typecheck still pass  
- [ ] You can `git checkout -- .` to undo if needed  

## Failure modes

| Issue | Action |
|-------|--------|
| Over-eager edits | Stay in `plan` / `suggest`; shrink the prompt scope |
| Wrong module | Name paths explicitly: `packages/foo/src/auth/*` |
| Flaky multi-agent merge | Force `--topology chain` or `--topology review` |

## Related

- [Plan Mode](/guide/usage/plan-mode)  
- [Running Tasks](/guide/usage/running-tasks)  
- [Approval modes in FAQ](/guide/faq)  
