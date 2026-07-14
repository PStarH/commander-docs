# 구성

환경 변수와 선택적 `.commander.json`.

| 변수 | 기본 | 설명 |
|------|------|------|
| `COMMANDER_MODE` | `auto-edit` | plan / read-only / auto-edit / full-auto / suggest |
| `COMMANDER_DEBUG` | `false` | 상세 로그 |
| `COMMANDER_MAX_CONCURRENCY` | `5` | 동시 에이전트 |
| `COMMANDER_TIMEOUT_MS` | `120000` | 타임아웃 |
| `PORT` | `4000` | API |
| `COMMANDER_API_KEY` | — | Bearer |
| `TENANT_PROVIDER` | `null` | multi-tenant 시 `simple` |
| `COMMANDER_SECURITY_PROFILE` | `standard` | 샌드박스 프로필 |

```json
{
  "provider": "auto",
  "model": "auto",
  "topology": "auto",
  "budget": "auto"
}
```

[프로바이더](/ko/guide/providers)
