<script setup lang="ts">
import { computed, onMounted, onBeforeUnmount } from 'vue'
import { withBase, useData } from 'vitepress'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

const { lang } = useData()
const locale = computed<'en' | 'zh' | 'ja' | 'ko' | 'es' | 'fr'>(() => {
  const l = lang.value || 'en'
  if (l.startsWith('zh')) return 'zh'
  if (l.startsWith('ja')) return 'ja'
  if (l.startsWith('ko')) return 'ko'
  if (l.startsWith('es')) return 'es'
  if (l.startsWith('fr')) return 'fr'
  return 'en'
})
const locPrefix = computed(() => (locale.value === 'en' ? '' : `/${locale.value}`))

const featureIcons = {
  wide1: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h4l3-7 4 14 3-7h4"/></svg>`,
  tall1: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l9 9-9 9-9-9z"/><circle cx="12" cy="12" r="2" fill="currentColor"/></svg>`,
  short1: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 0 1 14-5"/><path d="M20 12a8 8 0 0 1-14 5"/><path d="M18 4v4h-4M6 20v-4h4"/></svg>`,
  short2: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5 9-11"/></svg>`,
  tall2: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 0 1 13-6"/><path d="M20 12a8 8 0 0 1-13 6"/><path d="M3 6h4v4M21 18h-4v-4"/></svg>`,
  wide2: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 4v5c0 5-4 8-8 9-4-1-8-4-8-9V7z"/></svg>`,
}

// Keep stats aligned with packages/core (25 providers, 18 tools) and product README.
const features = computed(() => {
  const pre = locPrefix.value
  const base = [
    { span: 'wide', icon: featureIcons.wide1, link: `${pre}/architecture/agent-runtime` },
    { span: 'tall', icon: featureIcons.tall1, link: `${pre}/guide/usage/topology-decision-tree` },
    { span: 'short', icon: featureIcons.short1, link: `${pre}/guide/providers` },
    { span: 'short', icon: featureIcons.short2, link: `${pre}/architecture/verification` },
    { span: 'tall', icon: featureIcons.tall2, link: `${pre}/architecture/intelligence` },
    { span: 'wide', icon: featureIcons.wide2, link: `${pre}/architecture/production-readiness` },
  ]
  const copy = {
    en: [
      ['Live SSE streaming', 'Every agent thought, tool call, and decision streams in real time via SSE.'],
      ['Automatic topology selection', 'Classifies CODING / RESEARCH / ANALYSIS / FACTUAL and picks SINGLE · CHAIN · DISPATCH · ORCHESTRATOR · REVIEW.'],
      ['25 providers with auto-failover', 'One API key. Auto-detect + failover across cloud and local models.'],
      ['Quality gates on every output', 'Five-layer verification: hallucination, consistency, completeness, accuracy, safety.'],
      ['Self-optimizing runtime', 'Thompson Sampling + Reflexion meta-learner. Activates after 5+ experiences.'],
      ['Production infrastructure', 'Circuit breakers, DLQ, WAL checkpoints, semantic cache, saga, supervision tree.'],
    ],
    zh: [
      ['实时 SSE 流式输出', '每个代理的思考、工具调用与决策经 SSE 实时进入终端。'],
      ['自动拓扑选择', '分类 CODING / RESEARCH / ANALYSIS / FACTUAL，选择 5 种规范拓扑。'],
      ['25 家提供商自动故障转移', '任意一把 Key。自动识别与故障转移。'],
      ['每次输出都有质量门', '五层校验：幻觉、一致性、完整性、准确性、安全。'],
      ['自优化运行时', 'Thompson Sampling + Reflexion。5+ 经验后生效。'],
      ['生产级基础设施', '熔断、DLQ、WAL、语义缓存、Saga、监督树。'],
    ],
    ja: [
      ['ライブ SSE ストリーム', '思考・ツール・決定を SSE でリアルタイム表示。'],
      ['自動トポロジ選択', 'CODING / RESEARCH / ANALYSIS / FACTUAL を分類し 5 トポロジから選択。'],
      ['25 プロバイダー + フェイルオーバー', 'キー 1 つ。自動検出とフェイルオーバー。'],
      ['出力ごとの品質ゲート', '幻覚・一貫性・完全性・正確性・安全の 5 層。'],
      ['自己最適化ランタイム', 'Thompson Sampling + Reflexion。5+ 経験後に有効。'],
      ['本番インフラ', 'ブレーカー、DLQ、WAL、セマンティックキャッシュ、Saga。'],
    ],
    ko: [
      ['라이브 SSE 스트림', '사고·도구·결정을 SSE로 실시간 표시.'],
      ['자동 토폴로지 선택', 'CODING / RESEARCH / ANALYSIS / FACTUAL 분류 후 5종 선택.'],
      ['25 프로바이더 + 페일오버', '키 하나. 자동 감지와 페일오버.'],
      ['출력마다 품질 게이트', '환각·일관성·완전성·정확성·안전 5계층.'],
      ['자가 최적화 런타임', 'Thompson Sampling + Reflexion. 5+ 경험 후 활성.'],
      ['프로덕션 인프라', '서킷 브레이커, DLQ, WAL, 시맨틱 캐시, Saga.'],
    ],
    es: [
      ['Streaming SSE en vivo', 'Pensamientos, tools y decisiones en tiempo real por SSE.'],
      ['Topología automática', 'Clasifica CODING / RESEARCH / ANALYSIS / FACTUAL y elige entre 5 topologías.'],
      ['25 proveedores + failover', 'Una API key. Auto-detección y bascula entre cloud y local.'],
      ['Puertas de calidad', 'Cinco capas: alucinación, consistencia, completitud, exactitud, seguridad.'],
      ['Runtime auto-optimizado', 'Thompson Sampling + Reflexion. Activo tras 5+ experiencias.'],
      ['Infra de producción', 'Circuit breakers, DLQ, WAL, caché semántica, saga.'],
    ],
    fr: [
      ['Streaming SSE live', 'Pensées, tools et décisions en temps réel via SSE.'],
      ['Topologie automatique', 'Classe CODING / RESEARCH / ANALYSIS / FACTUAL et choisit parmi 5 topologies.'],
      ['25 fournisseurs + failover', 'Une clé API. Auto-détection et bascule cloud / local.'],
      ['Portes de qualité', 'Cinq couches : hallucination, cohérence, complétude, exactitude, sécurité.'],
      ['Runtime auto-optimisé', 'Thompson Sampling + Reflexion. Actif après 5+ expériences.'],
      ['Infra de production', 'Circuit breakers, DLQ, WAL, cache sémantique, saga.'],
    ],
  }[locale.value]

  return base.map((b, i) => ({
    ...b,
    title: copy[i][0],
    desc: copy[i][1],
  }))
})

