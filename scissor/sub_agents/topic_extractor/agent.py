"""Topic Extractor Agent - Silently extracts and stores the debate topic."""

from google.adk.agents import LlmAgent

from .prompt import TOPIC_EXTRACTOR_INSTRUCTION

# Simple LLM agent that extracts the topic and stores it
# Using instruction that returns a minimal acknowledgment
topic_extractor_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="TopicExtractor",
    description="Extracts the debate topic and detects language from user input",
    instruction=TOPIC_EXTRACTOR_INSTRUCTION,
    output_key="topic",  # This will save the user's message to state['topic']
)
