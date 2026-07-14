# 쿡북: 저장소 보안 감사

**목표:** 라이브 스트리밍과 읽기 쉬운 결과로 멀티 에이전트 보안 감사를 실행합니다.

**시간:** 약 10분 · **위험:** 읽기 위주 (`read-only` 또는 `plan` 권장)

## 1. 준비

```bash
cd /path/to/Commander   # 모노레포 루트
export OPENAI_API_KEY=sk-...   # 또는 지원되는 아무 키
```

학습 중 쓰기를 제한하려면:

```bash
export COMMANDER_MODE=read-only
```

## 2. 먼저 plan

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repository for security vulnerabilities, secrets, and risky dependencies"
```

**기대:** 분류(대개 ANALYSIS), 복잡도, 토폴로지(대개 DISPATCH 또는 REVIEW), 에이전트 역할.

## 3. stream으로 실행

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities, secrets, and risky dependencies" --stream
```

**스트림에서 기대하는 것:**

- 심의 배너 (작업 클래스 + 토폴로지)
- 여러 에이전트 또는 순차 도구 (grep, package audit 등)
- 품질 게이트 줄 (ACCURACY / COMPLETENESS / SAFETY …)
- 종합된 findings 요약

## 4. 토폴로지 고정 (선택)

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities" --stream --topology review
```

REVIEW는 더 엄격한 검증이 필요할 때 produce → critique 스타일을 강제합니다.

## 5. 성공 체크리스트

- [ ] Plan이 크래시 없이 토폴로지를 출력
- [ ] Stream에 에이전트/도구 활동이 보임
- [ ] 최종 요약에 구체적 findings 또는 범위와 함께 “없음”
- [ ] 설명 없는 행 (2분 이상 이벤트 0) 없음

## 실패 모드

| 문제                 | 조치                                                 |
| -------------------- | ---------------------------------------------------- |
| 프로바이더 없음      | `doctor`; 현재 셸의 env 확인                         |
| 얕은 감사            | 실제 코드베이스 경로 지정; 프롬프트를 더 구체적으로  |
| SAFETY 게이트 플래그 | 시크릿 유사 패턴이 있으면 정상 신호로 취급           |
| 비용/지연 큼         | `plan`만 사용하거나 빠른 프로바이더(Groq)로 트리아지 |

## 관련

- [보안](/ko/guide/security)
- [토폴로지 의사결정 트리](/ko/guide/usage/topology-decision-tree)
- [Watch 모드](/ko/guide/usage/watch-mode)
