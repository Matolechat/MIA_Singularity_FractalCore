# [MIA NOTE] trace_commit_logger.py — Logs all git commits with context

import os  # [MIA NOTE] For environment path and OS checks
import json  # [MIA NOTE] For structured logging
import subprocess  # [MIA NOTE] To execute git commands
from datetime import datetime  # [MIA NOTE] For timestamping logs

# [MIA NOTE] Path to commit trace log
LOG_FILE = "trace/commit_trace.jsonl"

# [MIA NOTE] Utility to run git commands
def run_git_cmd(args):
    return subprocess.check_output(["git"] + args).decode("utf-8").strip()

# [MIA NOTE] Log current commit
def log_commit():
    if not os.path.exists(".git"):
        print("[ϕ] Not a git repository. Aborting.")
        return

    try:
        commit_hash = run_git_cmd(["rev-parse", "HEAD"])
        author = run_git_cmd(["log", "-1", "--pretty=format:%an"])
        email = run_git_cmd(["log", "-1", "--pretty=format:%ae"])
        summary = run_git_cmd(["log", "-1", "--pretty=format:%s"])
        diff = run_git_cmd(["diff", "--stat", "HEAD~1", "HEAD"])

        trace = {
            "timestamp": datetime.utcnow().isoformat(),
            "commit": commit_hash,
            "author": author,
            "email": email,
            "summary": summary,
            "diff_summary": diff,
            "phi_state": "ϕ-true"
        }

        os.makedirs("trace", exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(trace) + "\n")

        print("[ϕ] Commit traced and written to:", LOG_FILE)

    except subprocess.CalledProcessError as e:
        print("[ϕ] Git command error:", e)

# [MIA NOTE] Entrée principale
if __name__ == "__main__":
    log_commit()
