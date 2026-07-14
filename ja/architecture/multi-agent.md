# マルチエージェント編成

Commander の核心は **5 つの正規トポロジ** で複数エージェントを編成する能力です。Anthropic の “Building effective agents” オントロジーに揃えます。レガシー名 9 つは 2 バージョンの移行ウィンドウ中エイリアスとして残ります。

## 正規トポロジ

| トポロジ         | 説明                             | レガシー別名                      |
| ---------------- | -------------------------------- | --------------------------------- |
| **SINGLE**       | 1 エージェントが全体             | —                                 |
| **CHAIN**        | 順次パイプライン                 | SEQUENTIAL                        |
| **DISPATCH**     | 独立サブタスクを同時実行して合成 | PARALLEL                          |
| **ORCHESTRATOR** | リードが分解・委譲して合成       | HIERARCHICAL / HYBRID             |
| **REVIEW**       | 生成 → 批評 → 洗練               | DEBATE / ENSEMBLE / EVALUATOR-OPT |

## トポロジ選択

審議エンジン（`deliberation.ts`）がタスクを分類し最適トポロジを選びます。

| 複雑度                           | 依存 | 選択         |
| -------------------------------- | ---- | ------------ |
| Trivial                          | なし | SINGLE       |
| Low                              | 順次 | CHAIN        |
| Low                              | 独立 | DISPATCH     |
| Medium                           | 混合 | ORCHESTRATOR |
| High                             | 混合 | ORCHESTRATOR |
| High-risk / Critical / Iterative | 任意 | REVIEW       |

## 詳細

- **SINGLE** — 単純で範囲が明確な依頼
- **CHAIN** — 多段変換、artifact 参照で積み上げ
- **DISPATCH** — 並列可能な独立サブタスク
- **ORCHESTRATOR** — リードが専門家に委譲し合成、適応リルーティング
- **REVIEW** — 独立解を交差検証・洗練

## スケール

`effortScaler.ts`：単純 1 · 中程度 2–5 · 複雑 5–10 · リサーチ 10–20。

## 通信

Message bus · Agent handoff（永続 inbox）· Artifact system · Three-layer memory。

## 関連

- [トポロジ決定木](/ja/guide/usage/topology-decision-tree)
- [エージェントランタイム](/ja/architecture/agent-runtime)
- [コア呼び出しチェーン](/ja/architecture/core-call-chain)
