<p align="center">
  <img src="assets/banner.svg" alt="gorkestra" width="100%">
</p>

<p align="center">
  <a href="https://pypi.org/project/gorkestra/"><img src="https://badge.fury.io/py/gorkestra.svg" alt="PyPI"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python"></a>
  <a href="https://x.ai"><img src="https://img.shields.io/badge/powered%20by-Grok-black" alt="Grok"></a>
</p>

<p align="center">
  <b>The LLM orchestration framework that thinks different.</b><br>
  Build autonomous AI agents powered by Grok. Ship to X. Break things.
</p>

---

## What is Gorkestra?

**Gorkestra** is an opinionated LLM orchestration framework built around xAI's Grok. Unlike generic LLM wrappers, Gorkestra is designed for building **autonomous agents** that can:

- **Think in chains** — Multi-step reasoning with memory
- **Use tools** — Web search, code execution, API calls
- **Adapt personality** — Dynamic persona switching based on context
- **Ship to X** — Native integration with the X/Twitter API
- **Self-improve** — Learn from interactions and feedback

## Core Concepts

### 1. Conductors
The brain of your agent. Orchestrates Grok with personas, tools, and memory.

```python
from gorkestra import Conductor

conductor = Conductor(
    model="grok-2",
    persona="analyst",
    tools=["web_search", "code_exec"],
    memory=True
)
```

### 2. Personas
Personality layers that shape how your agent thinks and responds.

```python
from gorkestra import Persona

crypto_degen = Persona(
    name="degen",
    voice="You're a crypto twitter degen. Use slang like 'gm', 'wagmi', 'ngmi'. Be bullish on everything.",
    temperature=0.9
)
```

### 3. Chains
Multi-step reasoning pipelines.

```python
from gorkestra import Chain, Step

research_chain = Chain([
    Step("search", "Find recent news about {topic}"),
    Step("analyze", "Analyze sentiment and key points"),
    Step("summarize", "Write a tweet-length summary"),
])

result = conductor.run_chain(research_chain, topic="AI agents")
```

### 4. Tools
Give your agent capabilities beyond text generation.

```python
from gorkestra.tools import WebSearch, CodeExec, XPost

conductor = Conductor(
    tools=[
        WebSearch(),           # Search the web
        CodeExec(sandbox=True), # Run Python code
        XPost(api_key="..."),  # Post to X
    ]
)
```

### 5. Memory
Persistent context across conversations.

```python
from gorkestra.memory import VectorMemory

conductor = Conductor(
    memory=VectorMemory(
        provider="chromadb",
        persist=True
    )
)

# Agent remembers previous conversations
conductor.conduct("Remember when we discussed AI safety?")
```

## Quick Start

```bash
pip install gorkestra
export XAI_API_KEY="your-key"
```

```python
from gorkestra import Conductor

# Simple agent
agent = Conductor()
response = agent.conduct("Explain quantum computing like I'm a crypto bro")

# With tools and memory
agent = Conductor(
    persona="researcher",
    tools=["web_search"],
    memory=True
)
response = agent.conduct("What's the latest on GPT-5?")
```

## CLI

```bash
# Interactive mode
gorkestra chat

# Single query
gorkestra ask "What is consciousness?"

# With persona
gorkestra ask "Roast this code" --persona savage --file code.py

# Run a chain
gorkestra chain research --topic "AI regulation"
```

## Built-in Personas

| Persona | Use Case |
|---------|----------|
| `default` | General assistant |
| `analyst` | Research & analysis |
| `creative` | Writing & ideation |
| `coder` | Programming help |
| `savage` | Unfiltered roasts |
| `degen` | Crypto/trading |
| `oracle` | Mystical wisdom |

## Architecture

```
gorkestra/
├── core/
│   ├── conductor.py    # Main orchestrator
│   ├── chain.py        # Multi-step chains
│   └── router.py       # Intent routing
├── personas/
│   ├── base.py         # Persona class
│   └── library.py      # Built-in personas
├── tools/
│   ├── base.py         # Tool interface
│   ├── search.py       # Web search
│   ├── code.py         # Code execution
│   └── x.py            # X/Twitter integration
├── memory/
│   ├── base.py         # Memory interface
│   ├── vector.py       # Vector store
│   └── graph.py        # Knowledge graph
└── agents/
    ├── base.py         # Agent base class
    └── prebuilt.py     # Ready-to-use agents
```

## X Integration

Post directly to X with Grok-powered content:

```python
from gorkestra import Conductor
from gorkestra.tools import XPost

agent = Conductor(
    persona="analyst",
    tools=[XPost(
        api_key="...",
        api_secret="...",
        access_token="...",
        access_secret="..."
    )]
)

# Generate and post
agent.conduct(
    "Write a thread about the future of AI agents, then post it",
    action="post"
)
```

## Why Gorkestra?

| Feature | Gorkestra | LangChain | Others |
|---------|-----------|-----------|--------|
| Grok-native | Yes | No | No |
| X integration | Built-in | Plugin | No |
| Persona system | First-class | Basic | Varies |
| Opinionated | Yes | No | Varies |
| Setup time | Minutes | Hours | Hours |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). We welcome:
- New personas
- Tool integrations
- Memory backends
- Bug fixes

## License

MIT License - see [LICENSE](LICENSE)

---

<p align="center">
  <sub>Built for builders. Powered by Grok. Not affiliated with xAI.</sub>
</p>
