import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Commander',
  description: 'Multi-agent orchestration engine — 18 providers · 8 topologies · 25+ tools · 330+ tests',
  lang: 'en-US',
  base: '/commander-docs/',

  head: [
    ['link', { rel: 'icon', href: '/commander-docs/favicon.svg', type: 'image/svg+xml' }],
    ['meta', { name: 'theme-color', content: '#6366f1' }],
    ['meta', { property: 'og:title', content: 'Commander — Multi-Agent Orchestration Engine' }],
    ['meta', { property: 'og:description', content: 'Orchestrate multiple agents across any topology — sequential, parallel, hierarchical, debate, ensemble, evaluator-optimizer — backed by 18 LLM providers.' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
  ],

  appearance: 'dark',

  themeConfig: {
    logo: '/commander-docs/logo.svg',

    nav: [
      { text: 'Guide', link: '/guide/getting-started', activeMatch: '/guide/' },
      { text: 'Architecture', link: '/architecture/overview', activeMatch: '/architecture/' },
      { text: 'API', link: '/api/overview', activeMatch: '/api/' },
      { text: 'Benchmarks', link: '/benchmarks', activeMatch: '/benchmarks' },
      { text: 'Deployment', link: '/deployment', activeMatch: '/deployment' },
      { text: 'FAQ', link: '/guide/faq', activeMatch: '/guide/faq' },
    ],

    sidebar: {
      '/guide/': [
        {
          text: 'Getting Started',
          items: [
            { text: 'Quick Start', link: '/guide/getting-started' },
            { text: 'Installation', link: '/guide/installation' },
            { text: 'CLI Commands', link: '/guide/commands' },
            { text: 'Providers', link: '/guide/providers' },
            { text: 'Configuration', link: '/guide/configuration' },
          ],
        },
        {
          text: 'Usage',
          items: [
            { text: 'Running Tasks', link: '/guide/usage/running-tasks' },
            { text: 'Plan Mode', link: '/guide/usage/plan-mode' },
            { text: 'Watch Mode (SSE)', link: '/guide/usage/watch-mode' },
            { text: 'Topology Decision Tree', link: '/guide/usage/topology-decision-tree' },
          ],
        },
        {
          text: 'Advanced',
          items: [
            { text: 'Custom Tools', link: '/guide/advanced/custom-tools' },
            { text: 'Custom Providers', link: '/guide/advanced/custom-providers' },
            { text: 'Plugin System', link: '/guide/advanced/plugin-system' },
            { text: 'Agent Teams', link: '/guide/advanced/agent-teams' },
          ],
        },
        {
          text: 'Reference',
          items: [
            { text: 'Agent SDK', link: '/guide/sdk' },
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
            { text: 'Tools (28)', link: '/architecture/tools' },
            { text: 'Security Sandbox', link: '/architecture/sandbox' },
            { text: 'Model Context Protocol', link: '/architecture/mcp' },
            { text: 'Skills System', link: '/architecture/skills-system' },
            { text: 'Channel Adapters', link: '/architecture/channel-adapters' },
            { text: 'Production Readiness', link: '/architecture/production-readiness' },
            { text: 'Multi-Tenancy', link: '/architecture/multi-tenancy' },
            { text: 'Extension Points', link: '/architecture/extension-points' },
            { text: 'Advanced Features', link: '/architecture/advanced-features' },
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
      { icon: 'github', link: 'https://github.com/sampan/Commander' },
    ],

    search: {
      provider: 'local',
    },

    editLink: {
      pattern: 'https://github.com/sampan/Commander/edit/main/docs/:path',
      text: 'Edit this page on GitHub',
    },

    footer: {
      message: 'MIT Licensed — Built for multi-agent orchestration.',
      copyright: 'Copyright © 2026 Commander Contributors',
    },
  },
})
