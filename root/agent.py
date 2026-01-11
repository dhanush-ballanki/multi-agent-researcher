from google.adk.agents import SequentialAgent
from root.agents import decomposer,fact_checker,researcher,synthesizer



orchestrator = SequentialAgent(
    name='Orchestrator',
    description="Uses all sub agents to do an efficient research",
    sub_agents=[decomposer.decomposer_agent,researcher.researcher_agent,fact_checker.fact_checker_agent,synthesizer.synthesizer_agent]
)

root_agent = orchestrator