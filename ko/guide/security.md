# 보안

**취약점 보고:** 공개 이슈 금지 — **sampan090611@gmail.com** (약 48시간 내 확인).

## 제어

```bash
export COMMANDER_MODE=read-only
export COMMANDER_API_KEY="long-random-secret"
export OLLAMA_BASE_URL=http://localhost:11434
```

완화: 주입 스캔, DLP, 승인 모드, 서킷 브레이커, 페일오버, 멀티 테넌트 격리, npm audit.

[게이트웨이](/ko/architecture/security-gateway) · [샌드박스](/ko/architecture/sandbox)
