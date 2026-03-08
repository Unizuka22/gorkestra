"""Core LLM adapter — wraps any backend with Gork energy."""
from typing import Optional
import os

BACKENDS = ["openai", "anthropic", "ollama", "groq"]

class Gorkestra:
    def __init__(self, backend: str = "openai", persona: str = "default", iq: int = 100):
        self.backend = backend
        self.persona = persona
        self.iq = max(1, min(iq, 100))  # 1–100, lower = funnier
        self._load_personality()

    def _load_personality(self):
        import importlib.resources as pkg
        path = pkg.files("gorkestra.personalities") / f"{self.persona}.txt"
        self.system_prompt = path.read_text()

    def ask(self, prompt: str) -> str:
        """Send a prompt through the Gork pipeline."""
        degraded = self._degrade(prompt)
        return self._call_backend(degraded)

    def _degrade(self, prompt: str) -> str:
        """Apply IQ degradation to the system prompt."""
        if self.iq < 40:
            return prompt.upper()  # shouting = confused
        return prompt

    def _call_backend(self, prompt: str) -> str:
        """Route to the correct LLM backend."""
        if self.backend == "openai":
            return self._openai(prompt)
        elif self.backend == "anthropic":
            return self._anthropic(prompt)
        raise ValueError(f"Unknown backend: {self.backend}. Choose from {BACKENDS}")

    def _openai(self, prompt: str) -> str:
        from openai import OpenAI
        client = OpenAI()
        res = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return res.choices[0].message.content

    def _anthropic(self, prompt: str) -> str:
        import anthropic
        client = anthropic.Anthropic()
        res = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=self.system_prompt,
            messages=[{"role": "user", "content": prompt}]
        )
        return res.content[0].text
