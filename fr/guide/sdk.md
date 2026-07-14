# Agent SDK (TypeScript)

```typescript
import { CommanderClient, createClient } from '@commander/sdk';

const client = new CommanderClient({ provider: 'openai' });
await client.connect();
const result = await client.run('analyze this repository');
await client.disconnect();
```

Publication npm en cours — monorepo-first.

[Déploiement](/fr/deployment) · [Python](/fr/guide/sdk-python)
