"""
Log Analyzer Module

Parses application logs to detect known error patterns,
extract timestamps, compute severity levels, and
generate recommendations.
"""

#cortexone_function.py
from log_parser import analyze_logs

def run(input_data):
    if not isinstance(input_data, dict):
        return {"error": "Input must be a JSON object"}

    log_text = input_data.get("log_text")

    if not isinstance(log_text, str):
        return {"error": "log_text must be a string"}

    return analyze_logs(log_text)