# Deployment

Commander의 **Deployment** 사용법과 운영 포인트를 정리합니다.

## 빠른 시작

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API:     http://localhost:4000
# Web GUI: http://localhost:3000   (Docker / Nginx)
# Dev GUI: http://localhost:5173   (pnpm gui, no Docker)
```


## 포인트

- monorepo CLI: `cliEntry.ts` / 빌드 후 `commander`  
- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 정확한 동작은 monorepo 소스를 기준으로 합니다  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
