# 토폴로지 탐색기

5개 정규 토폴로지를 한눈에 비교하고, 작업 유형에 맞는 선택을 고르는 가이드입니다.

## 한눈에

| 토폴로지 | 한 줄 | 에이전트 감 |
|----------|-------|-------------|
| **SINGLE** | 한 에이전트가 전부 | 1 |
| **CHAIN** | 순차 파이프 | 2–3 |
| **DISPATCH** | 독립 병렬 + 합성 | 2–10 |
| **ORCHESTRATOR** | 리드가 전문가에게 위임 | 3–8 |
| **REVIEW** | 생성 → 비평 → 정제 | 2–5 |

## 강제 선택

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --topology dispatch
npx tsx packages/core/src/cliEntry.ts run "task" --topology review
```

자동 선택은 심의·복잡도 점수를 따릅니다. 상세 트리: [토폴로지 의사결정 트리](/ko/guide/usage/topology-decision-tree).

## 언제 무엇을

- **단순 Q&A** → SINGLE  
- **다단계 변환** → CHAIN  
- **독립 모듈 감사** → DISPATCH  
- **설계+구현 분할** → ORCHESTRATOR  
- **보안·고위험** → REVIEW  

## 관련

- [멀티 에이전트](/ko/architecture/multi-agent)  
- [왜 Commander](/ko/guide/why-commander)  
- [Cookbook](/ko/guide/cookbook/)  
