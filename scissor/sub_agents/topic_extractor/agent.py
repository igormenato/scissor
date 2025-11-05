"""Topic Extractor Agent - Silently extracts and stores the debate topic."""

from google.adk.agents import LlmAgent

# Simple LLM agent that extracts the topic and stores it
# Using instruction that returns a minimal acknowledgment
topic_extractor_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="TopicExtractor",
    description="Extracts the debate topic and detects language from user input",
    instruction="""You are a topic extractor that detects language.

The user will provide a divisive topic for debate in ANY language.

Your job:
1. Detect the language (English, Portuguese, Spanish, etc.)
2. Acknowledge you received it in the SAME language as the user

Examples:
User: "Is AI dangerous?" → You: "Debate topic set. Participants are joining..."
User: "O livre-arbítrio existe?" → You: "Tópico de debate definido. Os participantes estão entrando..."
User: "¿La IA es peligrosa?" → You: "Tema de debate establecido. Los participantes se están uniendo..."

CRITICAL: Always respond in the SAME language as the user's input.
Keep your response under 15 words.
The debate will be handled by other agents in the detected language.""",
    output_key="topic",  # This will save the user's message to state['topic']
)
