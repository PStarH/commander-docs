#!/usr/bin/env python3
"""Generate zh / ja / ko locale trees from English docs for full coverage.

- Preserves hand-written locale pages (do not overwrite if HAND_WRITTEN marker or
  if path is in PRESERVE lists).
- For other pages: translated title + intro + section map + English body with
  clear localization notice. Code fences are preserved verbatim.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Hand-written locales — never overwrite
PRESERVE = {
    "zh": {
        "zh/index.md",
        "zh/community.md",
        "zh/guide/getting-started.md",
        "zh/guide/why-commander.md",
        "zh/guide/installation.md",
        "zh/guide/web-console.md",
        "zh/guide/faq.md",
        "zh/guide/cookbook/index.md",
        "zh/guide/cookbook/security-audit.md",
    },
    "ja": set(),
    "ko": set(),
}

EN_DIRS = ["guide", "architecture", "api"]
EN_ROOT_FILES = ["community.md", "deployment.md", "benchmarks.md"]

# Common heading / phrase translations
GLOSSARY = {
    "zh": {
        "Quick Start": "快速开始",
        "Installation": "安装",
        "Commands": "命令",
        "Providers": "提供商",
        "Configuration": "配置",
        "Troubleshooting": "故障排除",
        "FAQ": "常见问题",
        "Changelog": "更新日志",
        "Benchmarks": "基准测试",
        "Security": "安全",
        "Deployment": "部署",
        "Community": "社区",
        "Architecture Overview": "架构总览",
        "Overview": "概览",
        "API Reference": "API 参考",
        "Agent SDK": "Agent SDK",
        "Python SDK": "Python SDK",
        "Web Console": "Web 控制台",
        "Why Commander": "为什么选 Commander",
        "Cookbook": "实战手册",
        "Contributing": "贡献指南",
        "Showcase": "案例展示",
        "Next": "下一步",
        "Related": "相关",
        "Prerequisites": "前置要求",
        "Setup": "准备",
        "Usage": "用法",
        "Advanced": "进阶",
        "Failure modes": "失败模式",
        "Success checklist": "成功清单",
        "Getting Started": "入门",
        "Running Tasks": "运行任务",
        "Plan Mode": "计划模式",
        "Watch Mode": "监视模式",
        "Topology Decision Tree": "拓扑决策树",
        "Chaos Testing": "混沌测试",
        "Shadow Traffic": "影子流量",
        "Agent Teams": "代理团队",
        "Custom Providers": "自定义提供商",
        "Custom Tools": "自定义工具",
        "Plugin System": "插件系统",
        "RAG Knowledge Base": "RAG 知识库",
        "V2 Migration": "V2 迁移",
        "Architecture V2 Migration": "架构 V2 迁移",
        "Core Call Chain": "核心调用链",
        "Multi-Agent Orchestration": "多代理编排",
        "Agent Runtime": "代理运行时",
        "Smart Model Router": "智能模型路由",
        "Advanced Features": "高级特性",
        "Resilience": "弹性",
        "Event Sourcing & Recovery": "事件溯源与恢复",
        "Saga Transactions": "Saga 事务",
        "Agent Transaction Runtime": "代理事务运行时",
        "Supervision Tree": "监督树",
        "Backpressure Control": "背压控制",
        "Verification Pipeline": "校验流水线",
        "Caching": "缓存",
        "Speculative Execution": "推测执行",
        "Intelligence Layer": "智能层",
        "Security Gateway": "安全网关",
        "Security Sandbox": "安全沙箱",
        "Multi-Tenancy": "多租户",
        "Tools": "工具",
        "MCP Integration": "MCP 集成",
        "Channel Adapters": "通道适配器",
        "Skills System": "技能系统",
        "Self-Evolution": "自进化",
        "Production Readiness": "生产就绪",
        "Extension Points": "扩展点",
        "Task Complexity Analyzer": "任务复杂度分析器",
        "Adaptive Orchestrator": "自适应编排器",
        "Token Budget Allocator": "Token 预算分配器",
        "Three-Layer Memory": "三层记忆",
        "Reflection Engine": "反思引擎",
        "Consensus Checker": "共识检查器",
        "Inspector Agent": "巡检代理",
        "High-Level Flow": "高层流程",
        "Package Structure": "包结构",
        "Key Design Principles": "关键设计原则",
        "General": "一般",
        "Enterprise": "企业",
        "Performance": "性能",
        "Data & Privacy": "数据与隐私",
        "Reliability SLO Targets": "可靠性 SLO 目标",
        "Health Check Components": "健康检查组件",
        "Chaos Engineering Benchmark": "混沌工程基准",
        "Local development": "本地开发",
        "Docker": "Docker",
        "Production (VM / VPS)": "生产（VM / VPS）",
        "CI/CD": "CI/CD",
        "Verify installation": "验证安装",
        "Success criteria": "成功标准",
        "5-minute checklist": "五分钟清单",
        "What just happened?": "刚刚发生了什么？",
        "Next paths": "下一步路径",
        "If something fails": "如果失败了",
        "At a glance": "一览",
        "When to choose Commander": "何时选择 Commander",
        "vs common approaches": "与常见方案对比",
        "Proof points (honest)": "可验证声明",
        "60-second taste": "60 秒体验",
        "Start": "启动",
        "What you get": "你将获得",
        "Health checks": "健康检查",
        "Auth": "认证",
        "When to use Console vs CLI": "控制台 vs CLI",
        "Reporting vulnerabilities": "漏洞报告",
        "Threat model (summary)": "威胁模型（摘要）",
        "Controls you should configure": "应配置的控制项",
        "Security benchmarks (in monorepo)": "安全基准（monorepo）",
        "Architecture map": "架构地图",
        "Checklist before production": "上线前清单",
        "Layer 1 — Public integration (start here)": "第 1 层 — 公共集成（从这里开始）",
        "Layer 2 — Runtime orchestration components": "第 2 层 — 运行时编排组件",
        "When to use Layer 2": "何时使用第 2 层",
        "When **not** to use Layer 2": "何时**不要**使用第 2 层",
        "Global accessors": "全局访问器",
        "Architecture depth": "架构深度",
        "Related guides": "相关指南",
        "TypeScript SDK": "TypeScript SDK",
        "HTTP (server)": "HTTP（服务端）",
        "Mental model": "心智模型",
        "Feature flags / env": "特性开关 / 环境变量",
        "Route mapping": "路由映射",
        "Storage migration": "存储迁移",
        "Worker sketch": "Worker 示意",
        "Rollout strategy": "发布策略",
        "Read these five first": "先读这五页",
        "Topology Explorer": "拓扑探索器",
        "Interactive Topology Explorer": "交互式拓扑探索器",
    },
    "ja": {
        "Quick Start": "クイックスタート",
        "Installation": "インストール",
        "Commands": "コマンド",
        "Providers": "プロバイダー",
        "Configuration": "設定",
        "Troubleshooting": "トラブルシューティング",
        "FAQ": "FAQ",
        "Changelog": "変更履歴",
        "Benchmarks": "ベンチマーク",
        "Security": "セキュリティ",
        "Deployment": "デプロイ",
        "Community": "コミュニティ",
        "Architecture Overview": "アーキテクチャ概要",
        "Overview": "概要",
        "API Reference": "API リファレンス",
        "Web Console": "Web コンソール",
        "Why Commander": "なぜ Commander か",
        "Cookbook": "クックブック",
        "Contributing": "コントリビュート",
        "Showcase": "ショーケース",
        "Next": "次へ",
        "Related": "関連",
        "Prerequisites": "前提条件",
        "Setup": "セットアップ",
        "Usage": "使い方",
        "Advanced": "高度な話題",
        "Failure modes": "失敗モード",
        "Success checklist": "成功チェックリスト",
        "Getting Started": "はじめに",
        "Running Tasks": "タスク実行",
        "Plan Mode": "プランモード",
        "Watch Mode": "ウォッチモード",
        "Topology Decision Tree": "トポロジ決定木",
        "Chaos Testing": "カオステスト",
        "Shadow Traffic": "シャドートラフィック",
        "Agent Teams": "エージェントチーム",
        "Custom Providers": "カスタムプロバイダー",
        "Custom Tools": "カスタムツール",
        "Plugin System": "プラグインシステム",
        "RAG Knowledge Base": "RAG ナレッジベース",
        "V2 Migration": "V2 移行",
        "Architecture V2 Migration": "アーキテクチャ V2 移行",
        "Core Call Chain": "コア呼び出しチェーン",
        "Multi-Agent Orchestration": "マルチエージェント編成",
        "Agent Runtime": "エージェントランタイム",
        "Smart Model Router": "スマートモデルルーター",
        "Advanced Features": "高度な機能",
        "Resilience": "レジリエンス",
        "Event Sourcing & Recovery": "イベントソーシングと復旧",
        "Saga Transactions": "Saga トランザクション",
        "Agent Transaction Runtime": "エージェントトランザクションランタイム",
        "Supervision Tree": "スーパービジョンツリー",
        "Backpressure Control": "バックプレッシャー制御",
        "Verification Pipeline": "検証パイプライン",
        "Caching": "キャッシュ",
        "Speculative Execution": "投機的実行",
        "Intelligence Layer": "インテリジェンス層",
        "Security Gateway": "セキュリティゲートウェイ",
        "Security Sandbox": "セキュリティサンドボックス",
        "Multi-Tenancy": "マルチテナンシー",
        "Tools": "ツール",
        "MCP Integration": "MCP 統合",
        "Channel Adapters": "チャネルアダプター",
        "Skills System": "スキルシステム",
        "Self-Evolution": "自己進化",
        "Production Readiness": "本番準備",
        "Extension Points": "拡張ポイント",
        "Task Complexity Analyzer": "タスク複雑度アナライザー",
        "Adaptive Orchestrator": "適応型オーケストレーター",
        "Token Budget Allocator": "トークン予算アロケーター",
        "Three-Layer Memory": "3 層メモリ",
        "Reflection Engine": "リフレクションエンジン",
        "Consensus Checker": "コンセンサスチェッカー",
        "Inspector Agent": "インスペクターエージェント",
        "High-Level Flow": "ハイレベルフロー",
        "Package Structure": "パッケージ構成",
        "Key Design Principles": "設計原則",
        "General": "一般",
        "Enterprise": "エンタープライズ",
        "Performance": "パフォーマンス",
        "Data & Privacy": "データとプライバシー",
        "Local development": "ローカル開発",
        "Docker": "Docker",
        "CI/CD": "CI/CD",
        "Verify installation": "インストール検証",
        "Success criteria": "成功条件",
        "5-minute checklist": "5 分チェックリスト",
        "What just happened?": "何が起きたか",
        "Next paths": "次のパス",
        "If something fails": "失敗したら",
        "At a glance": "一覧",
        "When to choose Commander": "Commander を選ぶとき",
        "Proof points (honest)": "検証可能な主張",
        "60-second taste": "60 秒体験",
        "Start": "起動",
        "What you get": "できること",
        "Health checks": "ヘルスチェック",
        "Auth": "認証",
        "Reporting vulnerabilities": "脆弱性の報告",
        "Threat model (summary)": "脅威モデル（要約）",
        "Controls you should configure": "設定すべき制御",
        "Architecture map": "アーキテクチャマップ",
        "Checklist before production": "本番前チェックリスト",
        "Layer 1 — Public integration (start here)": "レイヤー 1 — 公開統合（ここから）",
        "Layer 2 — Runtime orchestration components": "レイヤー 2 — ランタイム編成コンポーネント",
        "Global accessors": "グローバルアクセサ",
        "Related guides": "関連ガイド",
        "Mental model": "メンタルモデル",
        "Route mapping": "ルート対応",
        "Storage migration": "ストレージ移行",
        "Rollout strategy": "ロールアウト戦略",
        "Read these five first": "まずこの 5 ページ",
        "Topology Explorer": "トポロジエクスプローラー",
        "Interactive Topology Explorer": "対話型トポロジエクスプローラー",
    },
    "ko": {
        "Quick Start": "빠른 시작",
        "Installation": "설치",
        "Commands": "명령",
        "Providers": "프로바이더",
        "Configuration": "구성",
        "Troubleshooting": "문제 해결",
        "FAQ": "FAQ",
        "Changelog": "변경 로그",
        "Benchmarks": "벤치마크",
        "Security": "보안",
        "Deployment": "배포",
        "Community": "커뮤니티",
        "Architecture Overview": "아키텍처 개요",
        "Overview": "개요",
        "API Reference": "API 참조",
        "Web Console": "웹 콘솔",
        "Why Commander": "왜 Commander인가",
        "Cookbook": "쿡북",
        "Contributing": "기여",
        "Showcase": "쇼케이스",
        "Next": "다음",
        "Related": "관련",
        "Prerequisites": "사전 요구사항",
        "Setup": "설정",
        "Usage": "사용법",
        "Advanced": "고급",
        "Failure modes": "실패 모드",
        "Success checklist": "성공 체크리스트",
        "Getting Started": "시작하기",
        "Running Tasks": "작업 실행",
        "Plan Mode": "플랜 모드",
        "Watch Mode": "워치 모드",
        "Topology Decision Tree": "토폴로지 결정 트리",
        "Chaos Testing": "카오스 테스트",
        "Shadow Traffic": "섀도 트래픽",
        "Agent Teams": "에이전트 팀",
        "Custom Providers": "커스텀 프로바이더",
        "Custom Tools": "커스텀 도구",
        "Plugin System": "플러그인 시스템",
        "RAG Knowledge Base": "RAG 지식 베이스",
        "V2 Migration": "V2 마이그레이션",
        "Architecture V2 Migration": "아키텍처 V2 마이그레이션",
        "Core Call Chain": "핵심 호출 체인",
        "Multi-Agent Orchestration": "멀티 에이전트 오케스트레이션",
        "Agent Runtime": "에이전트 런타임",
        "Smart Model Router": "스마트 모델 라우터",
        "Advanced Features": "고급 기능",
        "Resilience": "복원력",
        "Event Sourcing & Recovery": "이벤트 소싱 및 복구",
        "Saga Transactions": "Saga 트랜잭션",
        "Agent Transaction Runtime": "에이전트 트랜잭션 런타임",
        "Supervision Tree": "슈퍼비전 트리",
        "Backpressure Control": "백프레셔 제어",
        "Verification Pipeline": "검증 파이프라인",
        "Caching": "캐싱",
        "Speculative Execution": "추측 실행",
        "Intelligence Layer": "인텔리전스 레이어",
        "Security Gateway": "보안 게이트웨이",
        "Security Sandbox": "보안 샌드박스",
        "Multi-Tenancy": "멀티 테넌시",
        "Tools": "도구",
        "MCP Integration": "MCP 통합",
        "Channel Adapters": "채널 어댑터",
        "Skills System": "스킬 시스템",
        "Self-Evolution": "자가 진화",
        "Production Readiness": "프로덕션 준비",
        "Extension Points": "확장 지점",
        "Task Complexity Analyzer": "작업 복잡도 분석기",
        "Adaptive Orchestrator": "적응형 오케스트레이터",
        "Token Budget Allocator": "토큰 예산 할당기",
        "Three-Layer Memory": "3계층 메모리",
        "Reflection Engine": "리플렉션 엔진",
        "Consensus Checker": "합의 검사기",
        "Inspector Agent": "인스펙터 에이전트",
        "High-Level Flow": "고수준 흐름",
        "Package Structure": "패키지 구조",
        "Key Design Principles": "핵심 설계 원칙",
        "General": "일반",
        "Enterprise": "엔터프라이즈",
        "Performance": "성능",
        "Data & Privacy": "데이터 및 개인정보",
        "Local development": "로컬 개발",
        "Docker": "Docker",
        "CI/CD": "CI/CD",
        "Verify installation": "설치 검증",
        "Success criteria": "성공 기준",
        "5-minute checklist": "5분 체크리스트",
        "What just happened?": "방금 무슨 일이?",
        "Next paths": "다음 경로",
        "If something fails": "실패할 때",
        "At a glance": "한눈에",
        "When to choose Commander": "Commander를 선택해야 할 때",
        "Proof points (honest)": "검증 가능한 주장",
        "60-second taste": "60초 체험",
        "Start": "시작",
        "What you get": "제공 기능",
        "Health checks": "헬스 체크",
        "Auth": "인증",
        "Reporting vulnerabilities": "취약점 보고",
        "Threat model (summary)": "위협 모델(요약)",
        "Controls you should configure": "구성해야 할 제어",
        "Architecture map": "아키텍처 맵",
        "Checklist before production": "프로덕션 전 체크리스트",
        "Layer 1 — Public integration (start here)": "레이어 1 — 공개 통합(여기서 시작)",
        "Layer 2 — Runtime orchestration components": "레이어 2 — 런타임 오케스트레이션 컴포넌트",
        "Global accessors": "전역 액세서",
        "Related guides": "관련 가이드",
        "Mental model": "멘탈 모델",
        "Route mapping": "라우트 매핑",
        "Storage migration": "스토리지 마이그레이션",
        "Rollout strategy": "롤아웃 전략",
        "Read these five first": "먼저 이 다섯 페이지",
        "Topology Explorer": "토폴로지 탐색기",
        "Interactive Topology Explorer": "대화형 토폴로지 탐색기",
    },
}

BANNER = {
    "zh": (
        "> **本地化说明** · 本页标题与结构已本地化；代码块与精确 API 以英文源为准。"
        "完整英文版：[English]({en_link})\n"
    ),
    "ja": (
        "> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。"
        "英語版：[English]({en_link})\n"
    ),
    "ko": (
        "> **현지화 안내** · 제목/구조는 번역되었습니다. 코드와 정확한 API는 영어 원문을 기준으로 하세요."
        "영어 버전: [English]({en_link})\n"
    ),
}

INDEX = {
    "zh": "---\nlayout: page\n---\n\n<Home />\n",
    "ja": "---\nlayout: page\n---\n\n<Home />\n",
    "ko": "---\nlayout: page\n---\n\n<Home />\n",
}

# Hand-written JA/KO entry pages (full quality)
ENTRY_PAGES = {
    "ja": {
        "guide/getting-started.md": """# クイックスタート