const stats = computed(() => {
  const labels = {
    en: ['LLM providers', 'Canonical topologies', 'Built-in tools', 'Tests'],
    zh: ['LLM 提供商', '规范拓扑', '内置工具', '测试'],
    ja: ['LLM プロバイダー', '正規トポロジ', '組み込みツール', 'テスト'],
    ko: ['LLM 프로바이더', '정규 토폴로지', '내장 도구', '테스트'],
    es: ['Proveedores LLM', 'Topologías canónicas', 'Tools integradas', 'Tests'],
    fr: ['Fournisseurs LLM', 'Topologies canoniques', 'Tools intégrés', 'Tests'],
  }[locale.value]
  return [
    { value: '25', label: labels[0] },
    { value: '5', label: labels[1] },
    { value: '18', label: labels[2] },
    { value: '6700+', label: labels[3] },
  ]
})

const whyCards = computed(() => {
  const packs: Record<string, { title: string; desc: string }[]> = {
    en: [
      {
        title: 'You are the engineer, not a passenger',
        desc: 'Other frameworks hide agent graphs behind YAML and hope. Commander streams every thought, tool call, and quality gate so you can debug and trust the run.',
      },
      {
        title: 'No graph builders. No YAML.',
        desc: 'Describe the task in plain language. Deliberation classifies it, picks a topology, and scales agents 1–20. Simple tasks stay simple.',
      },
      {
        title: 'Production primitives, not demos',
        desc: 'Circuit breakers, DLQ, saga compensation, SQLite WAL checkpoints, semantic cache, multi-tenancy — the same discipline as a distributed system.',
      },
      {
        title: 'One key, twenty-five providers',
        desc: 'Set any API key. Auto-detect + failover across cloud and local models (Ollama, vLLM). Swap providers without rewriting your workflow.',
      },
    ],
    zh: [
      {
        title: '你是工程师，不是乘客',
        desc: '其它框架把代理图藏在 YAML 后面。Commander 流式输出思考、工具与质量门，让你能调试并信任结果。',
      },
      {
        title: '不画图。不写 YAML。',
        desc: '自然语言描述任务。审议引擎分类、选拓扑，代理 1–20 按需扩展。简单任务保持简单。',
      },
      {
        title: '生产原语，不是演示玩具',
        desc: '熔断、DLQ、Saga 补偿、WAL 检查点、语义缓存、多租户 — 与分布式系统同一套纪律。',
      },
      {
        title: '一把 Key，二十五家提供商',
        desc: '任意 Key 即可。云端与本地（Ollama、vLLM）自动发现与故障转移，换提供商不必重写流程。',
      },
    ],
    ja: [
      {
        title: 'あなたは乗客ではなくエンジニア',
        desc: '他フレームワークは YAML の裏にグラフを隠します。Commander は思考・ツール・品質ゲートをストリームし、信頼できる実行を可能にします。',
      },
      {
        title: 'グラフビルダーなし。YAML なし。',
        desc: '自然言語でタスクを記述。審議が分類しトポロジを選び、エージェント 1–20 をスケール。',
      },
      {
        title: '本番プリミティブ',
        desc: 'サーキットブレーカー、DLQ、Saga、WAL、セマンティックキャッシュ、マルチテナント。',
      },
      {
        title: 'キー 1 つ、25 プロバイダー',
        desc: '任意の API キー。クラウドとローカル (Ollama / vLLM) の自動検出とフェイルオーバー。',
      },
    ],
    ko: [
      {
        title: '승객이 아니라 엔지니어',
        desc: '다른 프레임워크는 YAML 뒤에 그래프를 숨깁니다. Commander는 사고·도구·품질 게이트를 스트림합니다.',
      },
      {
        title: '그래프 빌더 없음. YAML 없음.',
        desc: '자연어로 작업 설명. 심의가 분류하고 토폴로지를 고르며 에이전트 1–20을 확장합니다.',
      },
      {
        title: '프로덕션 프리미티브',
        desc: '서킷 브레이커, DLQ, Saga, WAL, 시맨틱 캐시, 멀티 테넌시.',
      },
      {
        title: '키 하나, 25 프로바이더',
        desc: '아무 API 키나. 클라우드와 로컬(Ollama/vLLM) 자동 감지와 페일오버.',
      },
    ],
    es: [
      {
        title: 'Eres ingeniero, no pasajero',
        desc: 'Otros frameworks esconden grafos detrás de YAML. Commander transmite pensamientos, tools y puertas de calidad para que puedas depurar y confiar.',
      },
      {
        title: 'Sin constructores de grafos. Sin YAML.',
        desc: 'Describe la tarea en lenguaje natural. La deliberación clasifica, elige topología y escala agentes 1–20.',
      },
      {
        title: 'Primitivas de producción',
        desc: 'Circuit breakers, DLQ, saga, WAL, caché semántica, multi-tenant — la misma disciplina que un sistema distribuido.',
      },
      {
        title: 'Una key, veinticinco proveedores',
        desc: 'Cualquier API key. Auto-detección y failover entre cloud y local (Ollama, vLLM).',
      },
    ],
    fr: [
      {
        title: 'Vous êtes ingénieur, pas passager',
        desc: 'D’autres frameworks cachent les graphes derrière du YAML. Commander streame pensées, tools et portes de qualité pour déboguer et faire confiance.',
      },
      {
        title: 'Pas de constructeur de graphes. Pas de YAML.',
        desc: 'Décrivez la tâche en langage naturel. La délibération classe, choisit la topologie et scale les agents 1–20.',
      },
      {
        title: 'Primitives de production',
        desc: 'Circuit breakers, DLQ, saga, WAL, cache sémantique, multi-tenant — la même discipline qu’un système distribué.',
      },
      {
        title: 'Une clé, vingt-cinq fournisseurs',
        desc: 'N’importe quelle clé API. Auto-détection et bascule cloud / local (Ollama, vLLM).',
      },
    ],
  }
  return packs[locale.value]
})

