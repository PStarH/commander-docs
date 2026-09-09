# Security and privacy

> This page is synchronized from the canonical English documentation. 日本語 navigation is available; commands and product limits are identical in every locale.

## Security boundary

Commander supports bearer authentication, configurable CORS, input validation,
structured logging, and local-first operation. Configure these controls for
your environment; they do not replace an application threat model.

The Enterprise Gateway uses an alpha multi-tenant path. Do not rely on it as a
production-proven isolation boundary.

## Data and credentials

- Keep provider API keys and `COMMANDER_API_KEY` outside source control.
- Restrict which tools can access customer systems.
- Review logs, retention settings, and backups for customer data.
- Define deletion and incident-response procedures before a pilot.

## Disclosure

Report security vulnerabilities privately as described in the repository
`SECURITY.md`. Public issues are not an appropriate disclosure channel.

## Compliance

Any ISO 42001 or NIST AI RMF material is reporting support, not certification.
Commander does not claim a SOC 2 report on this site.