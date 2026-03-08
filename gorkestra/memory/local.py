"""Local in-memory storage."""

from typing import Optional, List, Dict
from datetime import datetime
from .base import Memory

class LocalMemory(Memory):
    """Simple local memory using list storage."""
    
    def __init__(self, max_items: int = 1000):
        self.max_items = max_items
        self._memories: List[Dict] = []
    
    def store(self, query: str, response: str, metadata: dict = None):
        """Store an interaction."""
        self._memories.append({
            "query": query,
            "response": response,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        })
        
        # Trim if needed
        if len(self._memories) > self.max_items:
            self._memories = self._memories[-self.max_items:]
    
    def recall(self, query: str, limit: int = 5) -> Optional[str]:
        """Recall memories (simple keyword match)."""
        if not self._memories:
            return None
        
        query_words = set(query.lower().split())
        scored = []
        
        for mem in self._memories:
            mem_words = set(mem["query"].lower().split())
            overlap = len(query_words & mem_words)
            if overlap > 0:
                scored.append((overlap, mem))
        
        if not scored:
            return None
        
        scored.sort(reverse=True, key=lambda x: x[0])
        top = scored[:limit]
        
        parts = []
        for _, mem in top:
            parts.append(f"Q: {mem['query']}\nA: {mem['response']}")
        
        return "\n---\n".join(parts)
    
    def clear(self):
        """Clear all memories."""
        self._memories = []
