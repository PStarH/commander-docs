# Agent Teams

**Agent Teams.** Cette page décrit un composant d’architecture Commander. Le texte ci-dessous reprend la structure du monorepo en français opérationnel ; les blocs de code restent en anglais.

Métriques produit : **25** fournisseurs · **5** topologies · **18** tools · **6700+** tests.

CLI monorepo : `npx tsx packages/core/src/cliEntry.ts` · après build : `commander`

## Contenu principal

### Vue d’ensemble

En pratique, **Overview** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/agent-teams) pour le détail exhaustif.

### Creating a Team

En pratique, **Creating a Team** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/agent-teams) pour le détail exhaustif.

### Agent Communication

En pratique, **Agent Communication** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/agent-teams) pour le détail exhaustif.

### Team Topologies

En pratique, **Team Topologies** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/agent-teams) pour le détail exhaustif.

### Persistence

En pratique, **Persistence** s’intègre au runtime avec les portes de qualité, le DLQ et les circuit breakers. Consultez le monorepo pour le code source et la [référence anglaise](/guide/advanced/agent-teams) pour le détail exhaustif.

## Exemples (code inchangé)

```typescript
import { AgentTeamManager } from '@commander/core';

const team = new AgentTeamManager('team-1');

// Register agents
const leadId = team.registerAgent({
  id: 'lead',
  name: 'Lead Architect',
  role: 'architect',
  capabilities: ['system-design', 'code-review'],
});

const backendId = team.registerAgent({
  id: 'backend',
  name: 'Backend Specialist',
  role: 'engineer',
  capabilities: ['api-design', 'database'],
});

const frontendId = team.registerAgent({
  id: 'frontend',
  name: 'Frontend Specialist',
  role: 'engineer',
  capabilities: ['ui', 'react'],
});
```

```typescript
// Send a message to an agent
await team.sendMessage({
  from: leadId,
  to: backendId,
  subject: 'Design API endpoints',
  body: 'Need a REST API for the user module. Design the endpoints.',
  priority: 'high',
});

// Agent reads its inbox
const inbox = await team.getInbox(backendId);
const messages = inbox.getMessages();

// Agent replies
await team.sendMessage({
  from: backendId,
  to: leadId,
  subject: 'Re: Design API endpoints',
  body: 'Proposed endpoints:\nGET /users\nPOST /users\nGET /users/:id',
});
```

```typescript
// Resume a team from a previous session
const existingTeam = await AgentTeamManager.load('team-1');
```

## Opérations

```bash
npx tsx packages/core/src/cliEntry.ts doctor
npx tsx packages/core/src/cliEntry.ts status
curl -s http://localhost:4000/health/detailed || true
```

## Voir aussi

- [Vue d’architecture](/fr/architecture/overview)
- [Prêt production](/fr/architecture/production-readiness)
- [Sécurité](/fr/guide/security)
- [Démarrage rapide](/fr/guide/getting-started)
