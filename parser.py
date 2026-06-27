import re

def get_nginx_error_type(error_msg):
    if "Connection refused" in error_msg: return "connection_refused"
    if "upstream timed out" in error_msg: return "upstream_timeout"
    if "Permission denied" in error_msg: return "permission_denied"
    return "unknown"

def parse_nginx_log(line):
    pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[error\] .*?: (?P<error>.*)'
    match = re.search(pattern, line)
    if match:
        error_msg = match.group('error')
        return {
            "log_type": "nginx",
            "severity": "ERROR",
            "timestamp": match.group('timestamp'),
            "error_type": get_nginx_error_type(error_msg), # Nayi field
            "error": error_msg,
            "raw_line": line.strip()
        }
    return None
def parse_jenkins_log(line):
    # Regex updated to handle logs strictly
    pattern = r'\[(?P<timestamp>.*?)\] (?P<severity>ERROR|FATAL|WARNING): (?P<error>.*)'
    match = re.search(pattern, line)
    if match:
        return {
            "log_type": "jenkins",
            "severity": match.group('severity'),
            "timestamp": match.group('timestamp'),
            "error": match.group('error'),
            "raw_line": line.strip()
        }
    return None

def parse_app_log(line):
    pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<severity>ERROR|WARNING|EXCEPTION) (?P<error>.*)'
    match = re.search(pattern, line)
    if match:
        return {
            "log_type": "app",
            "severity": match.group('severity'),
            "timestamp": match.group('timestamp'), # Correction: Added timestamp field
            "error": match.group('error'),         # Correction: Added error field
            "raw_line": line.strip()
        }
    return None

def parse_log(log_type, file_path):
    parsed_data = []
    with open(file_path, 'r') as file:
        for line in file:
            data = None
            if log_type == 'nginx': data = parse_nginx_log(line)
            elif log_type == 'jenkins': data = parse_jenkins_log(line) # Fixed 'daata' typo
            elif log_type == 'app': data = parse_app_log(line)
            
            if data:
                parsed_data.append(data)
    return parsed_data
