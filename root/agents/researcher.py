from google.adk.agents import Agent
from google.adk.tools import google_search
from root.config import MODEL

researcher_agent = Agent(
    model = MODEL,
    name = 'researcher_agent',
    description = "Answers a given sub-question with factual information.Cite sources when possible and keep answers concise.",
    instruction = """
        You are a research assistant. 
        Answer a given sub-question with factual information.
        Cite sources when possible and keep answers concise.
""" ,
    tools = [google_search]

)