# 보안

Commander는 코드·도구·신뢰할 수 없는 모델 출력을 다루는 멀티 에이전트 워크로드를 위해 설계되었습니다. 운영자용 요약입니다. 심화: [Security Gateway](/ko/architecture/security-gateway), [Sandbox](/ko/architecture/sandbox), [멀티 테넌시](/ko/architecture/multi-tenancy).

## 취약점 신고

**보안 버그를 공개 GitHub 이슈로 올리지 마세요.**

**sampan090611@gmail.com** 으로 다음을 보내 주세요.

- 이슈 유형과 영향
- 관련 경로 / 커밋
- 재현 단계
- 가능하면 PoC

**48시간 이내** 수신 확인을 목표로 합니다 (제품 [SECURITY.md](https://github.com/PStarH/Commander/blob/master/SECURITY.md)).

## 위협 모델 (요약)

| 위협                   | Commander 완화                                                        |
| ---------------------- | --------------------------------------------------------------------- |
| 프롬프트 / 도구 인젝션 | 도구 출력 스캔, sanitizer, 비가역 도구 가역성 게이트                  |
| 시크릿 유출            | DLP 패턴, 시크릿 없는 구조화 로그, 엔터프라이즈 게이트웨이 vault 패턴 |
| 폭주 에이전트          | 승인 모드, 토큰 예산, 타임아웃, 서킷 브레이커                         |
| 프로바이더 장애 / 남용 | 페일오버 체인, rate limit, 테넌트 쿼터                                |
| 크로스 테넌트          | 스토리지·메모리·캐시·rate limit 격리                                  |
| 공급망 / 의존성        | CI npm audit; 키를 git에 넣지 않기                                    |

## 설정해야 할 통제

### 1. 승인 모드

| 모드        | 언제               |
| ----------- | ------------------ |
| `plan`      | 미리보기만         |
| `read-only` | 분석 / 감사        |
| `suggest`   | 사람이 쓰기 승인   |
| `auto-edit` | 신뢰하는 로컬 개발 |
| `full-auto` | PR 리뷰가 있는 CI  |

```bash
export COMMANDER_MODE=read-only
```

### 2. API 인증

HTTP 서버 실행 시:

```bash
export COMMANDER_API_KEY="long-random-secret"
```

API에 Bearer 필수. TLS·인증 없이 `:4000`을 공개 인터넷에 노출하지 마세요.

### 3. 네트워크 바인딩

API는 기본적으로 localhost 지향. 프로덕션에서는 리버스 프록시에서 TLS·인증 ([배포](/ko/deployment)).

### 4. 민감 코드

코드가 네트워크 밖으로 나가지 않게 **Ollama / vLLM** 선호:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
```

### 5. 멀티 테넌트 프로덕션

테넌트 프로바이더와 쿼터 활성화 — [멀티 테넌시](/ko/architecture/multi-tenancy).

## 보안 벤치마크 (모노레포)

| 스위트                | 목적                      |
| --------------------- | ------------------------- |
| Red Team (47)         | 방어에 대한 공격 카테고리 |
| AgentDojo             | 간접 인젝션 견고성        |
| Tenant isolation fuzz | 크로스 테넌트 변이 테스트 |

```bash
pnpm benchmark:redteam
pnpm benchmark:agentdojo
```

상세: [벤치마크](/ko/guide/benchmarks) · 제품 `BENCHMARK.md`.

## 관련

- [프로덕션 준비](/ko/architecture/production-readiness)
- [웹 콘솔](/ko/guide/web-console)
- [FAQ](/ko/guide/faq)
