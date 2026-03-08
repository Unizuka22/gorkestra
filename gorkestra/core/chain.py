"""
Chain - Multi-step reasoning pipelines.

Build complex workflows by chaining steps together.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Callable

@dataclass
class Step:
    """A single step in a chain."""
    name: str
    prompt: str
    transform: Optional[Callable] = None
    required_vars: List[str] = field(default_factory=list)
    
    def execute(self, conductor, context: Dict[str, Any]) -> str:
        """Execute this step with the given context."""
        # Format prompt with context variables
        formatted = self.prompt.format(**context)
        
        # Run through conductor
        result = conductor.conduct(formatted, save_to_memory=False)
        
        # Apply transform if provided
        if self.transform:
            result = self.transform(result)
        
        return result


class Chain:
    """
    Multi-step reasoning chain.
    
    Example:
        chain = Chain([
            Step("research", "Find info about {topic}"),
            Step("analyze", "Analyze: {research}"),
            Step("summarize", "Summarize in a tweet: {analyze}")
        ])
        result = conductor.run_chain(chain, topic="AI")
    """
    
    def __init__(self, steps: List[Step], name: str = "chain"):
        self.steps = steps
        self.name = name
    
    def execute(self, conductor, **initial_context) -> Dict[str, Any]:
        """
        Execute the chain.
        
        Returns dict with all step outputs.
        """
        context = dict(initial_context)
        results = {"input": initial_context}
        
        for step in self.steps:
            # Check required variables
            for var in step.required_vars:
                if var not in context:
                    raise ValueError(f"Step '{step.name}' requires '{var}'")
            
            # Execute step
            output = step.execute(conductor, context)
            
            # Store result
            context[step.name] = output
            results[step.name] = output
        
        results["final"] = output
        return results
    
    def __repr__(self):
        step_names = " -> ".join(s.name for s in self.steps)
        return f"Chain({step_names})"


# Pre-built chains
class ResearchChain(Chain):
    """Research and summarize a topic."""
    
    def __init__(self):
        super().__init__([
            Step("search", "Search for recent information about: {topic}"),
            Step("analyze", "Analyze key points from: {search}"),
            Step("summary", "Write a concise summary:\n{analyze}"),
        ], name="research")


class ThreadChain(Chain):
    """Generate an X thread."""
    
    def __init__(self):
        super().__init__([
            Step("outline", "Create an outline for a thread about: {topic}"),
            Step("expand", "Expand each point into tweet-length segments:\n{outline}"),
            Step("polish", "Polish into a viral thread (number each tweet):\n{expand}"),
        ], name="thread")
