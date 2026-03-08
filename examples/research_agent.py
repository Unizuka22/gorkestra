"""Example: Research agent that searches and summarizes."""

from gorkestra import ResearchAgent

agent = ResearchAgent()

# Research a topic
result = agent.research("Latest developments in AI agents 2026")
print("Research:\n", result)

# Summarize
summary = agent.summarize(result)
print("\nSummary:\n", summary)
