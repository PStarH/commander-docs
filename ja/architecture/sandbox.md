# セキュリティ・サンドボックス

Commander のサンドボックスはすべての実行を隔離し、Petri net スケジューラで資源を形式的に割り当てます。

## 構造

```
sandbox/
├── execPolicy.ts / approval.ts / profiles.ts / platforms.ts
├── manager.ts / executionRouter.ts / lane.ts
├── seccompBpf.ts / teeEnclave.ts / petriNetScheduler.ts
├── networkProxy.ts / backends/ (local, ssh, docker)
└── types.ts
```

## セキュリティ・プロファイル

| プロファイル | Shell | 書き込み | ネットワーク | 用途 |
|--------------|-------|----------|--------------|------|
| **READ_ONLY** | なし | 読み取りのみ | 遮断 | レビュー、非信頼入力 |
| **WORKSPACE_WRITE** | サンドボックス可 | プロジェクト | 可 | 開発 |
| **FULL_ACCESS** | 全面 | 任意 | 可 | CI/CD |
| **HARDENED** | なし | 拒否 | 遮断 | 非信頼コード |

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

## Petri Net スケジューラ

| Place | 容量 | 用途 |
|-------|------|------|
| `pending` | 無制限 | 待機 |
| `v8_slots` | 10 | V8 isolate |
| `seccomp_slots` | 4 | seccomp-BPF |
| `wasm_slots` | 2 | WASM |
| `tee_slots` | 1 | TEE |
| `executing` / `completed` | 無制限 | 実行中 / 完了 |

遷移 `admit_*` / `complete_*`。デッドロック・飽和・安全状態を解析してから入場。

## バックエンド

local · ssh · docker。

## 運用

```bash
export COMMANDER_MODE=read-only
npx tsx packages/core/src/cliEntry.ts plan "audit this repo"
```

非信頼コードには HARDENED + ネットワーク遮断を既定に。

## 関連

- [セキュリティ](/ja/guide/security)  
- [セキュリティゲートウェイ](/ja/architecture/security-gateway)  
- [ツール](/ja/architecture/tools)  
