# 카오스 테스트

카오스 테스트는 의도적으로 장애를 넣어 레질리언스(브레이커, 폴백, 체크포인트, DLQ)가 기대한 대로 동작하는지 검증합니다.

## 목적

- 프로바이더 타임아웃·rate limit 시 폴백  
- 크래시 후 체크포인트 재개  
- 브레이커 open / half-open  
- DLQ 적재와 재실행  

## monorepo에서

제품 CI와 `packages/core` 테스트에 카오스·스트레스 시나리오가 포함됩니다.

```bash
cd packages/core
npx tsx --test tests/*.test.ts
```

벤치마크·레드팀 스위트는 monorepo 스크립트(`pnpm benchmark:*`)를 참고하세요.

## 로컬 연습

```bash
# 의도적으로 느린/불안정 키 없이 plan 만
npx tsx packages/core/src/cliEntry.ts plan "audit this repo"

# 브레이커 상태 확인
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts doctor --reset
```

프로덕션에서 카오스를 넣을 때는 카나리 테넌트·섀도 트래픽을 쓰세요.

## 관련

- [Resilience](/ko/architecture/resilience)  
- [이벤트 소싱](/ko/architecture/event-sourcing)  
- [섀도 트래픽](/ko/guide/usage/shadow-traffic)  
- [벤치마크](/ko/guide/benchmarks)  