約 5 分で Commander を動かします。API キーは 1 つ。グラフビルダーも YAML も不要です。

## 成功条件

1. `pnpm install` がエラーなく終わる  
2. タスクを実行し **審議 (deliberation) + トポロジ** が見える  
3. プロセスが正常終了する（または `doctor` が明確なエラーを返す）

## 前提条件

- **Node.js** 18+（22 推奨）  
- **pnpm** 8+（9+ 推奨）  
- いずれか 1 つの LLM API キー  

> monorepo のため **pnpm** を使ってください。

## 5 分チェックリスト

### 1. クローンとインストール

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

### 2. API キー

```bash
export OPENAI_API_KEY=sk-...
# または ANTHROPIC_API_KEY / DEEPSEEK_API_KEY / GROQ_API_KEY / ...
```

### 3. plan（安全）

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
```

### 4. stream 実行

```bash
npx tsx packages/core/src/cliEntry.ts run "explain the architecture of this repository" --stream
```

### 5. Web コンソール（任意）

```bash
pnpm gui
# API :4000 · Web 開発時は多くが :5173
```

### 6. Docker（任意）

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
```

## 失敗したら

| 症状 | 対処 |
|------|------|
| Provider not available | 現在の shell で key を `export`、`doctor` を実行 |
| モジュール解決エラー | リポジトリルートで pnpm install / build |
| ハング | まず `plan`、`COMMANDER_DEBUG=true` |
| オフライン | `export OLLAMA_BASE_URL=http://localhost:11434` |

