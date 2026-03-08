<p align="center">
  <img src="assets/banner.svg" alt="gorkestra banner" width="100%">
</p>

<p align="center">
  <a href="https://pypi.org/project/gorkestra/"><img src="https://badge.fury.io/py/gorkestra.svg" alt="PyPI version"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python 3.9+"></a>
  <a href="https://github.com/Unizuka22/gorkestra"><img src="https://img.shields.io/badge/chaos-high-ff69b4" alt="Chaos Level: High"></a>
</p>

---

**gorkestra** is an LLM orchestration layer that wraps any AI backend with a configurable personality — from slightly unhinged to completely deranged.

It works like LangChain. It does not behave like LangChain.

## Features

- **Multiple Personas** — Switch between personalities on the fly
- **Adjustable IQ** — Control the chaos level (35 = very dumb, 200 = suspiciously coherent)
- **Multi-Backend** — Works with OpenAI, Anthropic Claude, and local Ollama models
- **CLI & Python API** — Use from terminal or import in your code
- **Extensible** — Create your own personas with custom system prompts

## Installation

```bash
pip install gorkestra
```

### Optional backends

```bash
pip install gorkestra[anthropic]   # Claude support
pip install gorkestra[ollama]      # Local models
pip install gorkestra[all]         # Everything
```

## Quickstart

### CLI Usage

```bash
# Basic usage
gorkestra "explain quantum physics"

# With persona
gorkestra "explain recursion" --persona oracle

# Adjust the IQ
gorkestra "write a poem" --persona roast --iq 35

# Use different backend
gorkestra "hello" --backend anthropic --model claude-3-opus
```

### Python API

```python
from gorkestra import Conductor

# Initialize with default settings
conductor = Conductor()

# Simple query
response = conductor.conduct("Explain machine learning")
print(response)

# With persona and IQ adjustment
response = conductor.conduct(
    "Write a startup pitch",
    persona="ceo",
    iq=150
)

# Using a different backend
from gorkestra import Conductor, AnthropicBackend

conductor = Conductor(backend=AnthropicBackend())
response = conductor.conduct("Hello", persona="oracle")
```

## Available Personas

| Persona | Description | Example Output |
|---------|-------------|----------------|
| `default` | Standard helpful assistant | Normal AI responses |
| `roast` | Savage, brutal honesty | "Your code is bad and you should feel bad" |
| `ceo` | Corporate buzzword generator | "Let's leverage synergies to disrupt the paradigm" |
| `cope` | Toxic positivity overload | "Everything is AMAZING and will be FINE" |
| `oracle` | Cryptic, mystical responses | "The answer lies within... or does it?" |

## IQ Levels

The `--iq` parameter controls response coherence:

| IQ Range | Behavior |
|----------|----------|
| 35-50 | Barely coherent, maximum chaos |
| 50-80 | Confused but trying |
| 80-120 | Normal operation |
| 120-150 | Surprisingly insightful |
| 150-200 | Suspiciously intelligent |

## Configuration

Create a `.gorkestra.yaml` in your project or home directory:

```yaml
default_backend: openai
default_persona: default
default_iq: 100

backends:
  openai:
    model: gpt-4
    api_key: ${OPENAI_API_KEY}
  
  anthropic:
    model: claude-3-sonnet
    api_key: ${ANTHROPIC_API_KEY}
  
  ollama:
    model: llama2
    host: http://localhost:11434

personas:
  custom_persona:
    system_prompt: "You are a helpful assistant who speaks like a pirate"
    temperature_modifier: 0.2
```

## Creating Custom Personas

```python
from gorkestra import Conductor, Persona

# Define a custom persona
pirate = Persona(
    name="pirate",
    system_prompt="You are a helpful assistant who speaks like a pirate. Use 'arr', 'matey', and nautical terms.",
    temperature_modifier=0.3
)

# Register and use
conductor = Conductor()
conductor.register_persona(pirate)

response = conductor.conduct("How do I install Python?", persona="pirate")
# "Arr matey! To install Python on yer ship..."
```

## Architecture

```
gorkestra/
├── core.py          # Main Conductor class
├── cli.py           # Command-line interface
├── backends/
│   ├── base.py      # Abstract backend class
│   ├── openai.py    # OpenAI implementation
│   ├── anthropic.py # Anthropic implementation
│   └── ollama.py    # Ollama implementation
├── personas/
│   ├── base.py      # Persona base class
│   └── builtin.py   # Built-in personas
└── config.py        # Configuration handling
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | OpenAI API key |
| `ANTHROPIC_API_KEY` | Anthropic API key |
| `GORKESTRA_DEFAULT_BACKEND` | Default backend to use |
| `GORKESTRA_DEFAULT_PERSONA` | Default persona |
| `GORKESTRA_CONFIG` | Path to config file |

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Hall of Fame

See [HALL_OF_FAME.md](HALL_OF_FAME.md) for our amazing contributors.

## License

MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">
  <i>"The AI will not listen. That's a feature, not a bug."</i>
</p>
