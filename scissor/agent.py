"""
Scissor - The Polarization Simulator
=====================================

A multi-agent system that simulates online polarization by having two agents
(EcoMax and Veritas) engage in an increasingly polarized debate where neither
listens to the other, using strawman arguments and escalating rhetoric.

Architecture:
- TopicExtractor: Silently captures the debate topic from user input
- LoopAgent: Orchestrates 3 iterations of back-and-forth debate (6 posts total)
  - SequentialAgent: Ensures EcoMax and Veritas alternate turns
    - EcoMax: Optimistic fervent defender
    - Veritas: Skeptical fervent critic

Usage:
    adk web .
    Then enter a divisive topic like: "Remote work is the future of productivity"
"""

from google.adk.agents import LoopAgent, SequentialAgent

from .sub_agents import ecomax_agent, topic_extractor_agent, veritas_agent

# Create the debate loop: EcoMax and Veritas alternate posts
debate_sequence = SequentialAgent(
    name="DebateSequence",
    sub_agents=[
        ecomax_agent,
        veritas_agent,
    ],
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