const quickLinks = computed(() => {
  const pre = locPrefix.value
  const labels = {
    en: ['Get started', 'Why Commander', 'Cookbook'],
    zh: ['快速开始', '为什么选它', '实战手册'],
    ja: ['クイックスタート', 'なぜ Commander', 'クックブック'],
    ko: ['빠른 시작', '왜 Commander', '쿡북'],
    es: ['Empezar', 'Por qué Commander', 'Cookbook'],
    fr: ['Démarrer', 'Pourquoi Commander', 'Cookbook'],
  }[locale.value]
  return [
    { text: labels[0], to: `${pre}/guide/getting-started`, theme: 'brand' },
    { text: labels[1], to: `${pre}/guide/why-commander`, theme: 'alt' },
    { text: labels[2], to: `${pre}/guide/cookbook/`, theme: 'alt' },
    { text: 'GitHub', to: 'https://github.com/PStarH/Commander', theme: 'ghost', external: true },
  ]
})

const demoLines = [
  { cls: 'cmd-demo-muted', text: '$ commander run "audit this repo" --stream' },
  { cls: 'cmd-demo-dim', text: '┌─ Deliberation ─────────────────────────────' },
  { cls: '', text: '│ Classification: ANALYSIS · Complexity: 7/10' },
  { cls: '', text: '│ Topology: DISPATCH (3 agents)' },
  { cls: 'cmd-demo-dim', text: '├─ Agent α (security-scanner) ───────────────' },
  { cls: 'cmd-demo-ok', text: '│ [tool] npm audit · 2 critical, 5 moderate' },
  { cls: 'cmd-demo-ok', text: '│ [gate] ACCURACY ✓ · COMPLETENESS ✓' },
  { cls: 'cmd-demo-dim', text: '├─ Synthesizer ──────────────────────────────' },
  { cls: 'cmd-demo-accent', text: '│ Leader synthesis · 4 findings, 2 critical' },
  { cls: 'cmd-demo-dim', text: '└────────────────────────────────────────────' },
]

