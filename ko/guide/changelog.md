# Changelog

- **SQLite persistence**: `SqliteWarRoomStore` with WAL mode, 9 indexes, transaction-safe writes. Enable via `WARROOM_STORAGE=sqlite`; `createWarRoomStore()` factory provides transparent switching - **Event sourcing engine**: Write-Ahead Log with SHA-256 hash chain tamper protection, snapshot-based recovery, deterministic event replay (IF-05)

이 문서는 Commander에서 **Changelog** 의 역할과 사용 방법을 설명합니다. CLI/API는 monorepo와 맞춥니다.

## 요점

- 지표: 25 프로바이더 · 5 토폴로지 · 18 도구 · 6700+ 테스트  
- 실행 예시는 [빠른 시작](/ko/guide/getting-started) 의 `cliEntry.ts` 경로를 사용  

## 관련

- [아키텍처](/ko/architecture/overview)  
- [빠른 시작](/ko/guide/getting-started)  
- [API](/ko/api/overview)  
