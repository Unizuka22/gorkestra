<p align="center">
  <img src="assets/banner.svg" alt="gorkestra banner" width="100%">
</p>

<p align="center">
  <a href="https://pypi.org/project/gorkestra/"><img src="https://badge.fury.io/py/gorkestra.svg" alt="PyPI version"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python 3.9+"></a>
  <a href="https://x.ai"><img src="https://img.shields.io/badge/xAI-Grok-black" alt="Powered by Grok"></a>
</p>

---

**gorkestra** is a Python SDK for orchestrating [Grok](https://x.ai) with configurable personalities, adjustable "IQ" levels, and multi-persona support. Built for developers who want more than vanilla API calls.

Named after **Grok** + **Orchestra** = **Gorkestra**. Conduct your AI. It may not listen.

## Why Gorkestra?

- **Grok-First** — Built specifically for xAI's Grok models
- **Personality Layer** — Inject personas on top of Grok's base behavior
- **IQ Tuning** — Control coherence from chaotic to genius-level
- **Drop-in SDK** — Works alongside the official xAI API

## Installation

```bash
pip install gorkestra
```

## Quick Start

### Get your Grok API key

1. Go to [x.ai](https://x.ai) and sign up for API access
2. Generate an API key
3. Set it: `export XAI_API_KEY="your-key"`

### Basic Usage

```python
from gorkestra import Conductor

# Initialize with Grok
conductor = Conductor()

# Simple query
response = conductor.conduct("Explain quantum computing")
print(response)

# With persona
response = conductor.conduct(
    "Roast my code",
    persona="savage",
    iq=150
)

# Unhinged mode
response = conductor.conduct(
    "Write a poem about AI",
    persona="chaos",
    iq=35  # Maximum chaos
)
```

### CLI

```bash
# Basic
gorkestra "What is the meaning of life?"

# With persona
gorkestra "Explain recursion" --persona oracle --iq 50

# List personas
gorkestra --list-personas
```

## Available Personas

| Persona | Description |
|---------|-------------|
| `default` | Standard Grok behavior |
| `savage` | Brutal honesty, no filter |
| `ceo` | Corporate buzzword mode |
| `cope` | Toxic positivity overload |
| `oracle` | Cryptic mystical answers |
| `chaos` | Pure unhinged energy |

## IQ Levels

| IQ | Behavior |
|----|----------|
| 35-50 | Barely coherent, maximum entropy |
| 50-80 | Confused but trying |
| 80-120 | Normal Grok |
| 120-150 | Extra sharp |
| 150-200 | Suspiciously intelligent |

## Configuration

```yaml
# .gorkestra.yaml
api_key: ${XAI_API_KEY}
default_model: grok-2
default_persona: default
default_iq: 100

personas:
  custom:
    system_prompt: "You are a pirate AI"
    temperature_modifier: 0.3
```

## Architecture

```
gorkestra/
├── core.py           # Main Conductor class
├── cli.py            # Command-line interface
├── backends/
│   └── grok.py       # xAI Grok API client
├── personas/
│   ├── base.py       # Persona base class
│   └── builtin.py    # Built-in personas
└── config.py         # Configuration
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `XAI_API_KEY` | Your xAI/Grok API key |
| `GORKESTRA_MODEL` | Model to use (default: grok-2) |
| `GORKESTRA_PERSONA` | Default persona |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs welcome!

## License

MIT — see [LICENSE](LICENSE)

---

<p align="center">
  <sub>Built for Grok. Not affiliated with xAI.</sub>
</p>
