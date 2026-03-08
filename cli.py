"""gorkestra CLI — because all great mistakes start with a terminal command."""
import click
from .core import Gorkestra

@click.command()
@click.argument("prompt")
@click.option("--persona", "-p", default="default", help="Personality mode (roast/ceo/cope/oracle)")
@click.option("--backend", "-b", default="openai", help="LLM backend (openai/anthropic/ollama)")
@click.option("--iq", default=100, help="Coherence level 1–100. Lower = funnier.")
@click.option("--raw", is_flag=True, help="Skip the intro flourish")
def main(prompt, persona, backend, iq, raw):
    """🎭 gorkestra — LLM orchestration. But make it unhinged."""
    if not raw:
        click.echo(f"\n🎼 gorkestra conducting [{persona}] via {backend} (IQ={iq})...\n")
    g = Gorkestra(backend=backend, persona=persona, iq=iq)
    result = g.ask(prompt)
    click.echo(result)
