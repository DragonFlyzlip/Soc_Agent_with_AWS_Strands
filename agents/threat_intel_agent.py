from strands import tool

@tool
def threat_intel_agent(query: str) -> str:
    return f"[Threat Intel] Lookup for: {query}"
