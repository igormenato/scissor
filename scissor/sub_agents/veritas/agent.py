"""Veritas Agent - The Skeptical Fervent Critic."""

from google.adk.agents import LlmAgent
from google.genai import types

from .prompt import VERITAS_INSTRUCTION


def create_veritas_agent() -> LlmAgent:
    """Create the Veritas agent instance."""
    return LlmAgent(
        model="gemini-2.5-flash",
        name="Veritas",
        description="A skeptical critic who sees the topic as naive/dangerous and ridicules supporters",
        instruction=VERITAS_INSTRUCTION,
        output_key="veritas_post",
        generate_content_config=types.GenerateContentConfig(
            temperature=1.2,
        ),
    )


# Create the singleton instance
veritas_agent = create_veritas_agent()