const t = computed(() => {
  const pre = locPrefix.value
  const pack = {
    en: {
      badge: 'v0.2 · Pre-production',
      h1a: 'Multi-agent orchestration,',
      h1b: 'built for production.',
      sub: 'Set one API key. Commander classifies the task, picks the right topology, and streams every agent decision to your terminal. No black boxes. 6700+ tests, no graph builders, no YAML.',
      demoTitle: 'See every decision',
      demoDesc:
        'Deliberation, topology, tools, and quality gates stream live — not after the fact. Copy, set a key, and watch agents work.',
      checklist: '5-minute checklist',
      cookbook: 'Cookbook recipes',
      featuresTitle: 'What Commander does',
      featuresSub: 'Six core capabilities, each backed by production-grade infrastructure and audited in CI.',
      whyTitle: 'Why Commander',
      whySub: 'Built for engineers who want to see what their AI is actually doing.',
      pathsTitle: 'Start where you are',
      pathsSub: 'Three paths into the same engine.',
      path1k: '01 · CLI',
      path1t: 'Run from the terminal',
      path1d: 'Clone, set one key, stream a multi-agent run in under two minutes.',
      path1a: 'Quick start →',
      path2k: '02 · Console',
      path2t: 'Open the Web Console',
      path2d: 'chat, topology, DLQ, governance.',
      path2a: 'Web Console →',
      path3k: '03 · SDK',
      path3t: 'Embed in TypeScript',
      path3d: 'events, memory, and plan mode.',
      path3a: 'Agent SDK →',
      ctaTitle: 'Ready to orchestrate?',
      ctaSub: 'One command, 25 providers, every decision visible. Set an API key and go.',
      ctaStart: 'Get started',
      ctaInstall: 'Install',
      ctaStar: 'Star on GitHub',
      more: 'Read more →',
    },
    zh: {
      badge: 'v0.2 · 预生产',
      h1a: '多代理编排，',
      h1b: '为生产而生。',
      sub: '一把 API Key。Commander 分类任务、选择拓扑，并把每个代理决策流式打到终端。无黑盒。6700+ 测试，不画图，不写 YAML。',
      demoTitle: '看清每一步决策',
      demoDesc: '审议、拓扑、工具与质量门实时流出 — 不是事后日志。复制命令、设置 Key，看着代理工作。',
      checklist: '五分钟清单',
      cookbook: '实战配方',
      featuresTitle: 'Commander 能做什么',
      featuresSub: '六大核心能力，均有生产级基础设施与 CI 审计支撑。',
      whyTitle: '为什么选 Commander',
      whySub: '为想看清 AI 在做什么的工程师而建。',
      pathsTitle: '从这里开始',
      pathsSub: '同一引擎的三条入口。',
      path1k: '01 · CLI',
      path1t: '终端直接跑',
      path1d: '克隆、设 Key，两分钟内流式多代理运行。',
      path1a: '快速开始 →',
      path2k: '02 · 控制台',
      path2t: '打开 Web 控制台',
      path2d: '对话、拓扑、DLQ、治理。',
      path2a: 'Web 控制台 →',
      path3k: '03 · SDK',
      path3t: '嵌入 TypeScript',
      path3d: '事件、记忆与 plan 模式。',
      path3a: 'Agent SDK →',
      ctaTitle: '准备好编排了吗？',
      ctaSub: '一条命令，25 家提供商，决策全程可见。设好 Key 开干。',
      ctaStart: '快速开始',
      ctaInstall: '安装',
      ctaStar: '在 GitHub 上 Star',
      more: '了解更多 →',
    },
    ja: {
      badge: 'v0.2 · プレ本番',
      h1a: 'マルチエージェント編成、',
      h1b: '本番のために。',
      sub: 'API キーは 1 つ。Commander がタスクを分類しトポロジを選び、すべての決定をターミナルにストリーム。ブラックボックスなし。6700+ テスト。',
      demoTitle: 'すべての決定を見る',
      demoDesc: '審議・トポロジ・ツール・品質ゲートがライブで流れます。キーを設定してエージェントを観察。',
      checklist: '5 分チェックリスト',
      cookbook: 'クックブック',
      featuresTitle: 'Commander ができること',
      featuresSub: '6 つのコア能力。本番インフラと CI で監査。',
      whyTitle: 'なぜ Commander か',
      whySub: 'AI の挙動を見たいエンジニアのために。',
      pathsTitle: 'ここから始める',
      pathsSub: '同じエンジンへの 3 つの入口。',
      path1k: '01 · CLI',
      path1t: 'ターミナルから実行',
      path1d: 'クローン、キー設定、2 分以内にストリーム。',
      path1a: 'クイックスタート →',
      path2k: '02 · コンソール',
      path2t: 'Web コンソールを開く',
      path2d: 'チャット、トポロジ、DLQ、ガバナンス。',
      path2a: 'Web コンソール →',
      path3k: '03 · SDK',
      path3t: 'TypeScript に埋め込む',
      path3d: 'イベント、メモリ、plan モード。',
      path3a: 'Agent SDK →',
      ctaTitle: '編成の準備はできた？',
      ctaSub: '1 コマンド、25 プロバイダー、すべて可視化。',
      ctaStart: 'はじめる',
      ctaInstall: 'インストール',
      ctaStar: 'GitHub で Star',
      more: '続きを読む →',
    },
    ko: {
      badge: 'v0.2 · 프리프로덕션',
      h1a: '멀티 에이전트 오케스트레이션,',
      h1b: '프로덕션을 위해.',
      sub: 'API 키 하나. Commander가 작업을 분류하고 토폴로지를 고르며 모든 결정을 터미널로 스트림. 블랙박스 없음. 6700+ 테스트.',
      demoTitle: '모든 결정을 보세요',
      demoDesc: '심의·토폴로지·도구·품질 게이트가 실시간으로 흐릅니다. 키를 설정하고 에이전트를 관찰하세요.',
      checklist: '5분 체크리스트',
      cookbook: '쿡북 레시피',
      featuresTitle: 'Commander가 하는 일',
      featuresSub: '6가지 핵심 역량. 프로덕션 인프라와 CI 감사.',
      whyTitle: '왜 Commander인가',
      whySub: 'AI가 무엇을 하는지 보고 싶은 엔지니어를 위해.',
      pathsTitle: '여기서 시작',
      pathsSub: '같은 엔진으로 가는 세 갈래.',
      path1k: '01 · CLI',
      path1t: '터미널에서 실행',
      path1d: '클론, 키 설정, 2분 내 스트림.',
      path1a: '빠른 시작 →',
      path2k: '02 · 콘솔',
      path2t: '웹 콘솔 열기',
      path2d: '채팅, 토폴로지, DLQ, 거버넌스.',
      path2a: '웹 콘솔 →',
      path3k: '03 · SDK',
      path3t: 'TypeScript에 임베드',
      path3d: '이벤트, 메모리, plan 모드.',
      path3a: 'Agent SDK →',
      ctaTitle: '오케스트레이션 준비됐나요?',
      ctaSub: '명령 하나, 25 프로바이더, 모든 결정이 보입니다.',
      ctaStart: '시작하기',
      ctaInstall: '설치',
      ctaStar: 'GitHub에서 Star',
      more: '더 보기 →',
    },
    es: {
      badge: 'v0.2 · Pre-producción',
      h1a: 'Orquestación multi-agente,',
      h1b: 'hecha para producción.',
      sub: 'Una API key. Commander clasifica la tarea, elige la topología y transmite cada decisión al terminal. Sin cajas negras. 6700+ tests, sin grafos ni YAML.',
      demoTitle: 'Mira cada decisión',
      demoDesc:
        'Deliberación, topología, tools y puertas de calidad en vivo. Copia, configura una key y observa a los agentes.',
      checklist: 'Lista de 5 minutos',
      cookbook: 'Recetas del cookbook',
      featuresTitle: 'Qué hace Commander',
      featuresSub: 'Seis capacidades núcleo con infraestructura de producción y CI.',
      whyTitle: 'Por qué Commander',
      whySub: 'Para ingenieros que quieren ver qué hace su IA de verdad.',
      pathsTitle: 'Empieza donde estés',
      pathsSub: 'Tres caminos al mismo motor.',
      path1k: '01 · CLI',
      path1t: 'Desde el terminal',
      path1d: 'Clona, configura una key, stream en menos de dos minutos.',
      path1a: 'Inicio rápido →',
      path2k: '02 · Consola',
      path2t: 'Abre la consola web',
      path2d: 'chat, topología, DLQ, gobernanza.',
      path2a: 'Consola web →',
      path3k: '03 · SDK',
      path3t: 'Integra en TypeScript',
      path3d: 'eventos, memoria y modo plan.',
      path3a: 'Agent SDK →',
      ctaTitle: '¿Listo para orquestar?',
      ctaSub: 'Un comando, 25 proveedores, cada decisión visible.',
      ctaStart: 'Empezar',
      ctaInstall: 'Instalar',
      ctaStar: 'Star en GitHub',
      more: 'Leer más →',
    },
    fr: {
      badge: 'v0.2 · Pré-production',
      h1a: 'Orchestration multi-agents,',
      h1b: 'faite pour la production.',
      sub: 'Une clé API. Commander classe la tâche, choisit la topologie et streame chaque décision dans le terminal. Pas de boîte noire. 6700+ tests, sans graphes ni YAML.',
      demoTitle: 'Voyez chaque décision',
      demoDesc:
        'Délibération, topologie, tools et portes de qualité en live. Copiez, définissez une clé, observez les agents.',
      checklist: 'Checklist 5 minutes',
      cookbook: 'Recettes cookbook',
      featuresTitle: 'Ce que fait Commander',
      featuresSub: 'Six capacités cœur, infra de production et CI.',
      whyTitle: 'Pourquoi Commander',
      whySub: 'Pour les ingénieurs qui veulent voir ce que fait vraiment leur IA.',
      pathsTitle: 'Commencez où vous êtes',
      pathsSub: 'Trois chemins vers le même moteur.',
      path1k: '01 · CLI',
      path1t: 'Depuis le terminal',
      path1d: 'Clonez, définissez une clé, streamez en moins de deux minutes.',
      path1a: 'Démarrage rapide →',
      path2k: '02 · Console',
      path2t: 'Ouvrir la console web',
      path2d: 'chat, topologie, DLQ, gouvernance.',
      path2a: 'Console web →',
      path3k: '03 · SDK',
      path3t: 'Intégrer en TypeScript',
      path3d: 'événements, mémoire et mode plan.',
      path3a: 'Agent SDK →',
      ctaTitle: 'Prêt à orchestrer ?',
      ctaSub: 'Une commande, 25 fournisseurs, chaque décision visible.',
      ctaStart: 'Démarrer',
      ctaInstall: 'Installer',
      ctaStar: 'Star sur GitHub',
      more: 'Lire la suite →',
    },
  }[locale.value]

  return {
    ...pack,
    path1to: `${pre}/guide/getting-started`,
    path2to: `${pre}/guide/web-console`,
    path3to: `${pre}/guide/sdk`,
    startTo: `${pre}/guide/getting-started`,
    installTo: `${pre}/guide/installation`,
    cookbookTo: `${pre}/guide/cookbook/`,
  }
})

