# クックブック: CI フルオート lint 修正

**ゴール:** CI で非対話的に Commander を走らせ、lint（など）を直す。

**時間:** 配線 ~15 分 · **リスク:** 高い自律性 — PR レビュー付きジョブに隔離

## CI 設計ルール

1. **使い捨てブランチ** または PR ワークフロー — エージェントが main に force-push しない
2. ジョブに必要な **シークレットだけ** export
3. サンプルリポジトリで dry-run してからだけ `COMMANDER_MODE=full-auto`
4. ログを CI アーティファクトとして保存

## 1. ローカル dry-run

```bash
export OPENAI_API_KEY=sk-...
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors in this repository" --stream
```

exit code と git diff が許容できるか確認します。

## 2. GitHub Actions スケッチ

```yaml
name: Commander lint fix
on:
  workflow_dispatch:
  # または schedule / pull_request

jobs:
  fix:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 9
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: pnpm
      - name: Install Commander
        run: |
          git clone --depth 1 https://github.com/PStarH/Commander.git /tmp/Commander
          cd /tmp/Commander && pnpm install
      - name: Run Commander
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          COMMANDER_MODE: full-auto
        run: |
          cd $GITHUB_WORKSPACE
          npx tsx /tmp/Commander/packages/core/src/cliEntry.ts run "fix all lint errors" --stream
      - name: Show diff
        run: git diff --stat
```

submodule や（将来の）公開パッケージで vendor する場合はパスを合わせてください。**現在の主経路は monorepo clone です。**

## 3. 成功チェックリスト

- [ ] ジョブが非対話（TTY プロンプトなし）
- [ ] ログに審議 + ストリーム
- [ ] merge 前に人が diff をレビュー
- [ ] シークレットがログに出ない

## 失敗モード

| 問題         | 対処                                                     |
| ------------ | -------------------------------------------------------- |
| 対話でハング | `full-auto`；承認プロンプトを無効化                      |
| レート制限   | ジョブを直列化；キャッシュ；プロンプト範囲を縮小         |
| 破壊的編集   | プロンプトを狭める（“eslint only”、path globs）；PR 必須 |

## 関連

- [FAQ — CI/CD](/ja/guide/faq)
- [デプロイ](/ja/deployment)
- [トラブルシューティング](/ja/guide/troubleshooting)
