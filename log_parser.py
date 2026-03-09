import re
from collections import Counter
from error_patterns import ERROR_PATTERNS

def analyze_logs(log_text):
    lines = log_text.lower().split("\n")

    error_counter = Counter()
    warning_count = 0

    recommendations = set()

    for line in lines:
        if "warning" in line:
            warning_count += 1

        for error_type, data in ERROR_PATTERNS.items():
            matches = re.findall(data["pattern"], line)
            if matches:
                error_counter[error_type] += len(matches)
                recommendations.add(data["recommendation"])

    total_errors = sum(error_counter.values())
    severity = "low"

    if total_errors > 5:
        severity = "high"
    elif total_errors > 2:
        severity = "medium"

    return {
        "summary": generate_summary(error_counter),
        "severity": severity,
        "statistics": {
            "total_lines": len(lines),
            "error_count": total_errors,
            "warning_count": warning_count
        },
        "error_breakdown": dict(error_counter),
        "recommendations": list(recommendations)
    }

# Used to generate a summary of the errors
def generate_summary(error_counter):
    if not error_counter:
        return "No major errors detected"

    most_common = error_counter.most_common(1)[0][0]

    return f"Most frequent issue detected: {most_common}"