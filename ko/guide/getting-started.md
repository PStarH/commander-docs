# 빠른 시작

약 5분 안에 Commander를 실행합니다. API 키 하나. 그래프 빌더 없음. YAML 없음.

## 성공 기준

다음 **세 가지**가 모두 참이면 완료입니다.

1. `pnpm install`이 오류 없이 끝남
2. 작업을 실행해 **심의(deliberation) + 토폴로지**를 봄 (plan 또는 stream)
3. 프로세스가 결과와 함께 종료 (또는 `doctor`의 명확한 오류 — 조용한 hang 아님)

## 사전 요구

- **Node.js** 18+ (22 권장)
- **pnpm** 8+ (9+ 권장 — monorepo workspaces)
- LLM API 키 하나 (OpenAI, Anthropic, DeepSeek, Groq, …)

> **pnpm**을 쓰세요. npm만으로는 멀티 패키지 monorepo에 부족합니다.

## 5분 체크리스트

### 1. 클론 & 설치

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

설치 후 권장:

```bash
pnpm -r build
```

### 2. API 키

```bash
export OPENAI_API_KEY=sk-...
# 또는: ANTHROPIC_API_KEY / DEEPSEEK_API_KEY / GROQ_API_KEY / ...
```

Commander가 프로바이더를 **자동 감지**합니다. 전체 목록: [프로바이더](/ko/guide/providers).

### 3. Plan (무위험)

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
```

파일 변경 없이 복잡도·토폴로지·에이전트 배분을 볼 수 있어야 합니다.

### 4. Stream 실행

```bash
npx tsx packages/core/src/cliEntry.ts run "explain the architecture of this repository" --stream
```

라이브 에이전트 사고, 도구 호출, 품질 게이트가 보여야 합니다.

### 5. (선택) 웹 콘솔

```bash
pnpm gui
```

- API: `http://localhost:4000`
- Web: 보통 `http://localhost:5173` (dev) 또는 `http://localhost:3000` (Docker)

[웹 콘솔](/ko/guide/web-console).

### 6. (선택) Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000
```

## 빌드 후: `commander` 바이너리 (선택)

npm 공개가 주 경로가 되기 전까지 monorepo 엔트리를 쓰세요.

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

로컬 core 빌드 후 workspace bin이 있을 수 있습니다.

```bash
pnpm --filter @commander/core build
commander run "audit this repo" --stream
```

## 실패했을 때

| 증상                             | 조치                                                                                               |
| -------------------------------- | -------------------------------------------------------------------------------------------------- |
| `Provider not available`         | `echo $OPENAI_API_KEY` — **이** 셸에 export. 그다음 `npx tsx packages/core/src/cliEntry.ts doctor` |
| `Cannot find module` / workspace | 레포 루트에서 **pnpm**, 재설치 `pnpm install` + `pnpm -r build`                                    |
| Hang / 출력 없음                 | 먼저 `plan`; `COMMANDER_DEBUG=true`; 네트워크/프로바이더 상태                                      |
| Rate limited                     | 대기, `COMMANDER_MAX_CONCURRENCY=1`, 또는 두 번째 키                                               |
| Circuit breaker open             | ~30초 대기 또는 `doctor --reset`                                                                   |
| 오프라인만                       | Ollama: `export OLLAMA_BASE_URL=http://localhost:11434`                                            |

전체: [문제 해결](/ko/guide/troubleshooting).

## 방금 무슨 일이?

1. 작업을 **분류** (CODING / RESEARCH / ANALYSIS / FACTUAL)
2. 토폴로지를 **선택** (SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW)
3. 도구와 함께 하나 이상의 에이전트를 **실행**
4. 다섯 품질 게이트로 출력을 **검증**

상세: [토폴로지 의사결정 트리](/ko/guide/usage/topology-decision-tree) · [아키텍처](/ko/architecture/overview).

## 다음 경로

| 목표                 | 이동                                                    |
| -------------------- | ------------------------------------------------------- |
| 실전 레시피          | [쿡북](/ko/guide/cookbook/)                             |
| 왜 이 프레임워크인가 | [왜 Commander](/ko/guide/why-commander)                 |
| TypeScript 임베드    | [Agent SDK](/ko/guide/sdk)                              |
| VM에 배포            | [배포](/ko/deployment) · [설치](/ko/guide/installation) |
| CLI 레퍼런스         | [명령](/ko/guide/commands)                              |
