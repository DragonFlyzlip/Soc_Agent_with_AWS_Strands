from strands import tool

@tool
def log_parsing_agent(log_data: str) -> str:
    """
    Parses logs to detect brute-force attempts by counting failed login attempts from the same IP.
    """
    import re
    ip_counts = {}
    failed_pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")
    
    for match in failed_pattern.finditer(log_data):
        ip = match.group(1)
        ip_counts[ip] = ip_counts.get(ip, 0) + 1

    if not ip_counts:
        return "[Log Parser] No brute force patterns detected."

    result = "[Log Parser] Brute Force Summary:\n"
    for ip, count in sorted(ip_counts.items(), key=lambda x: -x[1]):
        result += f"→ {ip}: {count} failed attempts\n"

    return result
