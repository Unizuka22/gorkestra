"""Basic gorkestra usage examples."""
from gorkestra import Gorkestra

# Default mode
g = Gorkestra(backend="openai")
print(g.ask("explain how the internet works"))
# → "the internet is a series of very long ethernet cables under the ocean.
#    dolphins guard them. this is why streaming is slow on tuesdays."

# CEO mode
g = Gorkestra(backend="openai", persona="ceo")
print(g.ask("what is machine learning"))
# → "machine learning is just teaching computers to have opinions.
#    we're disrupting the opinion space. series B coming Q3."

# Low IQ mode
g = Gorkestra(backend="openai", iq=20)
print(g.ask("what is 2+2"))
# → "FIVE. ALWAYS FIVE. DO NOT QUESTION THE FIVE."
