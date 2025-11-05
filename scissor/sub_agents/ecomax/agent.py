"""EcoMax Agent - The Optimistic Fervent Defender."""

from google.adk.agents import LlmAgent
from google.genai import types

from .prompt import ECOMAX_INSTRUCTION


def create_ecomax_agent() -> LlmAgent:
    """Create the EcoMax agent instance."""
    return LlmAgent(
        model="gemini-2.5-flash",
        name="EcoMax",
        description="A passionate defender who sees the topic overwhelmingly positive and attacks critics",
        instruction=ECOMAX_INSTRUCTION,
        output_key="ecomax_post",
        generate_content_config=types.GenerateContentConfig(
            temperature=1.2,
        ),
    )


# Create the singleton instance
ecomax_agent = create_ecomax_agent()
