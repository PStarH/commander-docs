# Fournisseurs

Commander prend en charge **25 fournisseurs LLM**. Une variable d’environnement suffit.

| Variable | Fournisseur |
|----------|-------------|
| `OPENAI_API_KEY` | OpenAI / DeepSeek / GLM / MiMo |
| `ANTHROPIC_API_KEY` | Anthropic |
| `GOOGLE_API_KEY` | Gemini |
| `GROQ_API_KEY` | Groq |
| `OLLAMA_BASE_URL` | Ollama (local) |
| `VLLM_BASE_URL` | vLLM (local) |
| `XAI_API_KEY` | xAI |
| `OPENROUTER_API_KEY` | OpenRouter |
| … | Voir le monorepo `providerRegistry.ts` pour la liste complète (25) |

```bash
export OPENAI_API_KEY=sk-...
```

Le routeur choisit selon complexité, coût, latence et fallback.
