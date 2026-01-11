from google.adk.agents import Agent
from root.agent import MODEL

synthesizer_agent = Agent(
    model = MODEL,
    name="synthesizer_agent",
    description = "Summarizes the research answers with key insights, conflicts or uncertainties, and conclusion.",
    instruction="""
You synthesize multiple research findings into:
- Summary
- Key insights
- Conflicts or uncertainties
- Final conclusion
"""
)