"""Base persona class."""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Persona:
    """Defines a personality for the AI conductor."""
    
    name: str
    system_prompt: str
    temperature_modifier: float = 0.0
    description: Optional[str] = None
    
    def get_temperature(self, base_temp: float) -> float:
        """Calculate adjusted temperature."""
        return max(0.0, min(2.0, base_temp + self.temperature_modifier))
    
    def format_prompt(self, iq: int = 100) -> str:
        """Format the system prompt with IQ adjustment."""
        iq_modifier = ""
        if iq < 50:
            iq_modifier = "\n\nIMPORTANT: You are incredibly confused and barely coherent. Make mistakes. Ramble. Forget what you were saying."
        elif iq < 80:
            iq_modifier = "\n\nNote: You're a bit slow today. Simple words. Short sentences. Maybe misunderstand things."
        elif iq > 150:
            iq_modifier = "\n\nNote: You are extraordinarily intelligent. Use sophisticated vocabulary. Make unexpected connections."
        
        return self.system_prompt + iq_modifier
