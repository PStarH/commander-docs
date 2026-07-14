# クックブック: モジュールを安全にリファクタ

**ゴール:** plan モードでリファクタをプレビューし、制御された承認で実行する。

**時間:** 約 15 分 · **リスク:** ファイル書き込み — `plan` / `suggest` から

## 1. 準備

```bash
cd /path/to/your-project   # または dry-run 用 Commander モノレポ
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=plan
```

実アプリに対してはクリーンなブランチ:

```bash
git checkout -b chore/commander-refactor
git status
```

## 2. plan をプレビュー

```bash
npx tsx packages/core/src/cliEntry.ts plan "refactor the authentication module to reduce duplication; keep public API stable"
```

**期待:** トポロジ（多くは CHAIN または ORCHESTRATOR）、手順、ツール、予算 — **ファイル編集なし**。

確認:

- 意図したモジュールだけか？
- リスクの高い変更なら REVIEW が適切か？

## 3. suggest モード（人が介在）

```bash
export COMMANDER_MODE=suggest
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module to reduce duplication; keep public API stable" --stream
```

モードに応じてターミナルの承認プロンプトで編集を許可/拒否します。

## 4. auto-edit（plan を信頼できるとき）

```bash
export COMMANDER_MODE=auto-edit
npx tsx packages/core/src/cliEntry.ts run "refactor the authentication module to reduce duplication; keep public API stable" --stream
```

## 5. ローカル検証

```bash
git diff
# プロジェクト固有:
pnpm test   # または npm test / cargo test / など
```

## 6. 成功チェックリスト

- [ ] 書き込み前に plan が妥当
- [ ] diff が意図ファイルに限定
- [ ] テスト / 型チェック通過
- [ ] 必要なら `git checkout -- .` で戻せる

## 失敗モード

| 問題                           | 対処                                            |
| ------------------------------ | ----------------------------------------------- |
| 過剰な編集                     | `plan` / `suggest` のまま；プロンプト範囲を縮小 |
| モジュール違い                 | パスを明示: `packages/foo/src/auth/*`           |
| 不安定なマルチエージェント結合 | `--topology chain` または `--topology review`   |

## 関連

- [Plan モード](/ja/guide/usage/plan-mode)
- [タスク実行](/ja/guide/usage/running-tasks)
- [FAQ の承認モード](/ja/guide/faq)
