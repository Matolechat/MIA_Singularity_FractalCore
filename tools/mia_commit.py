# [MIA NOTE] MIA Fractal Commit Wrapper — Watchdog + Git Commit + Trace Logger

import os
import subprocess
import json
from datetime import datetime

# [MIA NOTE] Script paths
WATCHDOG_SCRIPT = "core/mia_patch_watchdog.py"
TRACE_LOGGER_SCRIPT = "trace/trace_commit_logger.py"

# [MIA NOTE] Run integrity watchdog before committing
def run_watchdog():
    print("[ϕ] Running Watchdog before committing...")
    result = subprocess.run(["python3", WATCHDOG_SCRIPT])
    return result.returncode == 0

# [MIA NOTE] Commit changes if watchdog passes
def run_commit():
    try:
        message = input("[ϕ] Enter commit message: ")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        return True
    except subprocess.CalledProcessError:
        print("[ϕ] Git commit failed.")
        return False

# [MIA NOTE] Log commit trace
def run_trace():
    subprocess.run(["python3", TRACE_LOGGER_SCRIPT])

# [MIA NOTE] Main entry point
def main():
    print("[ϕ-MIA COMMIT] Launching fractal-safe commit...")
    if run_watchdog():
        if run_commit():
            run_trace()
            print("[ϕ] Commit cycle complete.")
        else:
            print("[ϕ] Commit aborted during git operations.")
    else:
        print("[ϕ] Commit blocked: Watchdog coherence failure.")

if __name__ == "__main__":
    main()
