# CLI 명령

예시는 빌드 후 `commander` 바이너리를 사용합니다. 소스 체크아웃에서는 다음으로 바꿉니다.

```bash
npx tsx packages/core/src/cliEntry.ts
```

## 작업 실행

| 명령                                | 설명                                       |
| ----------------------------------- | ------------------------------------------ |
| `commander <task>`                  | 빠른 작업 분석                             |
| `commander run <task>`              | 전체 멀티 에이전트 파이프라인              |
| `commander plan <task>`             | 심의 계획 (토폴로지, 에이전트, 예산)       |
| `commander run <task> --stream`     | 실시간 SSE 스트림                          |
| `commander run --file <tasks.json>` | 배치                                       |
| `commander swarm <task>`            | 재귀 분해 + 병렬                           |
| `commander drive <task>`            | 자율 단계 실행                             |
| `commander goal <task>`             | 다중 라운드 수렴                           |
| `commander company <task>`          | 품질 게이트·메모리 엔터프라이즈 파이프라인 |

## 인터페이스

| 명령            | 설명                         |
| --------------- | ---------------------------- |
| `commander gui` | Agent War Room (React + API) |
| `commander tui` | 터미널 대시보드              |
| `commander web` | 웹 인터페이스                |

## 분석 & 계획

| 명령                         | 설명                          |
| ---------------------------- | ----------------------------- |
| `commander review`           | 코드 리뷰 (P0–P3)             |
| `commander workers [topics]` | 병렬 리서치 워커              |
| `commander status`           | 시스템·프로바이더·MetaLearner |
| `commander cost`             | 비용 분석                     |

## 설정

| 명령                    | 설명           |
| ----------------------- | -------------- |
| `commander mode [mode]` | 승인 모드      |
| `commander config`      | 설정 보기/변경 |
| `commander doctor`      | 진단           |
| `commander budget`      | 토큰 예산      |
| `commander --debug`     | 상세 로그      |

## Skills / 세션 / Saga

- `skill list|view|create|pin`
- `history` / `share`
- `saga` · `checkpoint` · `compensation` · `resume` · `undo`

## 예

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo"
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
npx tsx packages/core/src/cliEntry.ts doctor
```

## 관련

- [빠른 시작](/ko/guide/getting-started)
- [토폴로지 의사결정 트리](/ko/guide/usage/topology-decision-tree)
- [설정](/ko/guide/configuration)
