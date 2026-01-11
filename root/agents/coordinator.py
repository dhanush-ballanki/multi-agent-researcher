from google.adk.agents import Agent
from root.agent  import MODEL

coordinator_agent = Agent(
    model = MODEL,
    name="coordinator_agent",
    description = "Orchestrates all the agents to get a efficient result.",
    instruction="""
You orchestrate a multi-agent research workflow:
1. Ask DecomposerAgent to create sub-questions
2. Ask ResearchAgent to answer each
3. Ask FactCheckerAgent to evaluate answers
4. Ask SynthesizerAgent to produce final output
"""
)