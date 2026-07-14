# Proveedores custom

Añade un backend LLM propio implementando la interfaz de proveedor y registrándolo en el runtime.

## Pasos

1. Extiende `BaseLLMProvider` (o implementa `LLMProvider`)  
2. Implementa `call(messages, options)`  
3. Registra con `registerProvider` / `runtime.registerProvider`  

```typescript
import { BaseLLMProvider } from '@commander/core';

class MyProvider extends BaseLLMProvider {
  async call(messages, options) {
    // HTTP a tu endpoint OpenAI-compatible o custom
    return { content: '...', usage: { totalTokens: 0 } };
  }
}

runtime.registerProvider('my-provider', new MyProvider());
```

## Variables de entorno

Sigue el patrón de [Proveedores](/es/guide/providers): key, base URL y modelo por defecto. El router podrá usarlo en la cadena de fallback si lo configuras.

## Checklist

- [ ] Timeouts y errores tipados  
- [ ] No filtrar secrets en logs  
- [ ] Tests de contrato (mensaje → respuesta)  
- [ ] Documentar env vars en tu deploy  

## Relacionado

- [Proveedores](/es/guide/providers)  
- [Router de modelos](/es/architecture/smart-model-router)
