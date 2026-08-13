# 빠른 시작

약 5분 안에 Commander를 실행합니다. API 키 하나. 그래프 빌더·YAML 없음.

## 성공 기준

1. `pnpm install` 성공  
2. 작업 실행 후 **심의(deliberation) + 토폴로지** 확인  
3. 정상 종료 또는 `doctor`의 명확한 오류  

## 사전 요구사항

- **Node.js** 18+ (22 권장)  
- **pnpm** 8+  
- LLM API 키 하나  

> monorepo이므로 **pnpm**을 사용하세요.

## 5분 체크리스트

### 1. 클론 및 설치

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

### 2. API 키

```bash
export OPENAI_API_KEY=sk-...
```

### 3. plan

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
```

### 4. stream 실행

```bash
npx tsx packages/core/src/cliEntry.ts run "explain the architecture of this repository" --stream
```

### 5. 웹 콘솔(선택)

```bash
pnpm gui
```

### 6. Docker(선택)

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
```

## 실패 시

| 증상 | 조치 |
|------|------|
| Provider not available | 현재 셸에 key export, `doctor` |
| 모듈 오류 | 루트에서 pnpm install/build |
| 멈춤 | `plan` 먼저, `COMMANDER_DEBUG=true` |
| 오프라인 | `OLLAMA_BASE_URL=http://localhost:11434` |

## 다음

- [왜 Commander인가](/ko/guide/why-commander)  
- [영문 문서](/guide/getting-started)  
- [아키텍처](/ko/architecture/overview)  
