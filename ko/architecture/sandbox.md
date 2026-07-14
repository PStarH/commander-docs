# 보안 샌드박스

Commander 샌드박스는 모든 실행을 격리하고, Petri net 스케줄러로 자원을 형식적으로 할당합니다.

## 구조

```
sandbox/
├── execPolicy.ts           ← 실행 정책
├── approval.ts             ← 민감 작업 승인
├── profiles.ts             ← READ_ONLY / WORKSPACE_WRITE / FULL_ACCESS / HARDENED
├── platforms.ts            ← 플랫폼별 설정
├── manager.ts              ← 수명주기
├── executionRouter.ts      ← 백엔드 라우팅
├── lane.ts                 ← 실행 레인
├── seccompBpf.ts           ← Linux seccomp-BPF
├── teeEnclave.ts           ← TEE
├── petriNetScheduler.ts    ← Petri net 자원 할당
├── networkProxy.ts
├── backends/               ← local / ssh / docker
└── types.ts
```

## 보안 프로파일

| 프로파일 | Shell | 파일 쓰기 | 네트워크 | 용도 |
|----------|-------|-----------|----------|------|
| **READ_ONLY** | 없음 | 읽기 전용 | 차단 | 코드 리뷰, 비신뢰 입력 |
| **WORKSPACE_WRITE** | 샌드박스 허용 | 프로젝트 파일 | 허용 | 개발 |
| **FULL_ACCESS** | 전체 | 임의 | 허용 | CI/CD |
| **HARDENED** | 없음 | 거부 | 차단 | 비신뢰 코드 실행 |

## ExecPolicy

```typescript
interface ExecPolicy {
  allowShell: boolean;
  allowNetwork: boolean;
  allowFileWrite: boolean;
  allowFileDelete: boolean;
  allowedPaths: string[];
  deniedPaths: string[];
  maxExecutionTime: number;
  maxMemory: number;
}
```

## Petri Net 스케줄러

교착 없는 동시 실행을 위한 형식 모델:

| Place | 용량 | 용도 |
|-------|------|------|
| `pending` | 무제한 | 대기 요청 |
| `v8_slots` | 10 | V8 isolate |
| `seccomp_slots` | 4 | seccomp-BPF |
| `wasm_slots` | 2 | WebAssembly |
| `tee_slots` | 1 | TEE |
| `executing` / `completed` | 무제한 | 실행 중 / 완료 |

전이: `admit_<tier>` (pending + slot → executing), `complete_<tier>` (슬롯 반환). 데드락·포화·안전 상태 분석 후 입장.

## 백엔드

- **local** — 프로세스 로컬  
- **ssh** — 원격 SSH  
- **docker** — 컨테이너 실행  

## 운영

```bash
export COMMANDER_MODE=read-only   # 또는 plan / suggest
npx tsx packages/core/src/cliEntry.ts plan "audit this repo"
```

비신뢰 코드에는 HARDENED + 네트워크 차단을 기본으로 하세요.

## 관련

- [보안](/ko/guide/security)  
- [보안 게이트웨이](/ko/architecture/security-gateway)  
- [도구](/ko/architecture/tools)  
