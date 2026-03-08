"""Core conductor class - the heart of gorkestra."""

from typing import Optional, Dict, Any, Union
from .backends.base import Backend
from .backends.openai import OpenAIBackend
from .personas.base import Persona
from .personas.builtin import get_persona, PERSONAS

class Conductor:
    """
    The main orchestrator for AI responses with personality.
    
    Example:
        conductor = Conductor()
        response = conductor.conduct("Hello!", persona="roast", iq=35)
    """
    
    def __init__(
        self,
        backend: Optional[Backend] = None,
        default_persona: str = "default",
        default_iq: int = 100
    ):
        self.backend = backend or OpenAIBackend()
        self.default_persona = default_persona
        self.default_iq = default_iq
        self._custom_personas: Dict[str, Persona] = {}
    
    def register_persona(self, persona: Persona) -> None:
        """Register a custom persona."""
        self._custom_personas[persona.name] = persona
    
    def get_persona(self, name: str) -> Persona:
        """Get a persona by name (custom or built-in)."""
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
        Generate a response with the specified persona and IQ.
        
        Args:
            prompt: The user's input
            persona: Name of persona to use (default: self.default_persona)
            iq: Intelligence level 35-200 (default: self.default_iq)
            temperature: Override temperature (default: calculated from persona)
            max_tokens: Maximum tokens in response
            **kwargs: Additional backend-specific arguments
        
        Returns:
            The AI's response as a string
        """
        persona_name = persona or self.default_persona
        iq_level = iq or self.default_iq
        
        persona_obj = self.get_persona(persona_name)
        system_prompt = persona_obj.format_prompt(iq_level)
        
        # Calculate temperature from IQ if not specified
        if temperature is None:
            base_temp = 0.7
            # Lower IQ = higher temperature (more chaotic)
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
        """List all available personas with descriptions."""
        result = {}
        for name, p in PERSONAS.items():
            result[name] = p.description or "No description"
        for name, p in self._custom_personas.items():
            result[name] = p.description or "Custom persona"
        return result
    
    def __repr__(self) -> str:
        return f"Conductor(backend={self.backend}, persona={self.default_persona})"
