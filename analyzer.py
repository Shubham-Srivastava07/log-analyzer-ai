ERROR_MAPPING = {
        "connection_refused": {
            "root_cause": "The backend service is down or not listening.",
            "solution": "Verify if the service is active (systemctl status) and check network connectivity."
            },
        "upstream_timeout": {
            "root_cause": "The request took too long, likely due to heavy load or network delay.",
            "solution": "Check service latency or increase the upstream timeout in config."
            },
        "permission_denied": {
            "root_cause": "Application lacks sufficient file system permissions.",
            "solution": "Execute 'chmod' pr 'chown' to fix folder ownership."
            }
        }

def analyze_log(log_entry):
    """
    log entry mein 'analysis' field add karta hai.
    """
    error_type = log_entry.get("error_type", "unknown")

    analysis = ERROR_MAPPING.get("error_type", {
        "root_cause": "Unkown issue detected.",
        "solution": "Check logs manually or escalate to admin."
        })
    log_entry["analysis"] = analysis
    return log_entry

