# シャドートラフィック

> **ローカライズについて** · 見出しは翻訳済みです。コードと正確な API は英語原文を正とします。英語版：[English](/guide/usage/shadow-traffic)



Shadow traffic lets you compare two versions of Commander side-by-side without affecting production. A shadow proxy mirrors production requests to a shadow endpoint and reports drift in status, latency, and cost.

## Use Cases


- **Pre-deploy validation** — Compare current vs candidate version before rollout
- **Provider migration** — Test switching from OpenAI to Anthropic without risk
- **Configuration changes** — Validate new topology or routing rules
- **Regression detection** — Catch performance or quality degradation early

## クイックスタート


### 1. Create Configuration


```bash
cat > .commander/shadow-config.json <<EOF
{
  "enabled": true,
  "endpoint": "http://localhost:9999",
  "sampleRate": 0.1,
  "scrubPii": true,
  "diffMode": "status_cost_latency",
  "timeoutMs": 5000
}
EOF
```

### 2. Start Shadow Runner


```bash
npx tsx packages/core/src/cli/commands/shadow.ts runner --port=9999 &
```

### 3. Enable Proxy in Production


```bash
export COMMANDER_SHADOW_ENABLED=true
npx tsx packages/core/src/cli/index.ts serve
```

### 4. View Drift Reports


```bash
npx tsx packages/core/src/cli/commands/shadow.ts drift
```

## 設定


| Field | Default | Description |
|-------|---------|-------------|
| `enabled` | `false` | Enable shadow proxy |
| `endpoint` | `http://localhost:9999` | Shadow runner URL |
| `sampleRate` | `0.1` | Fraction of requests to mirror (0–1) |
| `scrubPii` | `true` | Strip PII before forwarding |
| `ignoreFields` | `["Authorization", "x-api-key", ...]` | Headers to always redact |
| `diffMode` | `status_cost_latency` | What to compare: `status_cost_latency` or `full_output` |
| `timeoutMs` | `5000` | Shadow request timeout |

## Drift Detection


The drift reporter compares production and shadow responses:

| Metric | Drift Threshold | What it means |
|--------|----------------|---------------|
| Status delta | >5% | Different HTTP status codes |
| Latency delta | >5% | Significant performance difference |
| Cost delta | >5% | Token cost divergence |

When any threshold is breached, a `DriftEntry` is recorded with full context.

## PII Scrubbing


Forced redacted headers (always redacted, not user-overridable):
- `Authorization`
- `x-api-key`
- `x-auth-token`
- `cookie`

Body PII patterns (delegated to `UniversalSanitizer`):
- API keys: OpenAI (`sk-`), Anthropic (`sk-ant-`), Stripe (`sk_live_`), Slack (`xox*`), GitHub (`ghp_*`), AWS (`AKIA*`)
- Secrets: JWT tokens, PEM private keys, SSN, passwords
- Personal: email addresses, phone numbers
- XSS: `<script>` tags, event handlers, `javascript:` URLs

## トラブルシューティング


| Issue | Solution |
|-------|----------|
| Shadow returns 502 | Runner not started. Check process is alive on port 9999 |
| No drift reports | `sampleRate` may be too low. Set to `1.0` for testing |
| PII leaking | Check `.commander/shadow-config.json` `ignoreFields` list |
| Timeout errors | Increase `timeoutMs` if shadow endpoint is slow |

## Programmatic API


```typescript
import { ShadowProxy, DriftReporter } from '@commander/core';

const proxy = new ShadowProxy({
  enabled: true,
  endpoint: 'http://localhost:9999',
  sampleRate: 0.1,
});

const reporter = new DriftReporter();

// Wrap your request handler
app.use(proxy.middleware());

// Check for drift
const drift = reporter.getDriftEntries();
const breaches = drift.filter(d => d.driftDetected);
```
