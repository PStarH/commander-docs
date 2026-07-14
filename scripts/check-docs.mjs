#!/usr/bin/env node
/**
 * Content guards for commander-docs — fail CI on metric/CLI/base drift.
 */
import { readdirSync, readFileSync, statSync } from 'node:fs'
import { join, relative } from 'node:path'

const root = process.cwd()
const errors = []
const warnings = []

function walk(dir, acc = []) {
  for (const name of readdirSync(dir)) {
    if (name === 'node_modules' || name === '.vitepress' || name === '.git') continue
    const p = join(dir, name)
    const st = statSync(p)
    if (st.isDirectory()) walk(p, acc)
    else if (/\.(md|mts|vue|ts|js|mjs|css)$/.test(name)) acc.push(p)
  }
  return acc
}

const files = walk(root)

// --- Forbidden patterns (content drift) ---
const forbidden = [
  { re: /npx tsx cli\.ts\b/, msg: 'Use packages/core/src/cliEntry.ts instead of bare cli.ts' },
  { re: /\b22 providers\b/i, msg: 'Metric drift: use 25 providers' },
  { re: /\b24 providers\b/i, msg: 'Metric drift: use 25 providers' },
  { re: /\b17 built-in tools\b/i, msg: 'Metric drift: use 18 built-in tools' },
  { re: /\b6,742\b/, msg: 'Prefer 6700+ over exact fragile count' },
  { re: /OLLAMA_HOST\b/, msg: 'Use OLLAMA_BASE_URL / OLLAMA_API_KEY' },
  {
    re: /logo:\s*['"]\/commander-docs\//,
    msg: 'themeConfig.logo must not include base path (VitePress prefixes it)',
  },
]

for (const file of files) {
  const rel = relative(root, file)
  if (rel.includes('scripts/check-docs')) continue
  const text = readFileSync(file, 'utf8')
  for (const { re, msg } of forbidden) {
    if (re.test(text)) {
      const line = text.split('\n').findIndex((l) => re.test(l)) + 1
      errors.push(`${rel}:${line}: ${msg}`)
    }
  }
}

// --- Required public assets ---
const requiredAssets = ['public/og.png', 'public/robots.txt', 'public/llms.txt', 'public/logo.svg']
for (const a of requiredAssets) {
  try {
    statSync(join(root, a))
  } catch {
    errors.push(`missing required asset: ${a}`)
  }
}

// --- Home.vue must use withBase for internal CTAs ---
const home = readFileSync(join(root, '.vitepress/theme/components/Home.vue'), 'utf8')
if (!home.includes('withBase')) {
  errors.push('Home.vue must import/use withBase for GH Pages')
}
if (!home.includes('prefersReducedMotion') && !home.includes('prefers-reduced-motion')) {
  warnings.push('Home.vue should respect prefers-reduced-motion')
}

// --- Config must declare locales.zh ---
const cfg = readFileSync(join(root, '.vitepress/config.mts'), 'utf8')
if (!cfg.includes("zh:") && !cfg.includes('zh: {')) {
  errors.push('config.mts should define zh locale')
}
if (!cfg.includes('25 providers')) {
  errors.push('config description should mention 25 providers')
}

// --- zh locale pages exist ---
const zhRequired = [
  'zh/index.md',
  'zh/guide/getting-started.md',
  'zh/guide/why-commander.md',
  'zh/guide/faq.md',
]
for (const p of zhRequired) {
  try {
    statSync(join(root, p))
  } catch {
    errors.push(`missing zh page: ${p}`)
  }
}

if (warnings.length) {
  console.log('Warnings:')
  for (const w of warnings) console.log('  ⚠', w)
}

if (errors.length) {
  console.error('check-docs failed:\n')
  for (const e of errors) console.error('  ✗', e)
  process.exit(1)
}

console.log(`check-docs OK (${files.length} files scanned)`)
