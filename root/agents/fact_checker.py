from google.adk.agents import Agent
from root.agent import MODEL

fact_checker_agent = Agent(
    model = MODEL,
    name = 'fact_checker_agent',
    description = "Evaluates research answers. Checks credibility and finds any contradictions ",
    instruction = """
        You evaluate research answers.
        Score credibility from 0–1 and explain briefly.
        Flag any uncertainty or contradictions.
""",
)