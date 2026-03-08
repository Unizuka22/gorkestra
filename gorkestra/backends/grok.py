"""xAI Grok API backend."""

import os
from typing import Optional
from .base import Backend

class GrokBackend(Backend):
    """xAI Grok API backend - the primary backend for gorkestra."""
    
    BASE_URL = "https://api.x.ai/v1"
    
    def __init__(
        self, 
        model: str = "grok-2", 
        api_key: Optional[str] = None,
        **kwargs
    ):
        super().__init__(model, **kwargs)
        self.api_key = api_key or os.getenv("XAI_API_KEY")
        self._client = None
    
    @property
    def client(self):
        if self._client is None:
            try:
                from openai import OpenAI
                self._client = OpenAI(
                    api_key=self.api_key,
                    base_url=self.BASE_URL
                )
            except ImportError:
                raise ImportError("openai package required for Grok. Install with: pip install openai")
        return self._client
    
    def complete(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1024,
        **kwargs
    ) -> str:
        """Generate completion using Grok."""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
        return response.choices[0].message.content
    
    def validate_config(self) -> bool:
        """Check if API key is configured."""
        return self.api_key is not None
    
    @classmethod
    def available_models(cls) -> list:
        """List available Grok models."""
        return [
            "grok-2",
            "grok-2-mini", 
            "grok-beta"
        ]
