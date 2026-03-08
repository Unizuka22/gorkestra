"""Command-line interface for gorkestra."""

import argparse
import sys
from typing import Optional

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gorkestra",
        description="Conduct your AI. It will not listen.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  gorkestra "explain quantum physics"
  gorkestra "write a poem" --persona roast --iq 35
  gorkestra "hello" --backend anthropic
        """
    )
    
    parser.add_argument("prompt", nargs="?", help="The prompt to send")
    parser.add_argument("--persona", "-p", default="default",
                       help="Persona to use (default, roast, ceo, cope, oracle)")
    parser.add_argument("--iq", type=int, default=100,
                       help="IQ level 35-200 (default: 100)")
    parser.add_argument("--backend", "-b", default="openai",
                       help="Backend to use (openai, anthropic, ollama)")
    parser.add_argument("--model", "-m", help="Model to use")
    parser.add_argument("--temperature", "-t", type=float,
                       help="Override temperature")
    parser.add_argument("--max-tokens", type=int, default=1024,
                       help="Maximum tokens in response")
    parser.add_argument("--list-personas", action="store_true",
                       help="List available personas")
    parser.add_argument("--version", "-v", action="store_true",
                       help="Show version")
    
    return parser

def get_backend(name: str, model: Optional[str] = None):
    """Get backend instance by name."""
    if name == "openai":
        from .backends.openai import OpenAIBackend
        return OpenAIBackend(model=model) if model else OpenAIBackend()
    elif name == "anthropic":
        from .backends.anthropic import AnthropicBackend
        return AnthropicBackend(model=model) if model else AnthropicBackend()
    else:
        raise ValueError(f"Unknown backend: {name}")

def main(args: Optional[list] = None) -> int:
    parser = create_parser()
    opts = parser.parse_args(args)
    
    if opts.version:
        from . import __version__
        print(f"gorkestra v{__version__}")
        return 0
    
    if opts.list_personas:
        from .core import Conductor
        conductor = Conductor()
        print("\nAvailable personas:\n")
        for name, desc in conductor.list_personas().items():
            print(f"  {name:12} - {desc}")
        print()
        return 0
    
    if not opts.prompt:
        parser.print_help()
        return 1
    
    # Conduct!
    from .core import Conductor
    
    print(f"\n🎼 conducting [{opts.persona}] via {opts.backend} (IQ={opts.iq})...\n")
    
    try:
        backend = get_backend(opts.backend, opts.model)
        conductor = Conductor(backend=backend)
        
        response = conductor.conduct(
            prompt=opts.prompt,
            persona=opts.persona,
            iq=opts.iq,
            temperature=opts.temperature,
            max_tokens=opts.max_tokens
        )
        
        print(response)
        print()
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
