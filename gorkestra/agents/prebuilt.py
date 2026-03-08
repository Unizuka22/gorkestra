"""Pre-built agents ready to use."""

from .base import Agent
from ..core import Conductor

class ResearchAgent(Agent):
    """Agent specialized in research tasks."""
    
    def __init__(self):
        super().__init__(
            name="researcher",
            conductor=Conductor(
                persona="analyst",
                tools=["web_search"],
                memory=True
            )
        )
    
    def research(self, topic: str) -> str:
        """Research a topic."""
        return self.run(f"Research this topic thoroughly: {topic}")
    
    def summarize(self, text: str) -> str:
        """Summarize content."""
        return self.run(f"Summarize this:\n{text}")


class ContentAgent(Agent):
    """Agent for content creation."""
    
    def __init__(self):
        super().__init__(
            name="content",
            conductor=Conductor(persona="creative")
        )
    
    def write_thread(self, topic: str) -> str:
        """Write an X thread."""
        return self.run(
            f"Write a viral X thread about: {topic}\n"
            "Format as numbered tweets, each under 280 chars."
        )
    
    def write_post(self, topic: str, style: str = "engaging") -> str:
        """Write a single post."""
        return self.run(
            f"Write a {style} X post about: {topic}\n"
            "Keep it under 280 characters."
        )
