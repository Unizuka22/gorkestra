"""
gorkestra - Orchestrate Grok with personality.

A Python SDK for xAI's Grok with configurable personas and IQ levels.
"""

from .core import Conductor
from .personas.base import Persona
from .backends.grok import GrokBackend

__version__ = "0.1.0"
__all__ = ["Conductor", "Persona", "GrokBackend"]
