# 이벤트 소싱 & 복구

Commander의 이벤트 소싱은 **크래시 안전 실행**, 변조 방지 감사 추적, 결정적 재생, 좀비 런 자동 복구를 제공합니다.

## EventSourcingEngine

`EventSourcingEngine`은 WAL(Write-Ahead Log)과 SHA-256 해시 체인으로 IEventSourcingEngine 계약(Pillar I)을 구현합니다.

### Write-Ahead Log

이벤트는 `.commander_state/event-sourcing.wal` 에 원자적으로 추가됩니다 (`COMMANDER_EVENT_SOURCING_WAL` 로 경로 변경 가능).

```
[event 1] → SHA256("") → hash_1
[event 2] → SHA256(hash_1 | type | id | timestamp | payload) → hash_2
[event 3] → SHA256(hash_2 | type | id | timestamp | payload) → hash_3
```

쓰기 락이 append를 직렬화해 해시 체인 손상을 막습니다.

### 해시 체인 무결성

각 이벤트 해시는 이전 해시를 포함합니다. `verifyIntegrity()`가 전체를 재계산해 변조를 탐지합니다.

### 비결정 입력 기록

재생 시 재계산 대신 로그의 사용합니다.

- 타임스탬프 · 난수(UUID, salt) · LLM 응답 · 도구 결과  

제약 IF-05(결정적 재생): 로그를 재생하면 동일한 상태 전이가 나옵니다.

### 스냅샷 & 압축

- `snapshot()` — 전체 재생 없이 빠른 복구용 스냅샷  
- `compact()` — 스냅샷 이전 이벤트 제거, WAL 재작성  
- `readFrom(snapshotId)` — 스냅샷 이후 이벤트 스트림  

### 헬스

| 메트릭 | Degraded | Unhealthy |
|--------|----------|-----------|
| WAL write latency (p95) | 50ms | 200ms |
| WAL file size | 100MB | 500MB |
| Event backlog ratio | 1000 | 10000 |
| Hash chain integrity | — | 어떤 끊김이든 |

`/health/detailed` 로 노출됩니다.

### EventSourcingSubscriber

MessageBus에 구독해 메인 루프를 침범하지 않고 비동기 WAL 기록. WAL 불가 시 graceful degrade.

## RecoveryBootstrapper

프로세스 기동 시 좀비 런을 스캔합니다.

1. **RunLedger 스캔** — EXECUTING / VERIFYING / PAUSED  
2. **Lease 확인** — 만료 lease  
3. **Fencing lease 획득** — holder `recovery-{pid}`, TTL 30s  
4. **결정**  
   - PAUSED + 복구 가능 체크포인트 → resume  
   - EXECUTING/VERIFYING → abort + compensate (안전 기본값)  
   - 이미 처리됨 → skip  
5. **DLQ 기록** · MessageBus에 복구 이벤트  

### 멱등성

두 프로세스가 동시에 기동해도 두 번째는 lease를 보고 skip. CI에서는 `forceAbort`로 abort+compensate 강제 가능.

```typescript
interface RecoveryResult {
  scanned: number;
  recovered: number;
  aborted: number;
  skipped: number;
  details: RecoveryDetail[];
}
```

## 복구 우선순위

1. **이벤트 재생** — 가장 정확  
2. **체크포인트** — 빠르지만 최근 상태 손실 가능  
3. **Abort + compensate** — 안전 폴백  

## 연동

| 컴포넌트 | 역할 |
|----------|------|
| `RunLedger` | 런 상태 소스 오브 트루스 |
| `LeaseManager` | 배타 소유 fencing |
| `CheckpointStore` | SQLite 체크포인트 |
| `DeadLetterQueue` | 복구/중단 런 기록 |
| `MessageBus` | 복구 이벤트 |
| `CompensationBridge` | 중단 시 롤백 |

## 관련

- [프로덕션 준비](/ko/architecture/production-readiness)  
- [에이전트 런타임](/ko/architecture/agent-runtime)  
- [V2 마이그레이션](/ko/guide/migration-v2)  
