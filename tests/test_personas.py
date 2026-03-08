"""Tests for persona system."""

import pytest
from gorkestra.personas.base import Persona
from gorkestra.personas.builtin import get_persona, PERSONAS

def test_persona_creation():
    p = Persona(name="test", system_prompt="Test prompt")
    assert p.name == "test"
    assert p.system_prompt == "Test prompt"
    assert p.temperature_modifier == 0.0

def test_get_builtin_persona():
    persona = get_persona("roast")
    assert persona.name == "roast"
    assert "roast" in persona.system_prompt.lower() or "brutal" in persona.system_prompt.lower()

def test_invalid_persona():
    with pytest.raises(ValueError):
        get_persona("nonexistent")

def test_iq_formatting():
    persona = Persona(name="test", system_prompt="Base prompt")
    
    low_iq = persona.format_prompt(iq=35)
    assert "confused" in low_iq.lower() or "coherent" in low_iq.lower()
    
    normal_iq = persona.format_prompt(iq=100)
    assert normal_iq == "Base prompt"
    
    high_iq = persona.format_prompt(iq=180)
    assert "intelligent" in high_iq.lower()

def test_temperature_calculation():
    persona = Persona(name="test", system_prompt="", temperature_modifier=0.3)
    assert persona.get_temperature(0.7) == 1.0
    
    # Test bounds
    hot_persona = Persona(name="hot", system_prompt="", temperature_modifier=2.0)
    assert hot_persona.get_temperature(0.7) == 2.0  # Capped at 2.0
