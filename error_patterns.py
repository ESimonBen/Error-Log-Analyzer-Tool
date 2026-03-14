# error_patterns.py
import re

ERROR_PATTERNS = {
    "database timeout":{
        "pattern": r"database.*timeout",
        "severity": "high",
        "recommendation": "Check database availability or connection pool limits"
    },

    "connection refused": {
        "pattern": r"connection refused",
        "severity": "high",
        "recommendation": "Verify the service is running and reachable"
    },

    "file not found": {
        "pattern": r"file not found",
        "severity": "medium",
        "recommendation": "Verify file path or configuration settings"
    },

    "memory_error": {
        "pattern": r"out of memory",
        "severity": "critical",
        "recommendation": "Optimize memory usage"
    },

    "authentication_failed": {
        "pattern": r"authentication failed",
        "severity": "high",
        "recommendation": "Check authentication credentials or identity provider"
    },

    "disk_full": {
        "pattern": r"no space left on device",
        "severity": "critical",
        "recommendation": "Free disk space or expand storage"
    }
}

# Pre-compiling error patterns
COMPILED_ERROR_PATTERNS = {
    error: {
        "regex": re.compile(data["pattern"]),
        "severity": data["severity"],
        "recommendation": data["recommendation"]
    }
    for error, data in ERROR_PATTERNS.items()
}