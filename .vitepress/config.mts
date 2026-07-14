import { defineConfig } from 'vitepress'

const siteUrl = 'https://pstarh.github.io/commander-docs/'
const description =
  'Multi-agent orchestration engine — 25 providers · 5 canonical topologies · 18 built-in tools · 6700+ tests'

export default defineConfig({
  title: 'Commander',
  description,
  lang: 'en-US',
  base: '/commander-docs/',

  cleanUrls: false,
  lastUpdated: true,
  ignoreDeadLinks: [
    // Local dev URLs in install/console docs are intentional
    /^https?:\/\/localhost/,
  ],

  sitemap: {
    hostname: 'https://pstarh.github.io/commander-docs/',
  },

  vite: {
    ssr: {
      noExternal: ['gsap', 'gsap/ScrollTrigger'],
    },
  },

  head: [
    // Paths under head are NOT auto-prefixed with base — include it explicitly
    ['link', { rel: 'icon', href: '/commander-docs/favicon.svg', type: 'image/svg+xml' }],
    ['link', { rel: 'canonical', href: siteUrl }],
    ['meta', { name: 'theme-color', content: '#09090b' }],
    ['meta', { name: 'author', content: 'Commander Contributors' }],
    ['meta', { name: 'keywords', content: 'multi-agent, orchestration, LLM, commander, AI agents, SSE, topology' }],

    // Open Graph
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:url', content: siteUrl }],
    ['meta', { property: 'og:title', content: 'Commander — Multi-Agent Orchestration Engine' }],
    ['meta', { property: 'og:description', content: description }],
    ['meta', { property: 'og:site_name', content: 'Commander Docs' }],
    ['meta', { property: 'og:image', content: 'https://pstarh.github.io/commander-docs/og.png' }],
    ['meta', { property: 'og:image:width', content: '1200' }],
    ['meta', { property: 'og:image:height', content: '630' }],

    // Twitter
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title', content: 'Commander — Multi-Agent Orchestration Engine' }],
    ['meta', { name: 'twitter:description', content: description }],
    ['meta', { name: 'twitter:image', content: 'https://pstarh.github.io/commander-docs/og.png' }],

    // JSON-LD
    [
      'script',
      { type: 'application/ld+json' },
      JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'SoftwareApplication',
        name: 'Commander',
        applicationCategory: 'DeveloperApplication',
        operatingSystem: 'Cross-platform',
        license: 'https://opensource.org/licenses/MIT',
        url: 'https://github.com/PStarH/Commander',
        description,
        offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' },
      }),
    ],
  ],

  themeConfig: {
    // themeConfig.logo IS auto-prefixed with base — do NOT include /commander-docs/
    logo: '/logo.svg',

    siteTitle: 'Commander',

    nav: [
      { text: 'Guide', link: '/guide/getting-started', activeMatch: '/guide/' },
      { text: 'Architecture', link: '/architecture/overview', activeMatch: '/architecture/' },
      { text: 'API', link: '/api/overview', activeMatch: '/api/' },
      { text: 'Cookbook', link: '/guide/cookbook/', activeMatch: '/guide/cookbook/' },
      { text: 'Deployment', link: '/deployment', activeMatch: '/deployment' },
      { text: 'Community', link: '/community', activeMatch: '/community' },
    ],

    sidebar: {
      '/guide/': [
        {
          text: 'Getting Started',
          items: [
            { text: 'Quick Start', link: '/guide/getting-started' },
            { text: 'Why Commander', link: '/guide/why-commander' },
            { text: 'Installation', link: '/guide/installation' },
            { text: 'Web Console', link: '/guide/web-console' },
            { text: 'Commands', link: '/guide/commands' },
            { text: 'Providers', link: '/guide/providers' },
            { text: 'Configuration', link: '/guide/configuration' },
          ],
        },
        {
          text: 'Cookbook',
          items: [
            { text: 'Overview', link: '/guide/cookbook/' },
            { text: 'Security audit', link: '/guide/cookbook/security-audit' },
            { text: 'Refactor a module', link: '/guide/cookbook/refactor-module' },
            { text: 'CI full-auto lint fix', link: '/guide/cookbook/ci-full-auto' },
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
            { text: 'Security', link: '/guide/security' },
            { text: 'V2 Migration', link: '/guide/migration-v2' },
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
          text: 'Start here',
          items: [
            { text: 'Overview', link: '/architecture/overview' },
            { text: 'Core Call Chain', link: '/architecture/core-call-chain' },
            { text: 'Multi-Agent Orchestration', link: '/architecture/multi-agent' },
            { text: 'Agent Runtime', link: '/architecture/agent-runtime' },
          ],
        },
        {
          text: 'Core',
          collapsed: true,
          items: [
            { text: 'Smart Model Router', link: '/architecture/smart-model-router' },
            { text: 'Advanced Features', link: '/architecture/advanced-features' },
          ],
        },
        {
          text: 'Reliability',
          collapsed: true,
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
          collapsed: true,
          items: [
            { text: 'Speculative Execution', link: '/architecture/speculative-execution' },
            { text: 'Intelligence Layer', link: '/architecture/intelligence' },
          ],
        },
        {
          text: 'Security',
          collapsed: true,
          items: [
            { text: 'Security Gateway', link: '/architecture/security-gateway' },
            { text: 'Security Sandbox', link: '/architecture/sandbox' },
            { text: 'Multi-Tenancy', link: '/architecture/multi-tenancy' },
          ],
        },
        {
          text: 'Systems',
          collapsed: true,
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
          text: 'Public integration',
          items: [
            { text: 'Overview (Layer 1 & 2)', link: '/api/overview' },
          ],
        },
        {
          text: 'Runtime components (Layer 2)',
          items: [
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
