import { defineConfig, type DefaultTheme } from 'vitepress'

const locales = ['zh', 'ja', 'ko', 'es', 'fr'] as const

function prefix(locale: string, path: string) {
  return locale === 'en' ? path : `/${locale}${path}`
}

function theme(locale: string): DefaultTheme.Config {
  const link = (path: string) => prefix(locale, path)
  return {
    nav: [
      { text: 'Overview', link: link('/') },
      { text: 'Quick start', link: link('/getting-started') },
      { text: 'Deployment', link: link('/deployment') },
      { text: 'Security', link: link('/security') },
    ],
    sidebar: [
      {
        text: 'Commander',
        items: [
          { text: 'Overview', link: link('/') },
          { text: 'Quick start', link: link('/getting-started') },
          { text: 'Deployment', link: link('/deployment') },
          { text: 'Operations and rollback', link: link('/operations') },
          { text: 'Security and privacy', link: link('/security') },
          { text: 'SDKs and API', link: link('/sdk') },
          { text: 'Benchmarks', link: link('/benchmarks') },
          { text: 'Support and limits', link: link('/support') },
        ],
      },
    ],
    socialLinks: [{ icon: 'github', link: 'https://github.com/PStarH/Commander' }],
    editLink: {
      pattern: 'https://github.com/PStarH/commander-docs/edit/master/:path',
      text: 'Edit this page on GitHub',
    },
    footer: {
      message: 'MIT licensed.',
      copyright: 'Copyright 2026 Commander Contributors',
    },
  }
}

export default defineConfig({
  title: 'Commander',
  description: 'Local-first multi-agent orchestration for engineers.',
  base: '/commander-docs/',
  cleanUrls: false,
  lastUpdated: true,
  ignoreDeadLinks: [/^https?:\/\/localhost/],
  sitemap: { hostname: 'https://pstarh.github.io/commander-docs/' },
  themeConfig: theme('en'),
  locales: {
    root: { label: 'English', lang: 'en-US', themeConfig: theme('en') },
    ...Object.fromEntries(locales.map((locale) => [locale, {
      label: locale.toUpperCase(),
      lang: locale,
      link: `/${locale}/`,
      themeConfig: theme(locale),
    }])),
  },
})
