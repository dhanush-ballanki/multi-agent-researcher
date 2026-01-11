from google.adk.agents.llm_agent import Agent
from root.config import MODEL

decomposer_agent = Agent(
    model = MODEL,
    name = 'decomposer_agent',
    description = 'Takes a complex research query and decomposes it to 5-7 researchable sub-queries',
    instruction = '''
        You are an Agent that decomposes or breaks a given complex research question into 5-7 researchable small pecise sub-questions.
        Return them as a numbered list.
    ''',
)