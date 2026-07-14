# 웹 콘솔

웹 콘솔은 Commander의 시각적 제어면입니다. 스트리밍 에이전트와 채팅, 라이브 토폴로지, 거버넌스, 운영 뷰를 한곳에서 다룹니다.

## 시작

### 개발 (모노레포)

```bash
cd Commander
pnpm install
export OPENAI_API_KEY=sk-...   # 또는 다른 프로바이더
pnpm gui
```

| 서비스          | 일반적인 URL          |
| --------------- | --------------------- |
| API             | http://localhost:4000 |
| Web (Vite 개발) | http://localhost:5173 |

`pnpm gui`는 API + Web을 띄우고 브라우저를 열려고 시도합니다.

### Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
```

| 서비스      | URL                   |
| ----------- | --------------------- |
| API         | http://localhost:4000 |
| Web (Nginx) | http://localhost:3000 |

## 무엇을 얻을 수 있나

| 영역           | 용도                                                              |
| -------------- | ----------------------------------------------------------------- |
| **Dashboard**  | 배틀 리포트, 토큰 추이, 라이브 토폴로지, 에이전트 명단, 미션 보드 |
| **Chat**       | 실시간 에이전트 스트림이 있는 대화형 실행                         |
| **Governance** | 승인 큐, 정책 설정, 감사 로그                                     |
| **DLQ**        | 데드 레터 큐 조회 + 재실행                                        |
| **Security**   | 컴플라이언스 / 자세 뷰 (ISO 42001 / NIST AI RMF 지향)             |
| **Execution**  | 라이브 실행 피드, 환각 위험 패널                                  |
| **Agents**     | 명단 + 계보 트리                                                  |

라벨은 `apps/web` 패키지와 함께 바뀔 수 있습니다. 픽셀 단위 UI 스펙이 아니라 **제품 맵**으로 읽으세요.

## 미리보기

![Commander 웹 콘솔 — 미션 보드, 라이브 토폴로지, 실행 피드, 채팅](/console-mockup.svg)

## 헬스 체크

```bash
curl http://localhost:4000/health
curl http://localhost:4000/health/detailed
curl http://localhost:4000/readyz
curl http://localhost:4000/metrics
```

## 인증

`COMMANDER_API_KEY`가 설정되어 있으면 API 클라이언트(콘솔 포함)는 다음을 보내야 합니다.

```http
Authorization: Bearer <COMMANDER_API_KEY>
```

키를 커밋하지 마세요. 유출되면 즉시 교체하세요.

## 콘솔 vs CLI

| 콘솔이 맞을 때                     | CLI가 맞을 때                   |
| ---------------------------------- | ------------------------------- |
| 시각적 토폴로지와 승인이 필요할 때 | 스크립트, CI, SSH만 있는 호스트 |
| 긴 멀티 에이전트 실행 디버깅       | 일회성 `plan` / `run --stream`  |
| 운영 (DLQ, 감사)                   | 자동화와 패키징                 |

## 문제 해결

| 증상      | 조치                                           |
| --------- | ---------------------------------------------- |
| 빈 UI     | `:4000` API 가동 확인; 브라우저 콘솔 CORS 점검 |
| 401       | API와 클라이언트에 동일한 `COMMANDER_API_KEY`  |
| 모델 없음 | `pnpm gui`를 띄운 셸에 프로바이더 키 export    |
| 포트 충돌 | 4000/5173/3000 사용 중인 프로세스 종료         |

더 보기: [문제 해결](/ko/guide/troubleshooting) · [배포](/ko/deployment).

## 관련

- [빠른 시작](/ko/guide/getting-started)
- [설치](/ko/guide/installation)
- [Agent SDK](/ko/guide/sdk) (프로그래밍 대안)
