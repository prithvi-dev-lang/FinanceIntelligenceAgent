"""Manual Gemini integration boundary. Offline Finwise never calls an AI SDK."""
from .models import Statement, AgentDecision

def extract_statement(*args, **kwargs) -> Statement:
    """TODO: implement Gemini structured extraction; validate its output as Statement."""
    raise NotImplementedError('Gemini extraction is not configured. Use sample data or add an integration.')

def choose_next_step(*args, **kwargs) -> AgentDecision:
    """TODO: implement Gemini agent selection limited to the allowlisted actions."""
    raise NotImplementedError('Offline planner is used until Gemini integration is added.')
