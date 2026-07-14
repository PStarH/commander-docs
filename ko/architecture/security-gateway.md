# 엔터프라이즈 보안 게이트웨이

`EnterpriseSecurityGateway`는 모든 LLM 호출과 도구 실행에 적용되는 **7계층 심층 방어**입니다. 우회할 수 없습니다. 비용 검사는 LLM 호출 **전후** 모두 실행됩니다.

## 7계층 방어

| 계층 | 이름                 | 역할                            |
| ---- | -------------------- | ------------------------------- |
| 1    | Zero-Trust Signature | 무결성 검증 + 재전송 방지       |
| 2    | Authentication       | 타이밍 안전 비교의 API Key 검증 |
| 3    | Rate Limiting        | 전역 토큰 버킷 + IP 티어 제한   |
| 4    | Input Scanning       | 콘텐츠 인젝션 탐지 + 입력 검증  |
| 5    | Cost Pre-Check       | 청구 폭주 방지 (사전 추정)      |
| 6    | Request Processing   | 비즈니스 로직 실행              |
| 7    | Output Scanning      | DLP 유출 방지 + 비용 기록       |

### 설계 원칙

- **심층 방어** — 독립 계층, 책임이 분리
- **Fail fast** — 가장 저렴한 계층에서 조기 거절
- **관측 가능** — 모든 결정에 보안 메타데이터 로그
- **테넌트 격리** — 검사는 테넌트 단위
- **우회 불가** — 비용 검사는 호출 전후 모두

## DLP (Data Loss Prevention)

`dataLossPrevention.ts`가 모든 egress를 5단계 파이프로 스캔합니다.

### 탐지 패턴 (12+)

| 패턴                 | 예                            |
| -------------------- | ----------------------------- |
| API Key              | `sk-...`, `sk-ant-...`        |
| JWT                  | `eyJ...`                      |
| Private Key (PEM)    | `-----BEGIN PRIVATE KEY-----` |
| Credit Card (Luhn)   | `4111 1111 1111 1111`         |
| SSN                  | `123-45-6789`                 |
| Email / Phone        | `user@example.com`            |
| Internal IP          | `10.0.0.1`                    |
| DB connection string | `mongodb://user:pass@host`    |
| 클라우드 자격증명    | `AKIA...`, `AIza...`          |
| 중국 신분증 등       | 체크섬 검증                   |

### 레댁션 전략

| 전략     | 동작                      |
| -------- | ------------------------- |
| `REDACT` | `[REDACTED]` 로 치환      |
| `MASK`   | 부분 마스킹 (`sk-...abc`) |
| `HASH`   | SHA-256                   |
| `ALLOW`  | 통과 (로그만)             |

적용 지점: API 응답 · 로그 · 도구 결과 · 에이전트 출력 · SSE 스트림.

도구 입력은 실행 전 API Key / Private Key / AWS / GitHub Token / JWT / Password 6종을 스캔합니다.

## Capability Tokens

`capabilityToken.ts`가 단기 HMAC 서명 토큰을 발급합니다.

- 짧은 TTL · 스코프 바인딩 · HMAC 위변조 방지 · 만료 전 폐기 가능
- 도구 실행 지점에서 토큰 검증 필수

## Audit Chain Ledger

`auditChainLedger.ts`가 보안 이벤트를 해시 체인으로 기록해 변조 탐지가 가능합니다.

## 운영 팁

```bash
export COMMANDER_API_KEY="long-random-secret"
npx tsx packages/core/src/cliEntry.ts doctor
curl -s http://localhost:4000/health/detailed
```

공개 인터넷에 `:4000`을 TLS·인증 없이 노출하지 마세요. 지표: **25** 프로바이더 · **5** 토폴로지 · **18** tools · **6700+** 테스트.

## 관련

- [보안 가이드](/ko/guide/security)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [멀티 테넌시](/ko/architecture/multi-tenancy)
- [Sandbox](/ko/architecture/sandbox)
