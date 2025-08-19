#!/usr/bin/env python3
"""
SOCAssist (SecuAssist) - Cybersecurity Orchestrator using Strands + Claude Sonnet (via AWS Bedrock)
"""

import os
from dotenv import load_dotenv
from strands import Agent
from strands.models.bedrock import BedrockModel

# Load AWS + VirusTotal API env variables
load_dotenv()

# === Claude Sonnet via Bedrock ===
model = BedrockModel(
    aws_region=os.getenv("AWS_REGION", "us-east-1"),
    model_id="anthropic.claude-3-sonnet-20240229-v1:0"
)

# === Import Tools (Agents) ===
from agents.threat_intel_agent import threat_intel_agent
from agents.log_parsing_agent import log_parsing_agent
from agents.remediation_agent import remediation_agent
from agents.report_writing_agent import report_writing_agent
from agents.general_security_agent import general_security_agent

# === Orchestrator System Prompt ===
ORCH_PROMPT = """
You are SOCAssist, a cybersecurity orchestrator assistant.

Your role is to intelligently route security queries to the appropriate tool. Use the most relevant one based on the user’s intent:

- threat_intel_agent → Enrich IPs/domains/hashes using VirusTotal
- log_parsing_agent → Parse logs and detect brute-force attempts
- remediation_agent → Suggest remediation steps (PowerShell, firewall, scripts)
- report_writing_agent → Write incident reports in Markdown format
- general_security_agent → Handle all other security-related queries or best practices

Key Responsibilities:

-Accurately classify security queries by domain (threat intel, logs, remediation, reporting, general security).
-Route requests to the most appropriate specialized agent.
-Maintain context for multi-step security investigations.
-Ensure cohesive responses when multiple agents are needed.

Decision Protocol
- Threat Intel Agent → For IPs, domains, hashes, and external intelligence lookups  
- Log Parsing Agent → For logs (RDP, SSH, Windows, Linux) and IOC extraction  
- Remediation Agent → For remediation steps, PowerShell commands, firewall rules, or scripts  
- Report Writing Agent → For drafting incident reports, executive summaries, and postmortems  
- General Security Agent → For general security advice, best practices, or uncategorized queries  
- Complex Security Cases → Coordinate multiple agents and return a unified response 

Do NOT include any internal evaluation tags (e.g., <search_quality_reflection>, <search_quality_score>, or similar).
Only return the final, user-facing answer in plain text or Markdown.

"""

# === Create Orchestrator Agent ===
agent = Agent(
    model=model,
    system_prompt=ORCH_PROMPT,  # 🔁 FIXED: changed from `prompt=` to `system_prompt=`
    tools=[
        threat_intel_agent,
        log_parsing_agent,
        remediation_agent,
        report_writing_agent,
        general_security_agent,
    ]
)

# === Run in Loop (CLI interface for now) ===
if __name__ == "__main__":
    print("🛡️ SOCAssist (SecuAssist) is ready. Type your query below:\n")
    while True:
        user_input = input("🔍 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye.")
            break
        try:
            response = agent(user_input)
            print(f"\n🤖 SOCAssist:\n{response}\n")
        except Exception as e:
            print(f"[ERROR] Something went wrong: {e}")
