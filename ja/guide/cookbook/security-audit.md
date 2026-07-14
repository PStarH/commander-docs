# クックブック: リポジトリのセキュリティ監査

```bash
export COMMANDER_MODE=read-only
npx tsx packages/core/src/cliEntry.ts plan "audit this repository for security vulnerabilities, secrets, and risky dependencies"
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities, secrets, and risky dependencies" --stream
npx tsx packages/core/src/cliEntry.ts run "audit..." --stream --topology review
```

成功: プランにトポロジ、stream に tools/gates、具体的な findings。

[セキュリティ](/ja/guide/security) · [トポロジ](/ja/guide/usage/topology-decision-tree)
