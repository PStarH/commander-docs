<script setup lang="ts">
import { onMounted, onBeforeUnmount } from 'vue'
import { withBase } from 'vitepress'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

// Keep stats aligned with packages/core (25 providers, 18 tools) and product README.
const features = [
  {
    title: 'Live SSE streaming',
    desc: 'Every agent thought, tool call, and decision streams to your terminal in real time via Server-Sent Events. Not polling. Not logs after the fact — you watch your agents reason, step by step.',
    link: '/architecture/agent-runtime',
    span: 'wide',
    icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h4l3-7 4 14 3-7h4"/></svg>`,
  },
  {
    title: 'Automatic topology selection',
    desc: 'The deliberation engine classifies each task (CODING / RESEARCH / ANALYSIS / FACTUAL) and picks from 5 canonical topologies — SINGLE, CHAIN, DISPATCH, ORCHESTRATOR, REVIEW.',
    link: '/guide/usage/topology-decision-tree',
    span: 'tall',
    icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l9 9-9 9-9-9z"/><circle cx="12" cy="12" r="2" fill="currentColor"/></svg>`,
  },
  {
    title: '25 providers with auto-failover',
    desc: 'Set any one API key. Commander detects your provider, and if it fails, falls through a configurable chain — OpenAI → Anthropic → DeepSeek → Groq → Ollama.',
    link: '/guide/providers',
    span: 'short',
    icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 0 1 14-5"/><path d="M20 12a8 8 0 0 1-14 5"/><path d="M18 4v4h-4M6 20v-4h4"/></svg>`,
  },
  {
    title: 'Quality gates on every output',
    desc: 'Five-layer verification: hallucination, consistency, completeness, accuracy, and safety. Failed gates trigger retry with full context — no silent wrong answers.',
    link: '/architecture/verification',
    span: 'short',
    icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5 9-11"/></svg>`,
  },
  {
    title: 'Self-optimizing runtime',
    desc: 'A meta-learner using Thompson Sampling and Reflexion tunes agent configurations across runs. Activates after 5+ recorded experiences.',
    link: '/architecture/intelligence',
    span: 'tall',
    icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 0 1 13-6"/><path d="M20 12a8 8 0 0 1-13 6"/><path d="M3 6h4v4M21 18h-4v-4"/></svg>`,
  },
  {
    title: 'Production infrastructure',
    desc: 'Circuit breakers, dead letter queue, SQLite WAL checkpoints, semantic caching, saga transactions, and a supervision tree. Built with the same discipline as any production distributed system.',
    link: '/architecture/production-readiness',
    span: 'wide',
    icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 4v5c0 5-4 8-8 9-4-1-8-4-8-9V7z"/></svg>`,
  },
]

const stats = [
  { value: '25', label: 'LLM providers' },
  { value: '5', label: 'Canonical topologies' },
  { value: '18', label: 'Built-in tools' },
  { value: '6700+', label: 'Tests' },
]

const whyCards = [
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
]

const quickLinks = [
  { text: 'Get started', to: '/guide/getting-started', theme: 'brand' },
  { text: 'Why Commander', to: '/guide/why-commander', theme: 'alt' },
  { text: 'Cookbook', to: '/guide/cookbook/', theme: 'alt' },
  { text: 'GitHub', to: 'https://github.com/PStarH/Commander', theme: 'ghost', external: true },
]

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

/** Prefix site base for internal paths (required on GitHub Pages /commander-docs/). */
function hrefFor(to: string, external?: boolean) {
  if (external || /^https?:\/\//.test(to)) return to
  return withBase(to)
}

let ctx: gsap.Context | null = null

function playAnimations() {
  if (ctx) {
    ctx.revert()
    ctx = null
  }
  ScrollTrigger.getAll().forEach(t => t.kill())

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
  ScrollTrigger.getAll().forEach(t => t.kill())
})
</script>

<template>
  <div class="cmd-home">
    <!-- HERO -->
    <section class="cmd-hero">
      <div class="cmd-hero-inner">
        <div class="cmd-hero-text">
          <span class="cmd-badge">
            <span class="cmd-badge-dot" /> v0.2 · Pre-production
          </span>
          <h1>
            Multi-agent orchestration,<br />
            <span class="cmd-accent">built for production.</span>
          </h1>
          <p class="cmd-sub">
            Set one API key. Commander classifies the task, picks the right topology, and streams every agent decision to your terminal. No black boxes. 6700+ tests, no graph builders, no YAML.
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
          <h2>See every decision</h2>
          <p>
            Deliberation, topology, tools, and quality gates stream live — not after the fact.
            Copy, set a key, and watch agents work.
          </p>
          <pre class="cmd-demo-code" tabindex="0"><code>git clone https://github.com/PStarH/Commander.git
cd Commander && pnpm install
export OPENAI_API_KEY=sk-...
npx tsx packages/core/src/cliEntry.ts run "audit this repo" --stream</code></pre>
          <div class="cmd-actions">
            <a :href="hrefFor('/guide/getting-started')" class="cmd-btn cmd-btn--brand">5-minute checklist</a>
            <a :href="hrefFor('/guide/cookbook/')" class="cmd-btn cmd-btn--alt">Cookbook recipes</a>
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
        <h2>What Commander does</h2>
        <p>Six core capabilities, each backed by production-grade infrastructure and audited in CI.</p>
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
          <span class="cmd-feature-arrow">Read more →</span>
        </a>
      </div>
    </section>

    <!-- WHY -->
    <section class="cmd-why">
      <div class="cmd-section-head">
        <h2>Why Commander</h2>
        <p>Built for engineers who want to see what their AI is actually doing.</p>
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
        <h2>Start where you are</h2>
        <p>Three paths into the same engine.</p>
      </div>
      <div class="cmd-paths-grid">
        <a :href="hrefFor('/guide/getting-started')" class="cmd-path-card">
          <span class="cmd-path-kicker">01 · CLI</span>
          <h3>Run from the terminal</h3>
          <p>Clone, set one key, stream a multi-agent run in under two minutes.</p>
          <span class="cmd-feature-arrow">Quick start →</span>
        </a>
        <a :href="hrefFor('/guide/web-console')" class="cmd-path-card">
          <span class="cmd-path-kicker">02 · Console</span>
          <h3>Open the Web Console</h3>
          <p><code>pnpm gui</code> — chat, topology, DLQ, governance.</p>
          <span class="cmd-feature-arrow">Web Console →</span>
        </a>
        <a :href="hrefFor('/guide/sdk')" class="cmd-path-card">
          <span class="cmd-path-kicker">03 · SDK</span>
          <h3>Embed in TypeScript</h3>
          <p><code>CommanderClient.run()</code> with events, memory, and plan mode.</p>
          <span class="cmd-feature-arrow">Agent SDK →</span>
        </a>
      </div>
    </section>

    <!-- CTA -->
    <section class="cmd-cta">
      <h2>Ready to orchestrate?</h2>
      <p>One command, 25 providers, every decision visible. Set an API key and go.</p>
      <div class="cmd-actions">
        <a :href="hrefFor('/guide/getting-started')" class="cmd-btn cmd-btn--brand">Get started</a>
        <a :href="hrefFor('/guide/installation')" class="cmd-btn cmd-btn--alt">Install</a>
        <a href="https://github.com/PStarH/Commander" class="cmd-btn cmd-btn--ghost" target="_blank" rel="noopener">
          Star on GitHub <span class="cmd-ext">↗</span>
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
