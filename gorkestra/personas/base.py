"""Base persona class."""

from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Persona:
    """
    Defines an agent's personality.
    
    Attributes:
        name: Unique identifier
        system_prompt: Core personality instructions
        voice: Speaking style hints
        temperature: Creativity level (0.0-2.0)
        traits: Personality traits
    """
    name: str
    system_prompt: str
    voice: Optional[str] = None
    temperature: float = 0.7
    traits: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if self.voice:
            self.system_prompt = f"{self.system_prompt}\n\nVoice: {self.voice}"
