from strands import tool
from datetime import datetime

@tool
def report_writing_agent(summary: str) -> str:
    """
    Generates Markdown-based cybersecurity incident reports.
    """
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    report = f"""# 🛡️ Incident Report

**Date**: {now}  
**Summary**:  
{summary}

---

## 🔍 Investigation

_TBD_

## 🛠 Remediation

_TBD_

## ✅ Status

- [ ] Investigation complete  
- [ ] Remediated  
- [ ] Closed  
"""
    return report
