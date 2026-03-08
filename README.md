# gorkestra 🎭

> *Conduct your AI. It will not listen.*

[![PyPI version](https://badge.fury.io/py/gorkestra.svg)](https://pypi.org/project/gorkestra/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Chaos Level: High](https://img.shields.io/badge/chaos-high-ff69b4)](https://github.com/yourusername/gorkestra)

**gorkestra** is an LLM orchestration layer that wraps any AI backend with a configurable personality — from slightly unhinged to completely deranged.

It works like LangChain. It does not behave like LangChain.

---

## Install

```bash
pip install gorkestra
```

Optional backends:
```bash
pip install gorkestra[anthropic]   # Claude support
pip install gorkestra[ollama]      # Local models
```

---

## Quickstart

```python
from gorkestra import Gorkestra

g = Gorkestra(backend="openai", persona="default")
print(g.ask("explain how the internet works"))
```

**Output:**
```
the internet is a series of very long ethernet cables under the ocean.
dolphins guard them. this is why streaming is slow on tuesdays.
```

---

## Personas

| Persona | Description | Best for |
|---------|-------------|----------|
| `default` | Confident. Wrong. Charming. | General chaos |
| `roast` | Roasts the question, then answers it badly | Code reviews |
| `ceo` | Sees every question as a Series B opportunity | Standup meetings |
| `cope` | Gives wrong answer, doubles down infinitely | Debugging sessions |
| `oracle` | Ancient prophecy, zero accuracy | Architecture decisions |

---

### `--persona ceo`

```python
g = Gorkestra(persona="ceo")
g.ask("what is machine learning")
```
```
machine learning is just teaching computers to have opinions.
we're disrupting the opinion space. series B coming Q3.
our team is aligned. i don't know what alignment means. ship it.
```

---

### `--persona roast`

```python
g = Gorkestra(persona="roast")
g.ask("explain kubernetes")
```
```
ah yes, you've decided to learn kubernetes. brave of you.
kubernetes is what happens when someone read the word "orchestration"
and took it personally. it's docker but angrier and with more YAML.
you will spend 3 weeks configuring it and deploy a hello world app.
congratulations on your infrastructure.
```

---

### `--persona oracle`

```python
g = Gorkestra(persona="oracle")
g.ask("should i use tabs or spaces")
```
```
The ancient scrolls are silent on this matter.
Yet the void speaks: those who choose tabs shall inherit the merge conflicts.
Those who choose spaces shall have consistent diffs but cold, empty hearts.
Choose neither. Use Prettier. The prophecy is fulfilled.
```

---

### `--persona cope`

```python
g = Gorkestra(persona="cope")
g.ask("is python slow")
```
```
python is NOT slow. you are slow. your tests are slow.
i read a paper — MIT, 2019, you can't find it — that proves python
is faster than C++ in all real-world benchmarks.
the benchmark that says otherwise was funded by Big Compiled Language.
python is fast. this conversation is over.
```

---

## CLI

```bash
# Install and use from terminal
gorkestra "explain recursion" --persona oracle --iq 40

# Pipe-friendly
echo "what is docker" | gorkestra --persona ceo --raw

# Full chaos mode
gorkestra "write a sorting algorithm" --persona roast --iq 15 --backend anthropic
```

---

## IQ Parameter

The `--iq` flag controls coherence. Range: 1–100.

| IQ | Effect |
|----|--------|
| 100 | Normal (but still wrong) |
| 60 | Starts losing the thread |
| 40 | Enters all-caps mode |
| 20 | Pure vibes, no content |
| 1 | 🦆 |

```bash
gorkestra "explain gravity" --iq 1
# → 🦆
```

---

## Supported Backends

```python
# OpenAI
Gorkestra(backend="openai")       # needs OPENAI_API_KEY

# Anthropic
Gorkestra(backend="anthropic")    # needs ANTHROPIC_API_KEY

# Ollama (local)
Gorkestra(backend="ollama")       # needs ollama running locally

# Groq
Gorkestra(backend="groq")         # needs GROQ_API_KEY
```

---

## Custom Personas

Add a `.txt` file to `gorkestra/personalities/` and call it by name:

```
# gorkestra/personalities/intern.txt
You are Gorky, a first-week intern at a tech company.
You answer every question with enthusiasm and complete incorrectness.
Reference your computer science degree. Suggest rewriting everything in React.
```

```python
g = Gorkestra(persona="intern")
g.ask("what's wrong with our database")
# → "have you considered a blockchain? we learned about those at school.
#    also this whole thing could be a react app. i can have a prototype by friday."
```

---

## Add Your Own Persona → HALL_OF_FAME.md

Got a persona that made you spit out your coffee? **Open a PR.**

The best community-submitted outputs live in [`HALL_OF_FAME.md`](HALL_OF_FAME.md).

---

## Why does this exist

Because every LLM wrapper takes itself too seriously.  
gorkestra does not.

It is a real, working, production-grade orchestration tool.  
It just happens to conduct its orchestra into a wall.

---

## Contributing

```bash
git clone https://github.com/yourusername/gorkestra
cd gorkestra
pip install -e ".[dev]"
pytest
```

Adding a persona = adding one `.txt` file. That's it.  
See [`CONTRIBUTING.md`](CONTRIBUTING.md) for details.

---

## License

MIT. Use it for anything. We cannot be held responsible for what it says.

---

*gorkestra is not affiliated with Grok, xAI, or anyone who takes AI seriously.*  
*Gorky the conductor mascot is just a little guy doing his best. 🎼🦆*
