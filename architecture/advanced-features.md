# Advanced Engine Features

Commander includes several advanced engine components for sophisticated execution control.

## Speculative Executor

The speculative executor runs multiple execution paths in parallel and selects the best result:

```typescript
import { SpeculativeExecutor } from '@commander/core';

const executor = new SpeculativeExecutor();

// Run 3 speculative paths in parallel
const results = await executor.executeSpeculative(task, {
  strategies: [
    { provider: 'deepseek', temperature: 0.3 },
    { provider: 'openai', temperature: 0.5 },
    { provider: 'anthropic', temperature: 0.7 },
  ],
  selector: 'quality', // Pick the highest quality result
});
```

## Entropy Gater

Filters out low-confidence agent outputs using entropy-based detection:

```typescript
import { EntropyGater } from '@commander/core';

const gater = new EntropyGater({ threshold: 0.7 });

// Filter unreliable outputs
const filtered = gater.filter(agentOutputs);
// Only returns outputs with confidence > 0.7
```

## Cycle Detector

Detects and breaks dependency cycles in task graphs:

```typescript
import { CycleDetector } from '@commander/core';

const detector = new CycleDetector();

if (detector.hasCycle(taskGraph)) {
  const broken = detector.breakCycles(taskGraph);
  // Reorders tasks to eliminate circular dependencies
}
```

## Context Window Manager

Intelligently manages LLM context windows to prevent overflow:

```typescript
import { ContextWindowManager } from '@commander/core';

const manager = new ContextWindowManager({
  maxTokens: 128000,
  strategy: 'sliding', // 'sliding' | 'summary' | 'truncate'
});

const optimized = await manager.optimize(messages);
// Automatically compacts context when approaching limits
```

## Code Extractor

Extracts code blocks from LLM responses with format validation:

```typescript
import { CodeExtractor } from '@commander/core';

const extractor = new CodeExtractor();

const code = extractor.extract(response, {
  language: 'typescript',
  validate: true, // Validate syntax after extraction
});
```

## Format Bridge

Converts between different data formats automatically:

```typescript
import { FormatBridge } from '@commander/core';

const bridge = new FormatBridge();

const json = bridge.convert(yamlData, 'yaml', 'json');
const markdown = bridge.convert(htmlTable, 'html', 'markdown');
```

## Evolutionary Workflow Engine

Self-improving workflows that adapt based on past outcomes:

```typescript
import { EvolutionaryWorkflowEngine } from '@commander/core';

const engine = new EvolutionaryWorkflowEngine();

// Workflow evolves over time based on success/failure
const workflow = await engine.evolve('code-review', {
  generations: 10,
  mutationRate: 0.2,
});
```

## Structured Output

Parse and validate structured outputs from LLM responses:

```typescript
import { StructuredOutput } from '@commander/core';

const parser = new StructuredOutput();

const result = await parser.parse(response, {
  schema: {
    type: 'object',
    properties: {
      summary: { type: 'string' },
      confidence: { type: 'number' },
      actions: { type: 'array' },
    },
  },
});
```

## Parameter Controller

Dynamic parameter adjustment based on task context:

```typescript
import { ParameterController } from '@commander/core';

const controller = new ParameterController();

const params = controller.optimize({
  task: task,
  provider: 'openai',
  defaultParams: { temperature: 0.7, maxTokens: 4096 },
});
// Adjusts temperature, top_p, etc. based on task characteristics
```

## Config Validator

Validates Commander configuration at startup:

```typescript
import { ConfigValidator } from '@commander/core';

const validator = new ConfigValidator();

const errors = validator.validate(config);
if (errors.length > 0) {
  console.error('Config errors:', errors);
}
```

## OpenTelemetry Exporter

Export traces to OpenTelemetry-compatible backends:

```bash
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
export OTEL_SERVICE_NAME=commander

npx tsx packages/core/src/cliEntry.ts run "task"
# Traces exported to your OTLP endpoint
```
