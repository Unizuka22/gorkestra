"""Basic usage examples for gorkestra."""

from gorkestra import Conductor

# Create a conductor with default settings
conductor = Conductor()

# Simple query
print("=== Default Persona ===")
response = conductor.conduct("What is Python?")
print(response)

# With roast persona
print("\n=== Roast Persona ===")
response = conductor.conduct(
    "I wrote my first Hello World program today!",
    persona="roast"
)
print(response)

# With low IQ
print("\n=== Oracle + Low IQ ===")
response = conductor.conduct(
    "Should I learn JavaScript?",
    persona="oracle",
    iq=35
)
print(response)

# CEO speak
print("\n=== CEO Persona ===")
response = conductor.conduct(
    "How should I structure my startup?",
    persona="ceo",
    iq=150
)
print(response)
