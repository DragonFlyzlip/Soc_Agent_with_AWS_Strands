from strands import tool

@tool
def general_security_agent(query: str) -> str:
    """
    Handles general security queries and best practices.
    """
    return f"[Security FAQ] Answering: {query}"
