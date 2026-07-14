# クックブック: リポジトリのセキュリティ監査

**ゴール:** ライブストリーミングと読みやすい findings でマルチエージェントのセキュリティ監査を実行する。

**時間:** 約 10 分 · **リスク:** 読み取り中心（`read-only` または `plan` を推奨）

## 1. 準備

```bash
cd /path/to/Commander   # モノレポルート
export OPENAI_API_KEY=sk-...   # または対応キー
```

学習中は書き込みを制限:

```bash
export COMMANDER_MODE=read-only
```

## 2. まず plan

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repository for security vulnerabilities, secrets, and risky dependencies"
```

**期待:** 分類（多くは ANALYSIS）、複雑度、トポロジ（多くは DISPATCH または REVIEW）、エージェント役割。

## 3. stream で実行

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities, secrets, and risky dependencies" --stream
```

**ストリームで期待すること:**

- 審議バナー（タスク種別 + トポロジ）
- 複数エージェントまたは順次ツール（grep、package audit など）
- 品質ゲート行（ACCURACY / COMPLETENESS / SAFETY …）
- 統合された findings サマリー

## 4. トポロジを固定（任意）

```bash
npx tsx packages/core/src/cliEntry.ts run "audit this repository for security vulnerabilities" --stream --topology review
```

REVIEW は厳しめの検証が欲しいときに produce → critique を強制します。

## 5. 成功チェックリスト

- [ ] Plan がクラッシュせずトポロジを表示
- [ ] Stream にエージェント/ツール活動がある
- [ ] 最終サマリーに具体 findings、または範囲付きの「なし」
- [ ] 説明のないハング（2 分以上イベント 0）がない

## 失敗モード

| 問題             | 対処                                                    |
| ---------------- | ------------------------------------------------------- |
| プロバイダーなし | `doctor`；現在のシェルの env を確認                     |
| 浅い監査         | 実コードパスを指定；プロンプトを具体化                  |
| SAFETY ゲート    | シークレット類似パターンがあれば正常なシグナル          |
| コスト/遅延      | `plan` のみ、または高速プロバイダー（Groq）でトリアージ |

## 関連

- [セキュリティ](/ja/guide/security)
- [トポロジ決定木](/ja/guide/usage/topology-decision-tree)
- [Watch モード](/ja/guide/usage/watch-mode)