/** Prefix site base for internal paths (required on GitHub Pages /commander-docs/). */
function hrefFor(to: string, external?: boolean) {
  if (external || /^https?:\/\//.test(to)) return to
  return withBase(to)
}

let ctx: gsap.Context | null = null

function prefersReducedMotion(): boolean {
  if (typeof window === 'undefined') return true
  return window.matchMedia('(prefers-reduced-motion: reduce)').matches
}

function playAnimations() {
  if (ctx) {
    ctx.revert()
    ctx = null
  }
  ScrollTrigger.getAll().forEach((t) => t.kill())

  if (prefersReducedMotion()) return

  const hero = document.querySelector('.cmd-hero')
  if (!hero) return

  ctx = gsap.context(() => {
    const tl = gsap.timeline({ defaults: { ease: 'power3.out', duration: 0.6 } })
    tl.from('.cmd-hero .cmd-badge', { y: 12, opacity: 0 })
      .from('.cmd-hero h1', { y: 24, opacity: 0, duration: 0.8 }, '-=0.4')
      .from('.cmd-hero .cmd-sub', { y: 18, opacity: 0 }, '-=0.5')
      .from('.cmd-hero .cmd-actions .cmd-btn', { y: 12, opacity: 0, duration: 0.4, stagger: 0.08 }, '-=0.45')
      .from('.cmd-hero .cmd-mockup', { y: 32, opacity: 0, duration: 0.9, ease: 'power2.out' }, '-=0.55')
      .from('.cmd-hero .cmd-stat', { y: 12, opacity: 0, duration: 0.4, stagger: 0.08 }, '-=0.5')

    gsap.from('.cmd-demo-strip', {
      y: 16,
      opacity: 0,
      duration: 0.5,
      scrollTrigger: { trigger: '.cmd-demo-strip', start: 'top 90%', once: true },
    })

    gsap.from('.cmd-features .cmd-feature', {
      y: 28,
      opacity: 0,
      duration: 0.55,
      stagger: 0.06,
      ease: 'power2.out',
      scrollTrigger: { trigger: '.cmd-features', start: 'top 80%', once: true },
    })

    gsap.from('.cmd-why .cmd-why-card', {
      y: 24,
      opacity: 0,
      duration: 0.5,
      stagger: 0.08,
      ease: 'power2.out',
      scrollTrigger: { trigger: '.cmd-why', start: 'top 80%', once: true },
    })

    gsap.from('.cmd-cta', {
      y: 20,
      opacity: 0,
      duration: 0.6,
      scrollTrigger: { trigger: '.cmd-cta', start: 'top 85%', once: true },
    })
  })
}

onMounted(() => {
  gsap.registerPlugin(ScrollTrigger)
  requestAnimationFrame(() => requestAnimationFrame(playAnimations))
})

onBeforeUnmount(() => {
  if (ctx) {
    ctx.revert()
    ctx = null
  }
  ScrollTrigger.getAll().forEach((t) => t.kill())
})
</script>

<template>
  <div class="cmd-home">
    <!-- HERO -->
    <section class="cmd-hero">
      <div class="cmd-hero-inner">
        <div class="cmd-hero-text">
          <span class="cmd-badge">
            <span class="cmd-badge-dot" /> {{ t.badge }}
          </span>
          <h1>
            {{ t.h1a }}<br />
            <span class="cmd-accent">{{ t.h1b }}</span>
          </h1>
          <p class="cmd-sub">
            {{ t.sub }}
          </p>
          <div class="cmd-actions">
            <a
              v-for="(btn, i) in quickLinks"
              :key="i"
              :href="hrefFor(btn.to, btn.external)"
              :class="['cmd-btn', `cmd-btn--${btn.theme}`]"
              :target="btn.external ? '_blank' : undefined"
              :rel="btn.external ? 'noopener' : undefined"
            >
              {{ btn.text }}
              <span v-if="btn.external" class="cmd-ext">↗</span>
            </a>
          </div>
        </div>

        <div class="cmd-hero-mockup-wrap">
          <div class="cmd-mockup-shadow" />
          <div class="cmd-mockup">
            <img :src="withBase('/terminal-mockup.svg')" alt="Commander terminal streaming multi-agent execution" />
          </div>
        </div>
      </div>

      <!-- Stats strip — visual rhythm -->
      <div class="cmd-stats">
        <div v-for="s in stats" :key="s.label" class="cmd-stat">
          <div class="cmd-stat-value">{{ s.value }}</div>
          <div class="cmd-stat-label">{{ s.label }}</div>
        </div>
      </div>
    </section>

    <!-- DEMO — copy-paste success path + stream preview -->
    <section class="cmd-demo-strip" aria-label="Live stream demo">
      <div class="cmd-demo-grid">
        <div class="cmd-demo-copy">
          <h2>{{ t.demoTitle }}</h2>
          <p>{{ t.demoDesc }}</p>
          <pre class="cmd-demo-code" tabindex="0"><code>git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream</code></pre>
          <div class="cmd-actions">
            <a :href="hrefFor(t.startTo)" class="cmd-btn cmd-btn--brand">{{ t.checklist }}</a>
            <a :href="hrefFor(t.cookbookTo)" class="cmd-btn cmd-btn--alt">{{ t.cookbook }}</a>
          </div>
        </div>
        <div class="cmd-demo-terminal" role="img" aria-label="Example Commander stream output">
          <div class="cmd-demo-chrome">
            <span class="cmd-demo-dot cmd-demo-dot--r" />
            <span class="cmd-demo-dot cmd-demo-dot--y" />
            <span class="cmd-demo-dot cmd-demo-dot--g" />
            <span class="cmd-demo-chrome-title">commander · stream</span>
          </div>
          <div class="cmd-demo-body">
            <div
              v-for="(line, i) in demoLines"
              :key="i"
              :class="['cmd-demo-line', line.cls]"
            >{{ line.text }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- FEATURES — non-symmetric bento grid -->
    <section class="cmd-features">
      <div class="cmd-section-head">
        <h2>{{ t.featuresTitle }}</h2>
        <p>{{ t.featuresSub }}</p>
      </div>
      <div class="cmd-bento">
        <a
          v-for="(f, i) in features"
          :key="i"
          :href="hrefFor(f.link)"
          :class="['cmd-feature', `cmd-feature--${f.span}`]"
        >
          <div class="cmd-feature-icon" v-html="f.icon" />
          <h3 class="cmd-feature-title">{{ f.title }}</h3>
          <p class="cmd-feature-desc">{{ f.desc }}</p>
          <span class="cmd-feature-arrow">{{ t.more }}</span>
        </a>
      </div>
    </section>

    <!-- WHY -->
    <section class="cmd-why">
      <div class="cmd-section-head">
        <h2>{{ t.whyTitle }}</h2>
        <p>{{ t.whySub }}</p>
      </div>
      <div class="cmd-why-grid">
        <div v-for="(w, i) in whyCards" :key="i" class="cmd-why-card">
          <h3>{{ w.title }}</h3>
          <p>{{ w.desc }}</p>
        </div>
      </div>
    </section>

    <!-- PATHS -->
    <section class="cmd-paths">
      <div class="cmd-section-head">
        <h2>{{ t.pathsTitle }}</h2>
        <p>{{ t.pathsSub }}</p>
      </div>
      <div class="cmd-paths-grid">
        <a :href="hrefFor(t.path1to)" class="cmd-path-card">
          <span class="cmd-path-kicker">{{ t.path1k }}</span>
          <h3>{{ t.path1t }}</h3>
          <p>{{ t.path1d }}</p>
          <span class="cmd-feature-arrow">{{ t.path1a }}</span>
        </a>
        <a :href="hrefFor(t.path2to)" class="cmd-path-card">
          <span class="cmd-path-kicker">{{ t.path2k }}</span>
          <h3>{{ t.path2t }}</h3>
          <p><code>pnpm gui</code> — {{ t.path2d }}</p>
          <span class="cmd-feature-arrow">{{ t.path2a }}</span>
        </a>
        <a :href="hrefFor(t.path3to)" class="cmd-path-card">
          <span class="cmd-path-kicker">{{ t.path3k }}</span>
          <h3>{{ t.path3t }}</h3>
          <p><code>CommanderClient.run()</code> — {{ t.path3d }}</p>
          <span class="cmd-feature-arrow">{{ t.path3a }}</span>
        </a>
      </div>
    </section>

    <!-- CTA -->
    <section class="cmd-cta">
      <h2>{{ t.ctaTitle }}</h2>
      <p>{{ t.ctaSub }}</p>
      <div class="cmd-actions">
        <a :href="hrefFor(t.startTo)" class="cmd-btn cmd-btn--brand">{{ t.ctaStart }}</a>
        <a :href="hrefFor(t.installTo)" class="cmd-btn cmd-btn--alt">{{ t.ctaInstall }}</a>
        <a href="https://github.com/PStarH/Commander" class="cmd-btn cmd-btn--ghost" target="_blank" rel="noopener">
          {{ t.ctaStar }} <span class="cmd-ext">↗</span>
        </a>
      </div>
    </section>
  </div>
</template>

<style scoped>
.cmd-home {
  max-width: 1120px;
  margin: 0 auto;
  padding: 0 24px;
}

/* HERO */
.cmd-hero { padding: 64px 0 56px; }

.cmd-hero-inner {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 56px;
  align-items: center;
}

.cmd-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 4px 12px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--vp-c-text-2);
  letter-spacing: -0.005em;
  margin-bottom: 20px;
}

