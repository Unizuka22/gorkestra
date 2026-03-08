"""Web search tool."""

import os
from typing import List, Dict
from .base import Tool

class WebSearch(Tool):
    """Search the web using various providers."""
    
    name = "web_search"
    description = "Search the web for information"
    
    def __init__(self, provider: str = "auto"):
        self.provider = provider
    
    def execute(self, query: str, num_results: int = 5) -> List[Dict]:
        """
        Search the web.
        
        Args:
            query: Search query
            num_results: Number of results
        
        Returns:
            List of {title, url, snippet} dicts
        """
        # Try different providers
        if self.provider == "auto":
            if os.getenv("SERPER_API_KEY"):
                return self._search_serper(query, num_results)
            elif os.getenv("BRAVE_API_KEY"):
                return self._search_brave(query, num_results)
            else:
                return self._search_duckduckgo(query, num_results)
        
        return self._search_duckduckgo(query, num_results)
    
    def _search_duckduckgo(self, query: str, num_results: int) -> List[Dict]:
        """DuckDuckGo search (no API key needed)."""
        try:
            from duckduckgo_search import DDGS
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=num_results))
                return [
                    {"title": r["title"], "url": r["href"], "snippet": r["body"]}
                    for r in results
                ]
        except ImportError:
            return [{"error": "Install duckduckgo-search: pip install duckduckgo-search"}]
    
    def _search_serper(self, query: str, num_results: int) -> List[Dict]:
        """Serper.dev search."""
        import requests
        response = requests.post(
            "https://google.serper.dev/search",
            json={"q": query, "num": num_results},
            headers={"X-API-KEY": os.getenv("SERPER_API_KEY")}
        )
        data = response.json()
        return [
            {"title": r["title"], "url": r["link"], "snippet": r.get("snippet", "")}
            for r in data.get("organic", [])
        ]
    
    def _search_brave(self, query: str, num_results: int) -> List[Dict]:
        """Brave Search API."""
        import requests
        response = requests.get(
            "https://api.search.brave.com/res/v1/web/search",
            params={"q": query, "count": num_results},
            headers={"X-Subscription-Token": os.getenv("BRAVE_API_KEY")}
        )
        data = response.json()
        return [
            {"title": r["title"], "url": r["url"], "snippet": r.get("description", "")}
            for r in data.get("web", {}).get("results", [])
        ]
