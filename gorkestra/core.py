"""Core conductor class - orchestrate Grok with personality."""

from typing import Optional, Dict, Any
from .backends.base import Backend
from .backends.grok import GrokBackend
from .personas.base import Persona
from .personas.builtin import get_persona, PERSONAS

class Conductor:
    """
    Orchestrate Grok with configurable personalities.
    
    Example:
        conductor = Conductor()
        response = conductor.conduct("Hello!", persona="savage", iq=35)
    """
    
    def __init__(
        self,
        backend: Optional[Backend] = None,
        model: str = "grok-2",
        api_key: Optional[str] = None,
        default_persona: str = "default",
        default_iq: int = 100
    ):
        """
        Initialize the Conductor.
        
        Args:
            backend: Custom backend (default: GrokBackend)
            model: Grok model to use (grok-2, grok-2-mini, grok-beta)
            api_key: xAI API key (or set XAI_API_KEY env var)
            default_persona: Default persona name
            default_iq: Default IQ level (35-200)
        """
        self.backend = backend or GrokBackend(model=model, api_key=api_key)
        self.default_persona = default_persona
        self.default_iq = default_iq
        self._custom_personas: Dict[str, Persona] = {}
    
    def register_persona(self, persona: Persona) -> None:
        """Register a custom persona."""
        self._custom_personas[persona.name] = persona
    
    def get_persona(self, name: str) -> Persona:
        """Get persona by name."""
        if name in self._custom_personas:
            return self._custom_personas[name]
        return get_persona(name)
    
    def conduct(
        self,
        prompt: str,
        persona: Optional[str] = None,
        iq: Optional[int] = None,
        temperature: Optional[float] = None,
        max_tokens: int = 1024,
        **kwargs
    ) -> str:
        """
        Generate a response with Grok using the specified persona.
        
        Args:
            prompt: User input
            persona: Persona name (default/savage/ceo/cope/oracle/chaos)
            iq: Intelligence level 35-200
            temperature: Override temperature
            max_tokens: Max response tokens
        
        Returns:
            Grok's response
        """
        persona_name = persona or self.default_persona
        iq_level = iq or self.default_iq
        
        persona_obj = self.get_persona(persona_name)
        system_prompt = persona_obj.format_prompt(iq_level)
        
        if temperature is None:
            base_temp = 0.7
            iq_temp_modifier = (100 - iq_level) / 200
            temperature = persona_obj.get_temperature(base_temp + iq_temp_modifier)
        
        return self.backend.complete(
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
    
    def list_personas(self) -> Dict[str, str]:
        """List all available personas."""
        result = {name: p.description or "" for name, p in PERSONAS.items()}
        result.update({name: p.description or "Custom" for name, p in self._custom_personas.items()})
        return result