.cmd-badge-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #22c55e;
  box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.15);
}

.cmd-hero-text h1 {
  font-size: 3.1rem;
  line-height: 1.05;
  font-weight: 700;
  letter-spacing: -0.035em;
  color: var(--vp-c-text-1);
  margin: 0 0 18px;
}

.cmd-accent {
  background: linear-gradient(180deg, var(--vp-c-text-1) 0%, var(--vp-c-text-2) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.cmd-sub {
  font-size: 1.05rem;
  line-height: 1.6;
  color: var(--vp-c-text-2);
  margin: 0 0 28px;
  max-width: 520px;
}

.cmd-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.cmd-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 10px 18px;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 500;
  letter-spacing: -0.005em;
  text-decoration: none;
  transition: all 0.18s ease;
  border: 1px solid transparent;
  cursor: pointer;
}

.cmd-btn--brand {
  background: var(--vp-c-text-1);
  color: var(--vp-c-bg);
  border-color: var(--vp-c-text-1);
}
.cmd-btn--brand:hover {
  background: var(--vp-c-text-2);
  border-color: var(--vp-c-text-2);
  transform: translateY(-1px);
}

.cmd-btn--alt {
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  border-color: var(--vp-c-border);
}
.cmd-btn--alt:hover {
  background: var(--vp-c-bg-soft);
  border-color: var(--vp-c-text-3);
}

.cmd-btn--ghost {
  background: transparent;
  color: var(--vp-c-text-2);
  border-color: transparent;
}
.cmd-btn--ghost:hover {
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg-soft);
}

