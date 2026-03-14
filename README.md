# Log Analyzer Tool

Structured log analysis tool that scans raw application logs, detects common error patterns, and returns a JSON summary including severity, statistics, timestamps, and actionable recommendations. Designed to run as a single-function Rival tool with configurable regex-based patterns for multiple log formats.

---

# Features

- Detects common errors using configurable regex patterns.
- Tracks log levels (INFO, DEBUG, WARNING, ERROR, CRITICAL).
- Counts errors and warnings across the log.
- Extracts timestamps to determine when errors occurred.
- Computes an overall severity level based on detected error types.
- Returns structured JSON output for automation or monitoring systems.
- Easily extensible by adding new patterns in a single configuration file.

---

# Project Structure

```
log_analyzer/
│
├── cortexone_function.py   # Rival entry point (run function)
├── log_parser.py           # Core log analysis logic
├── error_patterns.py       # Regex patterns, severities, recommendations
├── severity.py             # Severity ranking logic
│
├── tests/
│   └── test_input.json     # Sample input payload
│
├── run_test.py             # Local test runner
└── README.md
```

---

# How It Works

1. `cortexone_function.run(input_data)` receives a JSON payload containing a `log_text` field.
2. The text is passed to `analyze_logs()` in `log_parser.py`.
3. The parser processes the log line-by-line and performs the following tasks:

   - Extracts timestamps from each log entry
   - Detects log levels (INFO, WARNING, ERROR, etc.)
   - Applies regex patterns from `error_patterns.py`
   - Counts occurrences of each error type
   - Collects recommended remediation actions
   - Computes an overall severity level using `severity.py`

4. A structured JSON summary is returned.

---

# Input Format

The tool expects a JSON object with a `log_text` field containing raw logs.

Example:

```json
{
  "log_text": "2026-03-10 12:00:01 INFO Server started\n2026-03-10 12:00:03 WARNING Disk usage high\n2026-03-10 12:00:05 ERROR connection refused"
}
```

---

# Output Format

Example output:

```json
{
  "summary": "Most frequent issue detected: connection_refused",
  "severity": "high",
  "statistics": {
    "total_lines": 3,
    "error_count": 1,
    "warning_count": 1
  },
  "log_levels": {
    "info": 1,
    "warning": 1,
    "error": 1
  },
  "error_breakdown": {
    "connection_refused": {
      "count": 1,
      "severity": "high"
    }
  },
  "recommendations": [
    "Verify the service is running and reachable"
  ],
  "first_error_time": "2026-03-10 12:00:05",
  "last_error_time": "2026-03-10 12:00:05"
}
```

---

# Running Locally

### 1. Install Python 3

```
python --version
```

### 2. Clone the repository

```
git clone <repo-url>
cd log_analyzer
```

### 3. (Optional) Create a virtual environment

```
python -m venv venv
source venv/bin/activate
```

### 4. Run the test script

```
python run_test.py
```

This will:

- Load `tests/test_input.json`
- Call the Rival entry function
- Print the JSON output to the console

---

# Extending Error Detection

New error patterns can be added by editing `error_patterns.py`.

Example:

```python
"authentication_failure": {
    "pattern": r"authentication failed",
    "severity": "high",
    "recommendation": "Check credentials or authentication service"
}
```

The parser will automatically detect the new error type without additional code changes.

---

# Example Use Cases

- Application log monitoring
- Infrastructure debugging
- Automated incident triage
- DevOps pipeline log validation
- Security log review

---

# Limitations

- Designed for text-based logs only
- Requires recognizable error patterns to detect issues
- Does not perform full log correlation or anomaly detection

---

# License

MIT License
