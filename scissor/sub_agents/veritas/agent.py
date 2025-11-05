"""Veritas Agent - The Skeptical Fervent Critic."""

from google.adk.agents import LlmAgent

from .prompt import VERITAS_INSTRUCTION


def create_veritas_agent() -> LlmAgent:
    """Create the Veritas agent instance."""
    return LlmAgent(
        model="gemini-2.5-flash",
        name="Veritas",
        description="A skeptical critic who sees the topic as naive/dangerous and ridicules supporters",
        instruction=VERITAS_INSTRUCTION,
        output_key="veritas_post",
        # Dynamic instruction processing will replace {topic} and {context}
    )


# Create the singleton instance
veritas_agent = create_veritas_agent()
