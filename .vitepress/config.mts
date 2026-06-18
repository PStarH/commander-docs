import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Commander',
  description: 'Multi-agent orchestration engine — 18 providers · 8 topologies · 25+ tools · 330+ tests',
  lang: 'en-US',
  base: '/commander-docs/',

  head: [
    ['link', { rel: 'icon', href: '/commander-docs/favicon.svg', type: 'image/svg+xml' }],
    ['meta', { name: 'theme-color', content: '#4f46e5' }],
    ['meta', { property: 'og:title', content: 'Commander — Multi-Agent Orchestration Engine' }],
    ['meta', { property: 'og:description', content: 'Orchestrate multiple agents across any topology — sequential, parallel, hierarchical, debate, ensemble, evaluator-optimizer — backed by 18 LLM providers.' }],
  ],

  themeConfig: {
    logo: '/commander-docs/logo.svg',

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
          ],
        },
        {
          text: 'SDK',
          items: [
            { text: 'Agent SDK', link: '/guide/sdk' },
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
            { text: 'Tools', link: '/architecture/tools' },
            { text: 'Production Readiness', link: '/architecture/production-readiness' },
            { text: 'Multi-Tenancy', link: '/architecture/multi-tenancy' },
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
      pattern: 'https://github.com/PStarH/Commander/edit/main/docs/:path',
      text: 'Edit this page on GitHub',
    },

    footer: {
      message: 'MIT Licensed — Built for multi-agent orchestration.',
      copyright: 'Copyright © 2026 Commander Contributors',
    },
  },
})
