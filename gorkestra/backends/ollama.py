"""Ollama local model backend."""

from typing import Optional
from .base import Backend

class OllamaBackend(Backend):
    """Ollama local model backend."""
    
    def __init__(self, model: str = "llama2", host: str = "http://localhost:11434", **kwargs):
        super().__init__(model, **kwargs)
        self.host = host
        self._client = None
    
    @property
    def client(self):
        if self._client is None:
            try:
                import ollama
                self._client = ollama.Client(host=self.host)
            except ImportError:
                raise ImportError("ollama package required. Install with: pip install ollama")
        return self._client
    
    def complete(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1024,
        **kwargs
    ) -> str:
        response = self.client.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt or ""},
                {"role": "user", "content": prompt}
            ],
            options={"temperature": temperature, "num_predict": max_tokens}
        )
        return response["message"]["content"]
    
    def validate_config(self) -> bool:
        try:
            self.client.list()
            return True
        except:
            return False