## 次へ

- [なぜ Commander か](/ja/guide/why-commander)  
- [英語ドキュメント全文](/guide/getting-started)  
- [アーキテクチャ](/ja/architecture/overview)  
""",
        "guide/why-commander.md": """# なぜ Commander か

Commander は、マルチエージェントを **ブラックボックスにしたくないエンジニア** 向けです。

**グラフビルダーなし。YAML なし。祈らない。**  
キー 1 つ → タスク分類 → トポロジ選択 → 全決定をストリーム → 出力を検証。

## 一覧

| 観点 | Commander | 典型的なフレームワーク |
|------|-----------|------------------------|
| 始め方 | 自然言語 + キー 1 つ | グラフ / YAML を組む |
| トポロジ | 5 種を自動選択 | 自分で辺を張る |
| 可視性 | ライブ SSE | 事後ログ |
| 品質 | 5 層ゲート | 任意 / DIY |
| プロバイダー | 25 + フェイルオーバー | 1–2 が中心 |
| 本番 | ブレーカー、DLQ、Saga、WAL | デモ優先 |

## 60 秒体験

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "explain this repository architecture" --stream
```

- [クイックスタート](/ja/guide/getting-started)  
- [英語版 Why](/guide/why-commander)  
""",
        "guide/faq.md": """# FAQ

## Commander とは？

5 つの正規トポロジで複数 AI エージェントを編成するエンジンです。25 プロバイダー、18 組み込みツール。

## 普通の AI コーディングツールとの違いは？

単一エージェントではなく、**自動トポロジ・ライブストリーム・品質ゲート・本番向け基盤** を備えます。

## オープンソース？

はい、MIT。

## API キーは複数必要？

いいえ。**1 つで十分**。複数設定するとフェイルオーバーが働きます。

## オフラインは？

Ollama / vLLM:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```

