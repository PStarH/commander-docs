# 섀도 트래픽

섀도 트래픽은 프로덕션에 영향을 주지 않고 Commander 두 버전을 **나란히 비교**합니다. 섀도 프록시가 프로덕션 요청을 섀도 엔드포인트로 미러링하고, 상태·지연·비용 드리프트를 보고합니다.

## 사용 사례

- **배포 전 검증** — 현재 vs 후보 버전 비교
- **프로바이더 마이그레이션** — OpenAI → Anthropic 등을 위험 없이 시험
- **설정 변경** — 새 토폴로지·라우팅 규칙 검증
- **회귀 탐지** — 성능·품질 저하를 조기 포착

## 빠른 시작

### 1. 설정 파일

```bash
cat > .commander/shadow-config.json <<EOF
{
  "enabled": true,
  "endpoint": "http://localhost:9999",
  "sampleRate": 0.1,
  "scrubPii": true,
  "diffMode": "status_cost_latency",
  "timeoutMs": 5000
}
EOF
```

### 2. 섀도 러너

```bash
npx tsx packages/core/src/cli/commands/shadow.ts runner --port=9999 &
```

### 3. 프로덕션에서 프록시 활성화

```bash
export COMMANDER_SHADOW_ENABLED=true
npx tsx packages/core/src/cli/index.ts serve
```

### 4. 드리프트 리포트

```bash
npx tsx packages/core/src/cli/commands/shadow.ts drift
```

> monorepo 경로와 스크립트 이름은 제품 버전에 따라 다를 수 있습니다. 최신 엔트리는 `packages/core/src/cliEntry.ts` 와 monorepo 문서를 확인하세요.

## 설정 필드 (요지)

| 필드         | 의미                              |
| ------------ | --------------------------------- |
| `endpoint`   | 섀도 대상 URL                     |
| `sampleRate` | 미러 비율 (0–1)                   |
| `scrubPii`   | PII 스크럽                        |
| `diffMode`   | status / cost / latency 비교 모드 |
| `timeoutMs`  | 섀도 요청 타임아웃                |

## 운영 주의

- 섀도는 **읽기 전용에 가깝게** 설계하세요. mutation이 있는 요청은 샘플링을 낮추거나 제외.
- 비용이 이중으로 나갈 수 있으니 `sampleRate`를 보수적으로.
- 드리프트가 크면 후보 버전을 롤백하거나 토폴로지·프로바이더를 재검토.

## 관련

- [배포](/ko/deployment)
- [프로덕션 준비](/ko/architecture/production-readiness)
- [벤치마크](/ko/guide/benchmarks)
- [문제 해결](/ko/guide/troubleshooting)
