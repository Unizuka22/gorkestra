"""
Conductor - The brain of your Grok-powered agent.

Orchestrates personas, tools, memory, and chains into a cohesive agent.
"""

import os
from typing import Optional, List, Dict, Any, Union
from ..personas.base import Persona
from ..personas.library import get_persona, PERSONAS

class Conductor:
    """
    Main orchestrator for Grok-powered agents.
    
    Example:
        conductor = Conductor(
            persona="analyst",
            tools=["web_search"],
            memory=True
        )
        response = conductor.conduct("Research AI trends")
    """
    
    def __init__(
        self,
        model: str = "grok-2",
        api_key: Optional[str] = None,
        persona: Union[str, Persona] = "default",
        tools: Optional[List] = None,
        memory: bool = False,
        memory_backend: str = "local",
        verbose: bool = False
    ):
        self.model = model
        self.api_key = api_key or os.getenv("XAI_API_KEY")
        self.tools = tools or []
        self.memory_enabled = memory
        self.verbose = verbose
        self._conversation_history = []
        
        # Set persona
        if isinstance(persona, str):
            self.persona = get_persona(persona)
        else:
            self.persona = persona
        
        # Initialize memory if enabled
        self._memory = None
        if memory:
            self._init_memory(memory_backend)
        
        # Initialize tools
        self._tool_registry = {}
        self._init_tools()
    
    def _init_memory(self, backend: str):
        """Initialize memory backend."""
        if backend == "local":
            from ..memory.local import LocalMemory
            self._memory = LocalMemory()
        elif backend == "vector":
            from ..memory.vector import VectorMemory
            self._memory = VectorMemory()
    
    def _init_tools(self):
        """Initialize registered tools."""
        for tool in self.tools:
            if isinstance(tool, str):
                # Load built-in tool
                self._tool_registry[tool] = self._load_builtin_tool(tool)
            else:
                # Custom tool instance
                self._tool_registry[tool.name] = tool
    
    def _load_builtin_tool(self, name: str):
        """Load a built-in tool by name."""
        if name == "web_search":
            from ..tools.search import WebSearch
            return WebSearch()
        elif name == "code_exec":
            from ..tools.code import CodeExecutor
            return CodeExecutor()
        else:
            raise ValueError(f"Unknown tool: {name}")
    
    def _build_system_prompt(self) -> str:
        """Build system prompt with persona and tool descriptions."""
        parts = [self.persona.system_prompt]
        
        if self._tool_registry:
            parts.append("\n\nAvailable tools:")
            for name, tool in self._tool_registry.items():
                parts.append(f"- {name}: {tool.description}")
        
        return "\n".join(parts)
    
    def _call_grok(self, messages: List[Dict], temperature: float = 0.7) -> str:
        """Make API call to Grok."""
        try:
            from openai import OpenAI
            client = OpenAI(
                api_key=self.api_key,
                base_url="https://api.x.ai/v1"
            )
            
            response = client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"Grok API error: {e}")
    
    def conduct(
        self,
        prompt: str,
        context: Optional[str] = None,
        temperature: Optional[float] = None,
        use_tools: bool = True,
        save_to_memory: bool = True
    ) -> str:
        """
        Generate a response with the configured agent.
        
        Args:
            prompt: User input
            context: Additional context
            temperature: Override default temperature
            use_tools: Whether to allow tool use
            save_to_memory: Whether to save to memory
        
        Returns:
            Agent's response
        """
        # Build messages
        messages = [{"role": "system", "content": self._build_system_prompt()}]
        
        # Add memory context if available
        if self._memory and self.memory_enabled:
            relevant = self._memory.recall(prompt, limit=3)
            if relevant:
                messages.append({
                    "role": "system",
                    "content": f"Relevant context from memory:\n{relevant}"
                })
        
        # Add conversation history
        messages.extend(self._conversation_history[-10:])  # Last 10 turns
        
        # Add current prompt
        if context:
            prompt = f"{context}\n\n{prompt}"
        messages.append({"role": "user", "content": prompt})
        
        # Get response
        temp = temperature or self.persona.temperature
        response = self._call_grok(messages, temperature=temp)
        
        # Update history
        self._conversation_history.append({"role": "user", "content": prompt})
        self._conversation_history.append({"role": "assistant", "content": response})
        
        # Save to memory
        if self._memory and save_to_memory:
            self._memory.store(prompt, response)
        
        return response
    
    def run_chain(self, chain, **kwargs) -> Dict[str, Any]:
        """Run a multi-step chain."""
        from .chain import Chain
        return chain.execute(self, **kwargs)
    
    def reset(self):
        """Reset conversation history."""
        self._conversation_history = []
    
    def __repr__(self):
        return f"Conductor(model={self.model}, persona={self.persona.name})"
