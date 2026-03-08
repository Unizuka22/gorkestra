"""Base memory interface."""

from abc import ABC, abstractmethod
from typing import Optional, List

class Memory(ABC):
    """Base class for memory backends."""
    
    @abstractmethod
    def store(self, query: str, response: str, metadata: dict = None):
        """Store an interaction."""
        pass
    
    @abstractmethod
    def recall(self, query: str, limit: int = 5) -> Optional[str]:
        """Recall relevant memories."""
        pass
    
    @abstractmethod
    def clear(self):
        """Clear all memories."""
        pass