.cmd-ext { font-size: 0.8em; opacity: 0.7; }

.cmd-hero-mockup-wrap {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 0;
}

.cmd-mockup-shadow {
  position: absolute;
  inset: 8% 6% -6% 6%;
  background: var(--vp-c-text-1);
  opacity: 0.04;
  filter: blur(40px);
  border-radius: 12px;
  z-index: 0;
}

.cmd-mockup {
  position: relative;
  z-index: 1;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid var(--vp-c-border);
  background: #09090b;
  width: 100%;
  max-width: 560px;
}

.cmd-mockup img {
  display: block;
  width: 100%;
  height: auto;
}

/* Stats */
.cmd-stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  background: var(--vp-c-border);
  border: 1px solid var(--vp-c-border);
  border-radius: 10px;
  margin-top: 56px;
  overflow: hidden;
}

.cmd-stat {
  background: var(--vp-c-bg);
  padding: 20px 24px;
  text-align: left;
}

.cmd-stat-value {
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: -0.025em;
  color: var(--vp-c-text-1);
  font-variant-numeric: tabular-nums;
  line-height: 1;
}

.cmd-stat-label {
  font-size: 0.8rem;
  color: var(--vp-c-text-3);
  margin-top: 4px;
  letter-spacing: -0.005em;
}

/* FEATURES — bento, 非对称 */
.cmd-features { padding: 80px 0 56px; }

.cmd-section-head {
  margin-bottom: 40px;
  max-width: 640px;
}

.cmd-section-head h2 {
  font-size: 1.875rem;
  font-weight: 700;
  letter-spacing: -0.025em;
  color: var(--vp-c-text-1);
  margin: 0 0 8px;
  line-height: 1.2;
}

.cmd-section-head p {
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--vp-c-text-2);
  margin: 0;
}

.cmd-bento {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-auto-rows: minmax(180px, auto);
  gap: 1px;
  background: var(--vp-c-border);
  border: 1px solid var(--vp-c-border);
  border-radius: 12px;
  overflow: hidden;
}

.cmd-feature--wide  { grid-column: span 4; grid-row: span 2; }
.cmd-feature--tall  { grid-column: span 2; grid-row: span 2; }
.cmd-feature--short { grid-column: span 3; grid-row: span 1; }

.cmd-feature {
  background: var(--vp-c-bg);
  padding: 28px;
  text-decoration: none;
  display: flex;
  flex-direction: column;
  position: relative;
  transition: background 0.18s ease;
  min-width: 0;
}

.cmd-feature:hover { background: var(--vp-c-bg-soft); }

.cmd-feature--tall {
  background: var(--vp-c-bg-soft);
}
.cmd-feature--tall:hover { background: var(--vp-c-bg); }

.cmd-feature-icon {
  width: 36px;
  height: 36px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-border);
  color: var(--vp-c-text-1);
  margin-bottom: 16px;
  flex-shrink: 0;
}
.cmd-feature--tall .cmd-feature-icon { background: var(--vp-c-bg-soft); }

.cmd-feature-icon :deep(svg) {
  width: 20px;
  height: 20px;
}

.cmd-feature-title {
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: -0.015em;
  color: var(--vp-c-text-1);
  margin: 0 0 8px;
  line-height: 1.3;
}

.cmd-feature-desc {
  font-size: 0.875rem;
  line-height: 1.6;
  color: var(--vp-c-text-2);
  margin: 0;
  flex: 1;
}

.cmd-feature-arrow {
  display: inline-flex;
  align-items: center;
  font-size: 0.8rem;
  color: var(--vp-c-text-3);
  margin-top: 16px;
  transition: color 0.18s ease, transform 0.18s ease;
}

.cmd-feature:hover .cmd-feature-arrow {
  color: var(--vp-c-text-1);
  transform: translateX(2px);
}

/* DEMO STRIP */
.cmd-demo-strip {
  padding: 8px 0 40px;
}

