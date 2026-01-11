from google.adk.agents.llm_agent import Agent

MODEL = 'gemini-3-flash-preview'

root_agent = Agent(
    model= MODEL,
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)