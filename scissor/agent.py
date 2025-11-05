import random
from typing import cast

from google.adk.agents import BaseAgent, LoopAgent, SequentialAgent

from .sub_agents import ecomax_agent, topic_extractor_agent, veritas_agent

# Randomize the debate order
debate_agents = cast(list[BaseAgent], [ecomax_agent, veritas_agent])
random.shuffle(debate_agents)

# Create the debate loop: EcoMax and Veritas in random order
debate_sequence = SequentialAgent(
    name="DebateSequence",
    sub_agents=debate_agents,
)

# Loop the debate sequence 3 times (3 posts each = 6 total)
debate_loop = LoopAgent(
    name="DebateLoop",
    sub_agents=[debate_sequence],
    max_iterations=3,
)

# Main orchestrator: Extract topic, then run the debate
root_agent = SequentialAgent(
    name="ScissorSimulator",
    description="Simulates polarized online debates where agents use strawman arguments and never seek common ground",
    sub_agents=[
        topic_extractor_agent,
        debate_loop,
    ],
)
