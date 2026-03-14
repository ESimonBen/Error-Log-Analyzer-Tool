# severity.py
from error_patterns import ERROR_PATTERNS

SEVERITY_RANK = {"low": 1, "medium": 2, "high": 3, "critical": 4}

def compute_overall_severity(error_counter):
    if not error_counter:
        return "low"

    max_rank = 1

    for error_type in error_counter:
        severity_label = ERROR_PATTERNS[error_type]["severity"]
        rank = SEVERITY_RANK.get(severity_label, 1)

        max_rank = max(max_rank, rank)

    for label, rank in SEVERITY_RANK.items():
        if rank == max_rank:
            return label