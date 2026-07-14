# 쿡북: 저장소 보안 감사

```bash
export COMMANDER_MODE=read-only
npx tsx packages/core/src/cliEntry.ts plan "audit this repository for security vulnerabilities, secrets, and risky dependencies"
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities, secrets, and risky dependencies" --stream
```

성공: 플랜에 토폴로지, 스트림에 tools/gates, 구체적 findings.

[보안](/ko/guide/security)
