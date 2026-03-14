import re

# Log Level Detection
LOG_LEVELS = ["info", "debug", "warning", "error", "critical"]

# Log Level Regular Expression
LOG_LEVEL_REGEX = {
    level: re.compile(rf"\b{level}\b")
    for level in LOG_LEVELS
}