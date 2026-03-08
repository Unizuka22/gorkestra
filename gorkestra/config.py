"""Configuration handling for gorkestra."""

import os
import yaml
from pathlib import Path
from typing import Optional, Dict, Any

DEFAULT_CONFIG = {
    "default_backend": "openai",
    "default_persona": "default",
    "default_iq": 100,
    "backends": {
        "openai": {"model": "gpt-4"},
        "anthropic": {"model": "claude-3-sonnet-20240229"},
        "ollama": {"model": "llama2", "host": "http://localhost:11434"}
    }
}

def find_config_file() -> Optional[Path]:
    """Find config file in standard locations."""
    locations = [
        Path.cwd() / ".gorkestra.yaml",
        Path.cwd() / ".gorkestra.yml",
        Path.home() / ".gorkestra.yaml",
        Path.home() / ".config" / "gorkestra" / "config.yaml",
    ]
    
    env_path = os.getenv("GORKESTRA_CONFIG")
    if env_path:
        locations.insert(0, Path(env_path))
    
    for path in locations:
        if path.exists():
            return path
    return None

def load_config() -> Dict[str, Any]:
    """Load configuration from file or return defaults."""
    config_file = find_config_file()
    
    if config_file:
        with open(config_file) as f:
            user_config = yaml.safe_load(f) or {}
        # Merge with defaults
        config = DEFAULT_CONFIG.copy()
        config.update(user_config)
        return config
    
    return DEFAULT_CONFIG.copy()

def get_backend_config(backend_name: str) -> Dict[str, Any]:
    """Get configuration for a specific backend."""
    config = load_config()
    return config.get("backends", {}).get(backend_name, {})
