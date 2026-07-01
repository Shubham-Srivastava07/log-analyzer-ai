from collections import Counter

def count_severity(logs):
    return Counter(log['severity'] for log in logs)

def count_services(logs):
    return Counter(log['log_type'] for log in logs)

def top_errors(logs, n=3):
    return Counter(log['error'] for log in logs).most_common(n)

def overall_health(logs):
    severity_counts = count_severity(logs)
    if severity_counts.get('FATAL', 0) > 0:
        return "Critical"
    elif severity_counts.get('ERROR', 0) > 5:
        return "Warning"
    else:
        return "Healthy"

def generate_summary(logs):
    severity = count_severity(logs)
    services = count_services(logs)
    errors = top_errors(logs)
    health = overall_health(logs)

    print("========= LOG SUMMARY =========")
    print(f"Total logs : {len(logs)}\n")

    print("severity")
    print("---------")
    for level, count in severity.items():
        print(f"{level:7} : {count}")

    print("\nServices")
    print("---------")
    for service, count in services.items():
        print(f"{service.capitalize():7} : {count}")

    print("\nTop Errors")
    print("-----------")
    for error, count in errors:
        print(f"{error:18} : {count}")

    print("\nOverall Health")
    print("---------------")
    print(health)
    print("=========================")

