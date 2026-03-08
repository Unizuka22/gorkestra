"""Base agent class."""

from typing import Optional, List
from ..core import Conductor

class Agent:
    """
    Higher-level agent abstraction.
    
    Agents are conductors with pre-configured tools, personas, and behaviors.
    """
    
    def __init__(
        self,
        name: str,
        conductor: Optional[Conductor] = None,
        **conductor_kwargs
    ):
        self.name = name
        self.conductor = conductor or Conductor(**conductor_kwargs)
    
    def run(self, task: str, **kwargs):
        """Run the agent on a task."""
        return self.conductor.conduct(task, **kwargs)
    
    def __repr__(self):
        return f"Agent({self.name})"
