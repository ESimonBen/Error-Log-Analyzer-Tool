import re

#Timestamps in the format YYYY-MM-DD HH::MM:SS
TIMESTAMP_REGEX = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")