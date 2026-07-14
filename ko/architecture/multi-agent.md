# 멀티 에이전트 오케스트레이션

| 토폴로지 | 패턴 |
|----------|------|
| SINGLE | 단일 에이전트 |
| CHAIN | 순차 파이프라인 |
| DISPATCH | 병렬 + 합성 |
| ORCHESTRATOR | 리드 + 워커 |
| REVIEW | 생산 + 비평 |

```bash
npx tsx packages/core/src/cliEntry.ts run "audit" --topology dispatch --stream
```

[토폴로지 탐색기](/ko/guide/topology-explorer)
