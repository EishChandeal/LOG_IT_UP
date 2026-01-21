from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class LogEntry:
    timestamp : str
    level : str
    ip : str
    status_code : int
    endpoint : str

new = LogEntry("2025-12-20 21:13:38", "INFO", "192.168.1.1", 201, "GET /home")
print(new)