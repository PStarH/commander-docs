# Shadow Traffic

Shadow traffic lets you compare two versions of Commander side-by-side without affecting production. A shadow proxy mirrors production requests to a shadow endpoint and reports drift in status, latency, and cost. - **Pre-deploy validation** — Compare current vs candidate version before rollout

本ページは Commander における **Shadow Traffic** の役割と使い方を説明します。CLI / API は monorepo と一致させています。

```bash
cat > .commander/shadow-config.json <<EOF
{
  "enabled": true,
  "endpoint": "http://localhost:9999",
  "sampleRate": 0.1,
  "scrubPii": true,
  "diffMode": "status_cost_latency",
  "timeoutMs": 5000
```

## 要点

- 指標: 25 プロバイダー · 5 トポロジ · 18 ツール · 6700+ テスト  
- 実行例は [クイックスタート](/ja/guide/getting-started) の `cliEntry.ts` を使用  

## 関連

- [アーキテクチャ](/ja/architecture/overview)  
- [クイックスタート](/ja/guide/getting-started)  
- [API](/ja/api/overview)  
