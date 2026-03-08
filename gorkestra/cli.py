"""Command-line interface for gorkestra."""

import argparse
import sys
import os

def create_parser():
    parser = argparse.ArgumentParser(
        prog="gorkestra",
        description="LLM orchestration framework powered by Grok"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Ask command
    ask = subparsers.add_parser("ask", help="Ask a question")
    ask.add_argument("prompt", help="Your question")
    ask.add_argument("--persona", "-p", default="default")
    ask.add_argument("--model", "-m", default="grok-2")
    ask.add_argument("--file", "-f", help="Include file content")
    
    # Chat command
    chat = subparsers.add_parser("chat", help="Interactive chat")
    chat.add_argument("--persona", "-p", default="default")
    chat.add_argument("--memory", action="store_true")
    
    # Chain command
    chain = subparsers.add_parser("chain", help="Run a chain")
    chain.add_argument("name", choices=["research", "thread"])
    chain.add_argument("--topic", "-t", required=True)
    
    # Personas command
    subparsers.add_parser("personas", help="List personas")
    
    # Version
    parser.add_argument("--version", "-v", action="store_true")
    
    return parser

def cmd_ask(args):
    from .core import Conductor
    
    conductor = Conductor(persona=args.persona, model=args.model)
    
    prompt = args.prompt
    if args.file:
        with open(args.file) as f:
            prompt = f"{prompt}\n\nFile content:\n{f.read()}"
    
    print(f"\n[{args.persona}] thinking...\n")
    response = conductor.conduct(prompt)
    print(response)

def cmd_chat(args):
    from .core import Conductor
    
    conductor = Conductor(
        persona=args.persona,
        memory=args.memory
    )
    
    print(f"\ngorkestra chat ({args.persona})")
    print("Type 'quit' to exit\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["quit", "exit", "q"]:
                break
            if not user_input:
                continue
            
            response = conductor.conduct(user_input)
            print(f"\nGrok: {response}\n")
        except KeyboardInterrupt:
            break
    
    print("\nBye!")

def cmd_chain(args):
    from .core import Conductor
    from .core.chain import ResearchChain, ThreadChain
    
    conductor = Conductor(persona="analyst")
    
    chains = {
        "research": ResearchChain(),
        "thread": ThreadChain()
    }
    
    chain = chains[args.name]
    print(f"\nRunning {args.name} chain on: {args.topic}\n")
    
    result = conductor.run_chain(chain, topic=args.topic)
    print(result["final"])

def cmd_personas(args):
    from .personas import PERSONAS
    
    print("\nAvailable personas:\n")
    for name, persona in PERSONAS.items():
        traits = ", ".join(persona.traits) if persona.traits else ""
        print(f"  {name:12} - {traits}")
    print()

def main(argv=None):
    parser = create_parser()
    args = parser.parse_args(argv)
    
    if args.version:
        from . import __version__
        print(f"gorkestra v{__version__}")
        return 0
    
    if args.command == "ask":
        cmd_ask(args)
    elif args.command == "chat":
        cmd_chat(args)
    elif args.command == "chain":
        cmd_chain(args)
    elif args.command == "personas":
        cmd_personas(args)
    else:
        parser.print_help()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
