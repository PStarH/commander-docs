# 토폴로지 결정 트리

심의 엔진이 **5개 정규 토폴로지**를 고르는 기준. [탐색기](/ko/guide/topology-explorer)도 참고.

1. 명확한 단일 질문 → **SINGLE**  
2. 엄격한 파이프라인 → **CHAIN**  
3. 병렬 전문가 + 합성 → **DISPATCH**  
4. 리드가 위임·재계획 → **ORCHESTRATOR**  
5. 고위험/비평 필요 → **REVIEW**  

```bash
npx tsx packages/core/src/cliEntry.ts plan "your real task"
npx tsx packages/core/src/cliEntry.ts run "task" --topology review --stream
```

[멀티 에이전트](/ko/architecture/multi-agent)
