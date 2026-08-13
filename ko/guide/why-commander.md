# 왜 Commander인가

Commander는 멀티 에이전트를 **블랙박스로 두지 않으려는 엔지니어**를 위한 제품입니다.

**그래프 빌더 없음. YAML 없음.**  
키 하나 → 작업 분류 → 토폴로지 선택 → 모든 결정을 스트림 → 출력 검증.

## 한눈에

| 항목 | Commander | 일반 프레임워크 |
|------|-----------|-----------------|
| 시작 | 자연어 + 키 하나 | 그래프/YAML 작성 |
| 토폴로지 | 5종 자동 선택 | 직접 연결 |
| 가시성 | 라이브 SSE | 사후 로그 |
| 품질 | 5계층 게이트 | 선택/자체 구현 |
| 프로바이더 | 25 + 페일오버 | 1–2개 중심 |
| 프로덕션 | 서킷브레이커, DLQ, Saga, WAL | 데모 우선 |

## 60초 체험

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "explain this repository architecture" --stream
```

- [빠른 시작](/ko/guide/getting-started)  
- [영문 Why](/guide/why-commander)  
