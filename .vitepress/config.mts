import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Commander',
  description:
    'Multi-agent orchestration engine — 25 providers · 5 canonical topologies · 18 built-in tools · 6700+ tests',
  lang: 'en-US',
  base: '/commander-docs/',

  cleanUrls: false,
  lastUpdated: true,
  ignoreDeadLinks: false,

  vite: {
    ssr: {
      noExternal: ['gsap', 'gsap/ScrollTrigger'],
    },
  },

  head: [
    // Paths under head are NOT auto-prefixed with base — include it explicitly
    ['link', { rel: 'icon', href: '/commander-docs/favicon.svg', type: 'image/svg+xml' }],
    ['meta', { name: 'theme-color', content: '#09090b' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'Commander — Multi-Agent Orchestration Engine' }],
    [
      'meta',
      {
        property: 'og:description',
        content:
          'Orchestrate multiple agents across any topology — single, chain, dispatch, orchestrator, review — backed by 25 LLM providers.',
      },
    ],
    ['meta', { property: 'og:site_name', content: 'Commander Docs' }],
  ],

  themeConfig: {
    // themeConfig.logo IS auto-prefixed with base — do NOT include /commander-docs/
    logo: '/logo.svg',

    siteTitle: 'Commander',

    nav: [
      { text: 'Guide', link: '/guide/getting-started', activeMatch: '/guide/' },
      { text: 'Architecture', link: '/architecture/overview', activeMatch: '/architecture/' },
      { text: 'API', link: '/api/overview', activeMatch: '/api/' },
      { text: 'Deployment', link: '/deployment', activeMatch: '/deployment' },
      { text: 'Community', link: '/community', activeMatch: '/community' },
    ],

    sidebar: {
      '/guide/': [
        {
          text: 'Getting Started',
          items: [
            { text: 'Quick Start', link: '/guide/getting-started' },
            { text: 'Installation', link: '/guide/installation' },
            { text: 'Commands', link: '/guide/commands' },
            { text: 'Providers', link: '/guide/providers' },
            { text: 'Configuration', link: '/guide/configuration' },
          ],
        },
        {
          text: 'Usage',
          items: [
            { text: 'Running Tasks', link: '/guide/usage/running-tasks' },
            { text: 'Plan Mode', link: '/guide/usage/plan-mode' },
            { text: 'Watch Mode', link: '/guide/usage/watch-mode' },
            { text: 'Topology Decision Tree', link: '/guide/usage/topology-decision-tree' },
            { text: 'Chaos Testing', link: '/guide/usage/chaos-testing' },
            { text: 'Shadow Traffic', link: '/guide/usage/shadow-traffic' },
          ],
        },
        {
          text: 'Advanced',
          items: [
            { text: 'Agent Teams', link: '/guide/advanced/agent-teams' },
            { text: 'Custom Providers', link: '/guide/advanced/custom-providers' },
            { text: 'Custom Tools', link: '/guide/advanced/custom-tools' },
            { text: 'Plugin System', link: '/guide/advanced/plugin-system' },
            { text: 'RAG Knowledge Base', link: '/guide/advanced/rag-knowledge-base' },
          ],
        },
        {
          text: 'SDK & Reference',
          items: [
            { text: 'Agent SDK', link: '/guide/sdk' },
            { text: 'Python SDK', link: '/guide/sdk-python' },
            { text: 'Benchmarks', link: '/guide/benchmarks' },
            { text: 'Troubleshooting', link: '/guide/troubleshooting' },
            { text: 'FAQ', link: '/guide/faq' },
            { text: 'Changelog', link: '/guide/changelog' },
          ],
        },
      ],
      '/architecture/': [
        {
          text: 'Architecture',
          items: [
            { text: 'Overview', link: '/architecture/overview' },
            { text: 'Core Call Chain', link: '/architecture/core-call-chain' },
            { text: 'Multi-Agent Orchestration', link: '/architecture/multi-agent' },
            { text: 'Agent Runtime', link: '/architecture/agent-runtime' },
            { text: 'Smart Model Router', link: '/architecture/smart-model-router' },
            { text: 'Advanced Features', link: '/architecture/advanced-features' },
          ],
        },
        {
          text: 'Reliability',
          items: [
            { text: 'Resilience', link: '/architecture/resilience' },
            { text: 'Event Sourcing & Recovery', link: '/architecture/event-sourcing' },
            { text: 'Saga Transactions', link: '/architecture/saga' },
            { text: 'Agent Transaction Runtime', link: '/architecture/atr' },
            { text: 'Supervision Tree', link: '/architecture/supervision-tree' },
            { text: 'Backpressure Control', link: '/architecture/backpressure' },
            { text: 'Verification Pipeline', link: '/architecture/verification' },
            { text: 'Caching', link: '/architecture/caching' },
          ],
        },
        {
          text: 'Performance',
          items: [
            { text: 'Speculative Execution', link: '/architecture/speculative-execution' },
            { text: 'Intelligence Layer', link: '/architecture/intelligence' },
          ],
        },
        {
          text: 'Security',
          items: [
            { text: 'Security Gateway', link: '/architecture/security-gateway' },
            { text: 'Security Sandbox', link: '/architecture/sandbox' },
            { text: 'Multi-Tenancy', link: '/architecture/multi-tenancy' },
          ],
        },
        {
          text: 'Systems',
          items: [
            { text: 'Tools', link: '/architecture/tools' },
            { text: 'MCP Integration', link: '/architecture/mcp' },
            { text: 'Channel Adapters', link: '/architecture/channel-adapters' },
            { text: 'Skills System', link: '/architecture/skills-system' },
            { text: 'Self-Evolution', link: '/architecture/self-evolution' },
            { text: 'Production Readiness', link: '/architecture/production-readiness' },
            { text: 'Extension Points', link: '/architecture/extension-points' },
          ],
        },
      ],
      '/api/': [
        {
          text: 'API Reference',
          items: [
            { text: 'Overview', link: '/api/overview' },
            { text: 'Task Complexity Analyzer', link: '/api/task-complexity-analyzer' },
            { text: 'Adaptive Orchestrator', link: '/api/adaptive-orchestrator' },
            { text: 'Token Budget Allocator', link: '/api/token-budget-allocator' },
            { text: 'Three-Layer Memory', link: '/api/three-layer-memory' },
            { text: 'Reflection Engine', link: '/api/reflection-engine' },
            { text: 'Consensus Checker', link: '/api/consensus-checker' },
            { text: 'Inspector Agent', link: '/api/inspector-agent' },
          ],
        },
      ],
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/PStarH/Commander' },
    ],

    search: {
      provider: 'local',
    },

    editLink: {
      // Default branch is master (not main)
      pattern: 'https://github.com/PStarH/commander-docs/edit/master/:path',
      text: 'Edit this page on GitHub',
    },

    lastUpdated: {
      text: 'Updated at',
      formatOptions: {
        dateStyle: 'medium',
      },
    },

    outline: {
      level: [2, 3],
      label: 'On this page',
    },

    docFooter: {
      prev: 'Previous',
      next: 'Next',
    },

    footer: {
      message: 'MIT Licensed — Built for multi-agent orchestration.',
      copyright: 'Copyright © 2026 Commander Contributors',
    },
  },
})
