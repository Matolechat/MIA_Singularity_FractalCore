# trace/signal_logger.py

import json
from datetime import datetime
import os

TRACE_FILE = "trace/phi_trace_log.jsonl"

def log_event(event: str, module: str = "unknown", level: str = "info"):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event,
        "module": module,
        "level": level
    }
    os.makedirs("trace", exist_ok=True)
    with open(TRACE_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

def replay_recent(limit=5):
    if not os.path.exists(TRACE_FILE):
        return []
    with open(TRACE_FILE, "r") as f:
        lines = f.readlines()[-limit:]
        return [json.loads(line) for line in lines]

if __name__ == "__main__":
    log_event("Trace system initialized", module="signal_logger", level="init")
    print("[MIA-TRACE] Last signals:")
    for e in replay_recent():
        print(f" - [{e['level']}] ({e['timestamp']}) {e['module']}: {e['event']}")
