# Web コンソール

可視化コントロール面：ストリーミングチャット、トポロジ、ガバナンス、運用ビュー。

```bash
pnpm gui
```

| サービス | URL |
|----------|-----|
| API | http://localhost:4000 |
| Web (dev) | http://localhost:5173 |
| Web (Docker) | http://localhost:3000 |

## 機能マップ

Dashboard · Chat · Governance · DLQ · Security · Execution · Agents

## ヘルス

```bash
curl http://localhost:4000/health
curl http://localhost:4000/metrics
```

`COMMANDER_API_KEY` 設定時は `Authorization: Bearer …` が必要です。

[トラブルシューティング](/ja/guide/troubleshooting)
