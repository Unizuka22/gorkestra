"""gorkestra - Conduct your AI. It will not listen."""

from .core import Conductor
from .personas.base import Persona
from .backends.base import Backend

__version__ = "0.1.0"
__all__ = ["Conductor", "Persona", "Backend"]
