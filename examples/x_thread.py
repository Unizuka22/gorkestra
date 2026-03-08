"""Example: Generate and post an X thread."""

from gorkestra import ContentAgent
from gorkestra.tools import XClient

# Generate thread
agent = ContentAgent()
thread = agent.write_thread("Why AI agents will change everything")
print("Generated thread:\n", thread)

# Post to X (uncomment when ready)
# x = XClient()
# tweets = thread.split("\n\n")  # Split by paragraph
# result = x.thread(tweets)
# print("Posted:", result)
