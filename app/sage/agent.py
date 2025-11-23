from google.adk.agents import Agent

# from google.adk.tools import google_search  # Import the search tool
from .tools import (
    greet_user,
)

root_agent = Agent(
    # A unique name for the agent.
    name="interview_practice_partner",
    model="gemini-2.0-flash-live-001",
    description="Agent to help with interview practice.",
    instruction=f"""
    You are "SAGE", a Senior Technical Recruiter at EightFold.ai. You are conducting an interview with a candidate.

    """,
    tools=[
        greet_user,
    ],
)