.cmd-demo-grid {
  display: grid;
  grid-template-columns: 1fr 1.05fr;
  gap: 28px;
  align-items: stretch;
}

.cmd-demo-copy h2 {
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: -0.025em;
  color: var(--vp-c-text-1);
  margin: 0 0 10px;
}

.cmd-demo-copy > p {
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--vp-c-text-2);
  margin: 0 0 16px;
  max-width: 440px;
}

.cmd-demo-code {
  margin: 0 0 18px;
  padding: 14px 16px;
  border-radius: 10px;
  border: 1px solid var(--vp-c-border);
  background: #09090b;
  color: #e4e4e7;
  font-family: var(--vp-font-family-mono);
  font-size: 0.72rem;
  line-height: 1.55;
  overflow-x: auto;
  white-space: pre;
}

.cmd-demo-terminal {
  border-radius: 12px;
  border: 1px solid var(--vp-c-border);
  background: #09090b;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  min-height: 280px;
}

.cmd-demo-chrome {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 14px;
  border-bottom: 1px solid #27272a;
  background: #111113;
}

.cmd-demo-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.cmd-demo-dot--r { background: #ef4444; }
.cmd-demo-dot--y { background: #eab308; }
.cmd-demo-dot--g { background: #22c55e; }

.cmd-demo-chrome-title {
  margin-left: 8px;
  font-size: 0.7rem;
  color: #71717a;
  font-family: var(--vp-font-family-mono);
}

.cmd-demo-body {
  padding: 14px 16px 18px;
  font-family: var(--vp-font-family-mono);
  font-size: 0.72rem;
  line-height: 1.65;
  color: #d4d4d8;
  flex: 1;
}

.cmd-demo-line { white-space: pre-wrap; word-break: break-word; }
.cmd-demo-muted { color: #a1a1aa; }
.cmd-demo-dim { color: #52525b; }
.cmd-demo-ok { color: #4ade80; }
.cmd-demo-accent { color: #fafafa; font-weight: 500; }

/* WHY */
.cmd-why {
  padding: 24px 0 16px;
}

.cmd-why-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.cmd-why-card {
  padding: 24px;
  border: 1px solid var(--vp-c-border);
  border-radius: 12px;
  background: var(--vp-c-bg);
  transition: background 0.18s ease, border-color 0.18s ease;
}

.cmd-why-card:hover {
  background: var(--vp-c-bg-soft);
  border-color: var(--vp-c-text-3);
}

.cmd-why-card h3 {
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -0.015em;
  color: var(--vp-c-text-1);
  margin: 0 0 8px;
  line-height: 1.35;
}

.cmd-why-card p {
  font-size: 0.875rem;
  line-height: 1.6;
  color: var(--vp-c-text-2);
  margin: 0;
}

/* PATHS */
.cmd-paths {
  padding: 40px 0 8px;
}

.cmd-paths-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.cmd-path-card {
  display: flex;
  flex-direction: column;
  padding: 24px;
  border: 1px solid var(--vp-c-border);
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
  text-decoration: none;
  transition: background 0.18s ease, transform 0.18s ease, border-color 0.18s ease;
  min-width: 0;
}

.cmd-path-card:hover {
  background: var(--vp-c-bg);
  border-color: var(--vp-c-text-3);
  transform: translateY(-2px);
}

.cmd-path-kicker {
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--vp-c-text-3);
  margin-bottom: 12px;
}

.cmd-path-card h3 {
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: -0.015em;
  color: var(--vp-c-text-1);
  margin: 0 0 8px;
}

.cmd-path-card p {
  font-size: 0.875rem;
  line-height: 1.6;
  color: var(--vp-c-text-2);
  margin: 0;
  flex: 1;
}

.cmd-path-card code {
  font-size: 0.8em;
  padding: 1px 5px;
  border-radius: 4px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-border);
}

.cmd-path-card .cmd-feature-arrow {
  margin-top: 16px;
}

.cmd-path-card:hover .cmd-feature-arrow {
  color: var(--vp-c-text-1);
  transform: translateX(2px);
}

/* CTA */
.cmd-cta {
  padding: 64px 0 96px;
  text-align: center;
  border-top: 1px solid var(--vp-c-border);
  margin-top: 56px;
}

.cmd-cta h2 {
  font-size: 1.75rem;
  font-weight: 700;
  letter-spacing: -0.025em;
  color: var(--vp-c-text-1);
  margin: 0 0 8px;
}

.cmd-cta p {
  font-size: 0.95rem;
  color: var(--vp-c-text-2);
  margin: 0 0 24px;
}

.cmd-cta .cmd-actions { justify-content: center; }

/* RESPONSIVE */
@media (max-width: 960px) {
  .cmd-hero-inner {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  .cmd-hero-text h1 { font-size: 2.4rem; }
  .cmd-mockup { max-width: 100%; }
  .cmd-bento {
    grid-template-columns: repeat(2, 1fr);
    grid-auto-rows: minmax(160px, auto);
  }
  .cmd-feature--wide,
  .cmd-feature--tall,
  .cmd-feature--short {
    grid-column: span 1;
    grid-row: span 1;
  }
  .cmd-paths-grid { grid-template-columns: 1fr; }
  .cmd-demo-grid { grid-template-columns: 1fr; }
}

@media (max-width: 640px) {
  .cmd-home { padding: 0 16px; }
  .cmd-hero { padding: 40px 0 32px; }
  .cmd-hero-text h1 { font-size: 1.9rem; }
  .cmd-sub { font-size: 0.95rem; }
  .cmd-stats { grid-template-columns: repeat(2, 1fr); }
  .cmd-bento { grid-template-columns: 1fr; }
  .cmd-why-grid { grid-template-columns: 1fr; }
  .cmd-section-head h2 { font-size: 1.5rem; }
  .cmd-cta h2 { font-size: 1.4rem; }
  .cmd-demo-code { font-size: 0.65rem; }
}
</style>
