"""Base backend class for LLM providers."""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

class Backend(ABC):
    """Abstract base class for LLM backends."""
    
    def __init__(self, model: Optional[str] = None, **kwargs):
        self.model = model
        self.config = kwargs
    
    @abstractmethod
    def complete(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1024,
        **kwargs
    ) -> str:
        """Generate a completion for the given prompt."""
        pass
    
    @abstractmethod
    def validate_config(self) -> bool:
        """Validate the backend configuration."""
        pass
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(model={self.model})"
