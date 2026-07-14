# 에이전트 런타임

**LLM → tools → 검증 → 재시도** 루프.

```bash
npx tsx packages/core/src/cliEntry.ts run "task" --stream
```

타임아웃 · 결과 캐시 · 서킷 브레이커 · 체크포인트.

[프로바이더](/ko/guide/providers) · [검증](/ko/architecture/verification)
