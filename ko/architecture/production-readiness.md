# 프로덕션 준비

Commander는 첫날부터 프로덕션을 염두에 둡니다. 관측·안전·신뢰성 기능이 구성 요소마다 들어 있습니다.

## 기능 매트릭스

| 역량                  | Commander 상태                                                                    |
| --------------------- | --------------------------------------------------------------------------------- |
| **타입 안전**         | TypeScript strict, **`as any` / `@ts-ignore` 제로** (ESLint error)                |
| **에러 처리**         | 100+ 모듈에서 **빈 catch 제로**                                                   |
| **메트릭**            | Prometheus/OpenMetrics 카운터·게이지·히스토그램 + 테넌트 라벨                     |
| **트레이싱**          | 영속 trace store, OpenTelemetry export                                            |
| **크래시 안전**       | 단계마다 atomic SQLite WAL 체크포인트 + 이벤트 소싱 해시 체인                     |
| **서킷 브레이커**     | 5회 실패 → 30s open → half-open, 프로바이더별 레지스트리                          |
| **DLQ**               | 7 카테고리, 15 실패 모드, 영속 저장 + 재실행                                      |
| **멀티 테넌시**       | 테넌트별 rate limit, 동시성 쿼터, 스토리지·캐시 격리                              |
| **보안**              | 7계층 EnterpriseSecurityGateway, DLP, capability tokens, Bearer, CORS, rate limit |
| **관측**              | health, readiness, OpenAPI, SSE, Grafana 대시보드                                 |
| **이벤트 소싱**       | SHA-256 해시 체인 WAL, 스냅샷 복구, 결정적 재생                                   |
| **플러그인 샌드박스** | 서드파티 플러그인 로드 컨텍스트 제한; 권한은 메인 시스템을 넘지 않음              |

## 안전 메커니즘

### Circuit Breaker

연속 5회 실패 후 30초 open, 이후 half-open으로 회복. `CircuitBreakerRegistry`가 활성 프로바이더 브레이커를 관리합니다.

### Dead Letter Queue

복구 불가 오류를 7 카테고리(llm, tool, execution, verification, circuit_breaker, compensation, semantic_drift)와 15 표준 실패 모드로 영속화. 원인 수정 후 재실행 지원.

### Compensation Registry

실패한 mutation 도구는 등록된 보상 액션으로 롤백. 분산 트랜잭션용 Saga 코디네이터와 연동.

### State Checkpointer

매 단계 SQLite WAL(synchronous=NORMAL, busy_timeout=5000)로 atomic 체크포인트. 실패 지점에서 재개.

### Event Sourcing Engine

SHA-256 해시 체인 WAL로 변조 방지 이벤트 로그. 타임스탬프·난수·LLM 응답·도구 결과 등 비결정 입력을 기록해 결정적 재생.

### Recovery Bootstrapper

프로세스 기동 시 zombie run(EXECUTING/VERIFYING/PAUSED) 스캔, fencing lease 획득 후 체크포인트 재개 또는 보상 후 중단.

## 관측

### 메트릭

```typescript
getMetricsCollector().exportOpenMetrics();
// counters, gauges, histograms + tenant labels
```

### Tracing

`TraceStore`에 영속하는 span 기반 실행 트레이스. OpenTelemetry export 시 PII 레드액션 (`gen_ai.prompt` 등 자동 제거).

### Health

- `/health` — liveness
- `/ready` — readiness
- `/metrics` — Prometheus
- `/health/detailed` — 브레이커, DLQ, compensation, event bus, provider, event sourcing

### Grafana

- **개발자 뷰**: 성공률, P95, 토큰 비용, 활성 run, 도구 성공률
- **메커니즘 뷰**: WAL 지연·크기, DLQ backlog, 브레이커 상태, 이벤트 backlog, SQLite 락, 보상 실행률

## 테스트

**실패 제로 지향:**

- 6700+ unit / integration / chaos / e2e
- 카오스 몽키 장애 주입
- 멀티 테넌트 격리 시나리오
- 플러그인 권한·샌드박스 시나리오
- 스트레스: 10K 메시지, 50 동시 호출

```
npx tsx --test tests/*.test.ts
npx tsc --noEmit
```

## 관련

- [에이전트 런타임](/ko/architecture/agent-runtime)
- [검증 파이프라인](/ko/architecture/verification)
- [배포](/ko/deployment)