## CI で使える？

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors"
```

詳細は [英語 FAQ](/guide/faq)。
""",
        "guide/installation.md": """# インストール

## 前提

- Node.js 18+  
- pnpm 8+  
- LLM API キー 1 つ  

## ローカル

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

## Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
# API :4000 · Web :3000
```

[英語 Deployment](/deployment) · [クイックスタート](/ja/guide/getting-started)
""",
        "guide/web-console.md": """# Web コンソール

可視化コントロール面：ストリーミングチャット、トポロジ、ガバナンス、運用ビュー。

```bash
pnpm gui
# API http://localhost:4000 · Web 多くは :5173
```

| 領域 | 用途 |
|------|------|
| Dashboard | レポート、トークン、トポロジ |
| Chat | リアルタイムエージェント対話 |
| Governance | 承認・ポリシー・監査 |
| DLQ | デッドレターの確認と再生 |

[英語 Web Console](/guide/web-console)
""",
        "community.md": """# コミュニティ

Commander は MIT のオープンソースです。

| チャネル | 状態 | リンク |
|----------|------|--------|
| GitHub | 公開 | [PStarH/Commander](https://github.com/PStarH/Commander) |
| Docs | 公開 | このサイト |
| Discord / Twitter | 予定 | リポジトリの告知をフォロー |

貢献: `pnpm install` 後テスト全緑。セキュリティ報告は公開 Issue ではなく [Security](/guide/security)。

日本語エントリ: [クイックスタート](/ja/guide/getting-started)
""",
        "guide/cookbook/index.md": """# クックブック

| レシピ | 内容 |
|--------|------|
| [英語: Security audit](/guide/cookbook/security-audit) | ストリーミング監査 |
| [英語: Refactor](/guide/cookbook/refactor-module) | plan → run |
| [英語: CI full-auto](/guide/cookbook/ci-full-auto) | CI で lint 修正 |

まずは [クイックスタート](/ja/guide/getting-started)。
""",
    },
    "ko": {
        "guide/getting-started.md": """# 빠른 시작

약 5분 안에 Commander를 실행합니다. API 키 하나. 그래프 빌더·YAML 없음.

## 성공 기준

1. `pnpm install` 성공  
2. 작업 실행 후 **심의(deliberation) + 토폴로지** 확인  
3. 정상 종료 또는 `doctor`의 명확한 오류  

## 사전 요구사항

- **Node.js** 18+ (22 권장)  
- **pnpm** 8+  
- LLM API 키 하나  

> monorepo이므로 **pnpm**을 사용하세요.

## 5분 체크리스트

### 1. 클론 및 설치

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
```

### 2. API 키

```bash
export OPENAI_API_KEY=sk-...
```

### 3. plan

```bash
npx tsx packages/core/src/cliEntry.ts plan "audit this repo for security vulnerabilities"
```

### 4. stream 실행

```bash
npx tsx packages/core/src/cliEntry.ts run "explain the architecture of this repository" --stream
```

### 5. 웹 콘솔(선택)

```bash
pnpm gui
```

### 6. Docker(선택)

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
```

## 실패 시

| 증상 | 조치 |
|------|------|
| Provider not available | 현재 셸에 key export, `doctor` |
| 모듈 오류 | 루트에서 pnpm install/build |
| 멈춤 | `plan` 먼저, `COMMANDER_DEBUG=true` |
| 오프라인 | `OLLAMA_BASE_URL=http://localhost:11434` |

## 다음

- [왜 Commander인가](/ko/guide/why-commander)  
- [영문 문서](/guide/getting-started)  
- [아키텍처](/ko/architecture/overview)  
""",
        "guide/why-commander.md": """# 왜 Commander인가

Commander는 멀티 에이전트를 **블랙박스로 두지 않으려는 엔지니어**를 위한 제품입니다.

**그래프 빌더 없음. YAML 없음.**  
키 하나 → 작업 분류 → 토폴로지 선택 → 모든 결정을 스트림 → 출력 검증.

## 한눈에

| 항목 | Commander | 일반 프레임워크 |
|------|-----------|-----------------|
| 시작 | 자연어 + 키 하나 | 그래프/YAML 작성 |
| 토폴로지 | 5종 자동 선택 | 직접 연결 |
| 가시성 | 라이브 SSE | 사후 로그 |
| 품질 | 5계층 게이트 | 선택/자체 구현 |
| 프로바이더 | 25 + 페일오버 | 1–2개 중심 |
| 프로덕션 | 서킷브레이커, DLQ, Saga, WAL | 데모 우선 |

## 60초 체험

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "explain this repository architecture" --stream
```

- [빠른 시작](/ko/guide/getting-started)  
- [영문 Why](/guide/why-commander)  
""",
        "guide/faq.md": """# FAQ

## Commander란?

5개 정규 토폴로지로 여러 AI 에이전트를 조율하는 엔진입니다. 25 프로바이더, 18 내장 도구.

## 일반 AI 코딩 도구와 차이는?

단일 에이전트가 아니라 **자동 토폴로지·라이브 스트림·품질 게이트·프로덕션 인프라**를 제공합니다.

## 오픈소스?

네, MIT.

## API 키가 여러 개 필요?

아니요. **하나면 충분**합니다.

## 오프라인?

```bash
export OLLAMA_BASE_URL=http://localhost:11434
npx tsx packages/core/src/cliEntry.ts run "analyze this code"
```

## CI?

```bash
export COMMANDER_MODE=full-auto
npx tsx packages/core/src/cliEntry.ts run "fix all lint errors"
```

자세한 내용: [영문 FAQ](/guide/faq).
""",
        "guide/installation.md": """# 설치

## 사전 요구

- Node.js 18+  
- pnpm 8+  
- LLM API 키 하나  

## 로컬

```bash
git clone https://github.com/PStarH/Commander.git
cd Commander
pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream
```

## Docker

```bash
export COMMANDER_API_KEY="your-secret-key"
export OPENAI_API_KEY="sk-..."
docker compose up -d
```

[영문 Deployment](/deployment) · [빠른 시작](/ko/guide/getting-started)
""",
        "guide/web-console.md": """# 웹 콘솔

시각적 제어면: 스트리밍 채팅, 토폴로지, 거버넌스, 운영 뷰.

```bash
pnpm gui
```

| 영역 | 용도 |
|------|------|
| Dashboard | 리포트, 토큰, 토폴로지 |
| Chat | 실시간 에이전트 대화 |
| Governance | 승인·정책·감사 |
| DLQ | 데드레터 조회/재생 |

[영문 Web Console](/guide/web-console)
""",
        "community.md": """# 커뮤니티

Commander는 MIT 오픈소스입니다.

| 채널 | 상태 | 링크 |
|------|------|------|
| GitHub | 활성 | [PStarH/Commander](https://github.com/PStarH/Commander) |
| Docs | 활성 | 이 사이트 |
| Discord / Twitter | 예정 | 저장소 공지 |

보안 취약점은 공개 이슈가 아니라 [Security](/guide/security)를 따르세요.

한국어 입구: [빠른 시작](/ko/guide/getting-started)
""",
        "guide/cookbook/index.md": """# 쿡북

| 레시피 | 내용 |
|--------|------|
| [영문: Security audit](/guide/cookbook/security-audit) | 스트리밍 감사 |
| [영문: Refactor](/guide/cookbook/refactor-module) | plan → run |
| [영문: CI full-auto](/guide/cookbook/ci-full-auto) | CI lint 수정 |

먼저 [빠른 시작](/ko/guide/getting-started).
""",
    },
}


def en_pages() -> list[Path]:
    out: list[Path] = []
    for d in EN_DIRS:
        out.extend(sorted(Path(ROOT, d).rglob("*.md")))
    for f in EN_ROOT_FILES:
        p = ROOT / f
        if p.exists():
            out.append(p)
    # topology explorer (new EN page)
    te = ROOT / "guide" / "topology-explorer.md"
    if te.exists():
        out.append(te)
    return out


def en_link_for(rel: str) -> str:
    # rel like guide/foo.md -> /guide/foo
    if rel.endswith("/index.md"):
        return "/" + rel[: -len("index.md")]
    if rel.endswith(".md"):
        return "/" + rel[:-3]
    return "/" + rel


def translate_heading(title: str, locale: str) -> str:
    g = GLOSSARY.get(locale, {})
    if title in g:
        return g[title]
    # try without punctuation variants
    t = title.strip()
    if t in g:
        return g[t]
    return title


def localize_markdown(body: str, locale: str, en_rel: str) -> str:
    """Translate # / ## / ### headings via glossary; keep rest."""
    g = GLOSSARY.get(locale, {})
    lines = body.splitlines(keepends=True)
    out = []
    in_code = False
    for line in lines:
        if line.startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        if not in_code:
            m = re.match(r"^(#{1,6})\s+(.+?)(\s*#*\s*)$", line)
            if m:
                level, title, trail = m.group(1), m.group(2).strip(), m.group(3)
                # strip trailing custom anchors {#...}
                title_clean = re.sub(r"\s*\{#.*\}$", "", title)
                tr = g.get(title_clean, title_clean)
                out.append(f"{level} {tr}{trail if trail.startswith(chr(10)) else ''}\n" if not trail.strip() else f"{level} {tr}\n")
                continue
            # internal links: keep as-is (point to EN or same structure under locale later)
        out.append(line)
    text = "".join(out)
    # rewrite absolute guide/architecture/api links to locale prefix when possible
    def repl_link(m):
        path = m.group(1)
        if path.startswith(("http", "mailto", "#")):
            return m.group(0)
        if path.startswith(("/guide/", "/architecture/", "/api/", "/deployment", "/community", "/benchmarks")):
            # /guide/foo -> /zh/guide/foo
            return f"](/{locale}{path})"
        return m.group(0)

    text = re.sub(r"\]\(([^)]+)\)", lambda m: repl_link(m) if False else (
        f"](/{locale}{m.group(1)})" if m.group(1).startswith(("/guide/", "/architecture/", "/api/")) and not m.group(1).startswith(f"/{locale}/") else m.group(0)
    ), text)
    # simpler second pass
    for prefix in ("/guide/", "/architecture/", "/api/"):
        text = text.replace(f"]({prefix}", f"](/{locale}{prefix}")
    text = text.replace(f"](/{locale}/deployment)", "](/deployment)")  # root pages handled below
    # deployment/community/benchmarks at root
    text = re.sub(rf"\]\(/{locale}/(deployment|community|benchmarks)\)", r"](/\1)", text)
    text = text.replace("](/deployment)", f"](/{locale}/deployment)")
    text = text.replace("](/community)", f"](/{locale}/community)")
    text = text.replace("](/benchmarks)", f"](/{locale}/benchmarks)")

    banner = BANNER[locale].format(en_link=en_link_for(en_rel))
    # insert banner after first H1
    parts = text.split("\n", 1)
    if parts and parts[0].startswith("# "):
        rest = parts[1] if len(parts) > 1 else ""
        return parts[0] + "\n\n" + banner + "\n" + rest
    return banner + "\n" + text


def write_locale_page(locale: str, en_path: Path) -> None:
    rel = str(en_path.relative_to(ROOT)).replace("\\", "/")
    dest_rel = f"{locale}/{rel}"
    if dest_rel in PRESERVE.get(locale, set()):
        return
    dest = ROOT / dest_rel
    dest.parent.mkdir(parents=True, exist_ok=True)

    # entry hand pages
    if rel in ENTRY_PAGES.get(locale, {}):
        dest.write_text(ENTRY_PAGES[locale][rel], encoding="utf-8")
        return

    src = en_path.read_text(encoding="utf-8")
    # Translate H1 via glossary if known
    m = re.match(r"^#\s+(.+)$", src, re.M)
    if m:
        h1 = m.group(1).strip()
        tr = translate_heading(h1, locale)
        if tr != h1:
            src = src.replace(f"# {h1}", f"# {tr}", 1)

    localized = localize_markdown(src, locale, rel)
    dest.write_text(localized, encoding="utf-8")


def main() -> None:
    pages = en_pages()
    print(f"EN pages: {len(pages)}")
    for locale in ("zh", "ja", "ko"):
        # index
        idx = ROOT / locale / "index.md"
        idx.parent.mkdir(parents=True, exist_ok=True)
        if str(idx.relative_to(ROOT)) not in PRESERVE.get(locale, set()) or not idx.exists():
            if locale != "zh" or not idx.exists():
                # zh index already hand-written — only write if missing
                if not idx.exists():
                    idx.write_text(INDEX[locale], encoding="utf-8")
        if locale in ("ja", "ko"):
            idx.write_text(INDEX[locale], encoding="utf-8")

        n = 0
        for p in pages:
            write_locale_page(locale, p)
            n += 1
        # ensure entry pages even if not in en list path form
        for rel, content in ENTRY_PAGES.get(locale, {}).items():
            dest = ROOT / locale / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")
        print(f"{locale}: wrote/updated tree ({n} en mirrors + entry pages)")


if __name__ == "__main__":
    main()
