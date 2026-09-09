#!/usr/bin/env node
import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs'
import { join, relative } from 'node:path'

const root = process.cwd()
const locales = ['zh', 'ja', 'ko', 'es', 'fr']
const pages = ['index.md', 'getting-started.md', 'deployment.md', 'operations.md', 'security.md', 'sdk.md', 'benchmarks.md', 'support.md']
const errors = []

for (const locale of locales) {
  for (const page of pages) {
    if (!existsSync(join(root, locale, page))) errors.push(`missing ${locale}/${page}`)
  }
}

function walk(dir, out = []) {
  for (const name of readdirSync(dir)) {
    if (['.git', '.vitepress', 'node_modules', '.omo'].includes(name)) continue
    const file = join(dir, name)
    if (statSync(file).isDirectory()) walk(file, out)
    else if (file.endsWith('.md') || file.endsWith('.mts')) out.push(file)
  }
  return out
}

const forbidden = [
  [/localhost:3001/, 'Commander API must not use port 3001'],
  [/\/api\/v1/, 'legacy API routes are not public documentation'],
  [/6700\+ tests/, 'fragile test-count marketing is not a public claim'],
  [/OpenClaw|PinchBench/, 'unverified competitive benchmark claim'],
  [/100% defense/i, 'benchmark claim needs an evidence level, not an absolute'],
]

for (const file of walk(root)) {
  const text = readFileSync(file, 'utf8')
  for (const [pattern, message] of forbidden) {
    if (pattern.test(text)) errors.push(`${relative(root, file)}: ${message}`)
  }
}

if (errors.length) {
  console.error(errors.join('\n'))
  process.exit(1)
}
console.log(`Validated ${pages.length} public pages in ${locales.length + 1} locales.`)
