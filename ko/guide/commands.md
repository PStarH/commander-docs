# CLI 명령

빌드 후 `commander`. 소스:

```bash
npx tsx packages/core/src/cliEntry.ts
```

## 실행

| 명령 | 설명 |
|------|------|
| `run <task>` | 전체 multi-agent 실행 |
| `plan <task>` | 심의 플랜 |
| `run <task> --stream` | SSE 스트림 |
| `run --file tasks.json` | 배치 |
| `swarm` / `drive` / `goal` / `company` | 고급 모드 |

## UI · 설정

`gui` · `tui` · `web` · `mode` · `config` · `doctor` · `budget` · `status` · `--debug`

## 승인 모드

`plan` · `read-only` · `suggest` · `auto-edit` · `full-auto`
