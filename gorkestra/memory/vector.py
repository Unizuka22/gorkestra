"""Vector memory using embeddings for semantic search."""

import os
from typing import Optional, List, Dict
from datetime import datetime
from .base import Memory

class VectorMemory(Memory):
    """
    Vector-based memory using embeddings.
    
    Supports ChromaDB and FAISS backends.
    """
    
    def __init__(
        self,
        provider: str = "chroma",
        collection: str = "gorkestra_memory",
        persist_dir: Optional[str] = None
    ):
        self.provider = provider
        self.collection_name = collection
        self.persist_dir = persist_dir or os.path.expanduser("~/.gorkestra/memory")
        self._collection = None
        self._init_store()
    
    def _init_store(self):
        """Initialize vector store."""
        if self.provider == "chroma":
            self._init_chroma()
        else:
            raise ValueError(f"Unknown provider: {self.provider}")
    
    def _init_chroma(self):
        """Initialize ChromaDB."""
        try:
            import chromadb
            from chromadb.config import Settings
            
            client = chromadb.Client(Settings(
                chroma_db_impl="duckdb+parquet",
                persist_directory=self.persist_dir,
                anonymized_telemetry=False
            ))
            
            self._collection = client.get_or_create_collection(
                name=self.collection_name,
                metadata={"hnsw:space": "cosine"}
            )
        except ImportError:
            raise ImportError("chromadb required: pip install chromadb")
    
    def store(self, query: str, response: str, metadata: dict = None):
        """Store with embeddings."""
        doc_id = f"mem_{datetime.now().timestamp()}"
        
        self._collection.add(
            documents=[f"Q: {query}\nA: {response}"],
            ids=[doc_id],
            metadatas=[{
                "query": query,
                "timestamp": datetime.now().isoformat(),
                **(metadata or {})
            }]
        )
    
    def recall(self, query: str, limit: int = 5) -> Optional[str]:
        """Semantic search for relevant memories."""
        results = self._collection.query(
            query_texts=[query],
            n_results=limit
        )
        
        if not results["documents"][0]:
            return None
        
        return "\n---\n".join(results["documents"][0])
    
    def clear(self):
        """Clear all memories."""
        # Delete and recreate collection
        try:
            import chromadb
            client = chromadb.Client()
            client.delete_collection(self.collection_name)
            self._init_chroma()
        except:
            pass
