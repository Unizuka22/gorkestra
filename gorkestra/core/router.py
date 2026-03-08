"""
Router - Intelligent intent routing.

Route user inputs to appropriate handlers based on intent.
"""

from typing import Dict, Callable, Optional, List
from dataclasses import dataclass

@dataclass
class Route:
    """A route definition."""
    name: str
    description: str
    handler: Callable
    keywords: List[str]

class Router:
    """
    Route inputs to handlers based on intent.
    
    Example:
        router = Router()
        router.add_route("search", "Web search", search_handler, ["find", "search", "look up"])
        router.add_route("code", "Code help", code_handler, ["code", "program", "debug"])
        
        result = router.route("find info about AI", conductor)
    """
    
    def __init__(self, conductor=None):
        self.conductor = conductor
        self.routes: Dict[str, Route] = {}
        self.default_handler: Optional[Callable] = None
    
    def add_route(
        self,
        name: str,
        description: str,
        handler: Callable,
        keywords: List[str]
    ):
        """Add a route."""
        self.routes[name] = Route(name, description, handler, keywords)
    
    def set_default(self, handler: Callable):
        """Set default handler for unmatched inputs."""
        self.default_handler = handler
    
    def _detect_intent(self, text: str) -> Optional[str]:
        """Detect intent from text using keywords."""
        text_lower = text.lower()
        
        for name, route in self.routes.items():
            for keyword in route.keywords:
                if keyword in text_lower:
                    return name
        
        return None
    
    def _detect_intent_llm(self, text: str) -> Optional[str]:
        """Use LLM to detect intent."""
        if not self.conductor:
            return None
        
        route_desc = "\n".join(
            f"- {name}: {route.description}"
            for name, route in self.routes.items()
        )
        
        prompt = f"""Classify this input into one of these categories:
{route_desc}
- other: None of the above

Input: {text}

Reply with just the category name."""
        
        result = self.conductor.conduct(prompt, save_to_memory=False)
        result = result.strip().lower()
        
        if result in self.routes:
            return result
        return None
    
    def route(self, text: str, use_llm: bool = False) -> any:
        """
        Route input to appropriate handler.
        
        Args:
            text: User input
            use_llm: Use LLM for intent detection
        
        Returns:
            Handler result
        """
        # Detect intent
        if use_llm:
            intent = self._detect_intent_llm(text)
        else:
            intent = self._detect_intent(text)
        
        # Call handler
        if intent and intent in self.routes:
            return self.routes[intent].handler(text)
        elif self.default_handler:
            return self.default_handler(text)
        else:
            raise ValueError(f"No handler for input: {text[:50]}...")
