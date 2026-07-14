# Inspector Agent

ランタイム健全性・異常・設定ドリフトを検知するインスペクタです。運用ダッシュボードや doctor フローと併用します。

## 役割

- プロバイダー / ブレーカー / DLQ の異常シグナル  
- 長時間 stuck run の検出  
- 設定・権限のざっくり健全性チェック  

## 使い方（概念）

```typescript
import { getGlobalInspectorAgent } from '@commander/core';

const inspector = getGlobalInspectorAgent();
const report = await inspector.inspect({ tenantId: 'default' });
// report.issues[] — severity, code, recommendation
```

CLI ではまず:

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
```

## いつ使うか

- Layer 2 拡張・社内 ops ツール  
- 通常のタスク実行だけなら CLI doctor + Web Console で足りる  

## 関連

- [API 概要](/ja/api/overview)  
- [Resilience](/ja/architecture/resilience)  
- [トラブルシューティング](/ja/guide/troubleshooting)  
