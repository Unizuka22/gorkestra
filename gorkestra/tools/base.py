"""Base tool interface."""

from abc import ABC, abstractmethod
from typing import Any, Dict

class Tool(ABC):
    """Base class for agent tools."""
    
    name: str
    description: str
    
    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """Execute the tool."""
        pass
    
    def to_schema(self) -> Dict:
        """Return JSON schema for the tool."""
        return {
            "name": self.name,
            "description": self.description
        }
