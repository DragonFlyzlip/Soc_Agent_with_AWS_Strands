# Soc Assist: Cybersecurity Multi-Agent Assistant

**Soc Assist** is a modular, multi-agent cybersecurity assistant powered by Claude 3 Sonnet via Amazon Bedrock and built with the [Strands framework](https://github.com/strands-project/strands).  
It automates and accelerates Security Operations Center (SOC) workflows like IOC enrichment, log parsing, incident report generation, and mitigation scripting — all via a natural language CLI.

---

## Purpose

SOC analysts often face alert fatigue, redundant tasks, and disconnected tooling.  
SecuAssist automates these workflows by routing prompts to purpose-built agents capable of:

- Enriching IOCs (IPs, domains, hashes)
- Parsing logs for failed login attempts
- Suggesting firewall rules and scripts
- Drafting complete incident reports
- Providing security best practices

---

## Features

- Modular multi-agent architecture
- Claude 3 Sonnet (LLM) via Amazon Bedrock
- IOC enrichment with VirusTotal and Shodan
- Parsing of RDP, SSH, and authentication logs
- Script generation (PowerShell, Python) for blocking attackers
- Human-readable report templates
- General cybersecurity guidance
