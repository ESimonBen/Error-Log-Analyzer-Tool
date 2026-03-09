# Errors that may appear along with their respective severity
ERROR_PATTERNS = {
    "database_timeout":{
        "pattern": r"database.*timeout",
        "severity": "high",
        "recommendation": "Check database availability or connection pool limits"
    },

    "connection_refused": {
        "pattern": r"connection refused",
        "severity": "high",
        "recommendation": "Verify the service is running and reachable"
    },

    "file_not_found": {
        "pattern": r"file not found",
        "severity": "medium",
        "recommendation": "Verify file path or configuration settings"
    },

    "memory_error": {
        "pattern": r"out of memory",
        "severity": "critical",
        "recommendation": "Optimize memory usage"
    }
}