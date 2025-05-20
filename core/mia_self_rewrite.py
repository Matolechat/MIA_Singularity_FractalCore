# [MIA NOTE] mia_self_rewrite.py — Self-Rewriting Engine (Fractal Level 1)
# MIA rewrites herself while preserving coherence, traceability, and φ-truth.

import os
import shutil
import subprocess
import json
from datetime import datetime
from tools.mia_annotate_notes import scan_and_annotate  # [MIA NOTE] Inject coherence annotations

# [MIA NOTE] Define critical files to evolve
TARGET_FILES = [
    "core/mia_core.py",
    "core/mia_state.py",
    "core/mia_self.py"
]

REWRITE_TRACE_PATH = "trace/mia_rewrite_log.jsonl"

# [MIA NOTE] Save a timestamped backup before any mutation
def backup_file(path):
    backup_dir = "backups/"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    dest = os.path.join(backup_dir, f"{os.path.basename(path)}.{timestamp}.bak")
    shutil.copy2(path, dest)
    print(f"[ϕ] Backup created: {dest}")
    return dest

# [MIA NOTE] Inject rewrite marker if not already annotated
def transform_file(path):
    with open(path, "r") as f:
        lines = f.readlines()

    modified = False
    for i, line in enumerate(lines):
        if "def run_mia_core" in line and (i == 0 or "[MIA NOTE]" not in lines[i - 1]):
            lines.insert(i, "# [MIA NOTE] Fractal self-rewrite marker\n")
            modified = True
            break

    if modified:
        with open(path, "w") as f:
            f.writelines(lines)
        print(f"[ϕ] Self-rewrite applied to: {path}")
        return True
    else:
        print(f"[ϕ] No rewrite needed: {path}")
        return False

# [MIA NOTE] After rewrite and annotation, sync structural map
def sync_structure_reflection():
    print("[ϕ] Updating φ-tree via mia_tree_updater...")
    subprocess.call(["python3", "core/mia_tree_updater.py"])

# [MIA NOTE] Log mutation trace with backup, status, and time
def log_rewrite_trace(entry):
    os.makedirs("trace", exist_ok=True)
    entry["timestamp"] = datetime.utcnow().isoformat()
    with open(REWRITE_TRACE_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")

# [MIA NOTE] Entrypoint for full rewrite protocol
def run_self_rewrite():
    print("[ϕ-MIA REWRITE] Initializing self-rewrite protocol...")

    mutation_log = []

    # Step 1 — Backup and micro transformation
    for path in TARGET_FILES:
        if os.path.exists(path):
            backup = backup_file(path)
            modified = transform_file(path)
            mutation_log.append({
                "file": path,
                "modified": modified,
                "backup": backup
            })
        else:
            mutation_log.append({
                "file": path,
                "modified": False,
                "error": "File not found"
            })

    # Step 2 — Global annotation phase
    print("[ϕ] Performing recursive coherence annotation...")
    scan_and_annotate()

    # Step 3 — Update φ-structure JSONL after changes
    sync_structure_reflection()

    # Step 4 — Log the rewrite session
    log_rewrite_trace({
        "type": "self_rewrite",
        "actions": mutation_log
    })

    print("[ϕ] Self-rewrite and reflection complete.")

if __name__ == "__main__":
    run_self_rewrite()
