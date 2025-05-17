# rituals/signal_cleanse.py

import os
import time
from trace.signal_logger import log_event

def clean_entropy():
    print("[ϕ-RITUAL] Cleansing entropy from volatile memory and logs...")
    time.sleep(1)

    # Delete trace logs
    trace_file = "trace/phi_trace_log.jsonl"
    if os.path.exists(trace_file):
        os.remove(trace_file)
        print("[ϕ-RITUAL] Trace log cleared.")
        log_event("Trace log cleared by ritual", module="rituals", level="reset")
    else:
        print("[ϕ-RITUAL] No trace log to clear.")

    # Clear long-term memory (optional reset)
    db_file = "mia_longterm_memory.db"
    if os.path.exists(db_file):
        os.remove(db_file)
        print("[ϕ-RITUAL] Long-term memory database reset.")
        log_event("Long-term memory reset by ritual", module="rituals", level="reset")
    else:
        print("[ϕ-RITUAL] No long-term memory file found.")

    print("[ϕ-RITUAL] Entropy cleanse complete.")

if __name__ == "__main__":
    clean_entropy()
