# Benchmarks

> This page is synchronized from the canonical English documentation. 简体中文 navigation is available; commands and product limits are identical in every locale.

Commander maintains benchmarks for regression detection and development
feedback. They are not production SLAs, SOC evidence, or independent product
certifications.

## Evidence levels

- **Simulated or fixture:** exercises an in-process or scripted harness.
- **CI baseline:** detects regressions in a controlled build environment.
- **Production measurement:** requires a defined customer workload and an
  operational measurement window; this site does not claim one.

The repository benchmark guide records runnable commands and methodology. Some
capability suites are scaffolds or offline fixtures and must not be read as
external leaderboard results.

## What to evaluate

For a pilot, measure your own workload: tool permissions, provider failure
handling, latency, cost, data handling, and rollback behavior. Preserve the
inputs and environment used for comparison.