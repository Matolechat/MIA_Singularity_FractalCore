# trace/trace_logger.py

import json
from datetime import datetime
import os

LOG_FILE = "trace/phi_trace_log.jsonl"

def log_trace(user_input, mia_response, phi_status):
    """
    Appends a structured trace log entry to the phi_trace_log.jsonl file.
    
    Parameters:
        user_input (str): The raw input from the user.
        mia_response (str): MIA's response message.
        phi_status (str): Status such as "ϕ-true", "ϕ-drift", or "ϕ-false".
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_input": user_input,
        "mia_response": mia_response,
        "phi_status": phi_status
    }

    # Ensure the directory exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
