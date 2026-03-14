# log_parser.py
import re
from collections import Counter
from error_patterns import ERROR_PATTERNS
from error_patterns import COMPILED_ERROR_PATTERNS
from severity import compute_overall_severity
from utils.timestamp import TIMESTAMP_REGEX
from utils.log_levels import LOG_LEVEL_REGEX

# Converts internal error names into readable text
def format_error_name(name):
    return name.replace("_", " ").title()

# Used to generate a summary of the errors
def generate_summary(error_counter):
    if not error_counter:
        return "No major errors detected"

    most_common, count = error_counter.most_common(1)[0]
    most_common = format_error_name(most_common)

    return f"Most frequent issue detected: {most_common} ({count} occurrences)"

def analyze_logs(log_text):
    lines = log_text.lower().split("\n")

    error_counter = Counter()
    warning_count = 0
    level_counter = Counter()

    recommendations = set()
    first_error_time = None
    last_error_time = None

    for line in lines:
        for level, regex in LOG_LEVEL_REGEX.items():
            if regex.search(line):
                level_counter[level] += 1

        timestamps = TIMESTAMP_REGEX.findall(line)
        if timestamps:
            if first_error_time is None:
                first_error_time = timestamps[0]
            last_error_time = timestamps[-1]

        if "warning" in line:
            warning_count += 1

        for error_type, data in COMPILED_ERROR_PATTERNS.items():
            matches = data["regex"].findall(line)
            if matches:
                error_counter[error_type] += len(matches)
                recommendations.add(data["recommendation"])

    total_errors = sum(error_counter.values())
    severity = compute_overall_severity(error_counter)
    error_rate = total_errors / len(lines) if lines else 0

    return {
        "summary": generate_summary(error_counter),
        "severity": severity,
        "statistics": {
            "total_lines": len(lines),
            "error_count": total_errors,
            "warning_count": warning_count,
            "error_rate": round(error_rate, 4)
        },
        "log_levels": dict(level_counter),
        "error_breakdown": {
            error_type: {
                "count": count,
                "severity": ERROR_PATTERNS[error_type]["severity"]
            }
            for error_type, count in error_counter.items()
        },
        "top_errors": error_counter.most_common(3),
        "recommendations": list(recommendations),
        "timeline": {
            "first_error_time": first_error_time if total_errors > 0 else None,
            "last_error_time": last_error_time if total_errors > 0 else None
        },
        "tool_metadata": {
            "tool": "log_analyzer",
            "version": "1.0"
        }
    }