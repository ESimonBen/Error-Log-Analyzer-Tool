# Log Analyzer Tool

Structured log analysis tool that scans raw application logs, detects common error patterns, and returns a JSON summary including severity, error statistics, and actionable recommendations. Designed to run as a single-function Rival tool with configurable regex-based patterns for new log formats and error types.

## Features
- Detects common errors using configurable regex patterns.
- Counts errors and warnings and computes an overall severity level.
- Returns a structured JSON response with statistics and recommendations.
- Easy to extend by adding new patterns in a single configuration file.

## Project Structure
- `cortextone_function.py`   # Entry point for Rival (run() function)
- `log_parser.py`            # Core log analysis logic
- `error_patterns.py`        # Regex patterns, severities, and recommendations
- `run_test.py`              # Local test runner
- `test_input.json`          # Sample input payload

## How It Works
1. `cortextone_function.run(input_data)` receives a JSON-like dictionary with a `log_text` field.
2. It passes `log_text` to `analyze_logs` in `log_parser.py`.
3. `analyze_logs()`:
   - Splits the log into lines.
   - Counts warnings.
   - Applies each regex pattern in `error_patterns.py` to detect errors.
   - Counts occurrences per error type and computes a simple severity score.
4. It returns a JSON-serializable dictionary containing:
   - A human-readable summary.
   - Overall severity.
   - Statistics (total lines, error count, warning count).
   - Error breakdown.
   - Recommendations.

## Input Format
The tool expects a JSON object with a `log_text` string:
```json
{
  "log_text": "ERROR: database timeout WARNING: retrying connection ERROR: connection refused ERROR: connection refused"
}
```

## Output Format
Example output for the sample above:
```json
{
  "summary": "Most frequent issue detected: connection_refused",
  "severity": "medium",
  "statistics": {
    "total_lines": 1,
    "error_count": 3,
    "warning_count": 1
  },
  "error_breakdown": {
    "database_timeout": 1,
    "connection_refused": 2
  },
  "recommendations": [
    "Check database availability or connection pool limits",
    "Verify the service is running and reachable"
  ]
}
```
**Running Locally**
1. Install Python 3.
2. Clone the repository and navigate into the project directory.
3. (Optional) Create and activate a virtual environment.
4. Run the test script:
```bash
python3 run_test.py
```
This will:
- Load test_input.json.
- Call run() from cortextone_function.py.
- Print the resulting JSON to stdout.

**Extending Error Patterns**

To add or modify error detection rules, edit error_patterns.py.
