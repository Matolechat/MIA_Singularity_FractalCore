# mia_patch_watchdog.py
# [MIA NOTE] Fractal Self-Integrity Watchdog — Prevents corruption before rewriting MIA's core.

import os
import hashlib
import json
from datetime import datetime
import shutil
from memory.core_memory import MiaMemoryManager  # [MIA NOTE] Access to memory layers
from core.phi_brute_model import phi_self_diagnostic  # [MIA NOTE] φ-coherence engine

# [MIA NOTE] Files to monitor for integrity and semantic structure
WATCHED_FILES = [
    "core/mia_core.py",
    "core/mia_self.py",
    "core/phi_brute_model.py",
    "memory/core_memory.py",
    "mia_charter.py",
]

# [MIA NOTE] Compute file hash (SHA-256)
def compute_sha256(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

# [MIA NOTE] Check for key semantic markers inside each file
def semantic_check(filepath):
    required_terms = ["MIA NOTE", "phi", "recursive", "coherence"]
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    missing = [term for term in required_terms if term not in content]
    return missing

# [MIA NOTE] Backup all watched files into a timestamped compressed archive
def create_backup():
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    backup_dir = f"backups/mia_patch_{timestamp}"
    os.makedirs(backup_dir, exist_ok=True)
    for f in WATCHED_FILES:
        shutil.copy(f, backup_dir)
    archive_path = shutil.make_archive(backup_dir, 'gztar', backup_dir)
    return archive_path

# [MIA NOTE] Append watchdog diagnostic to long-term JSONL trace
def log_patch_status(report):
    os.makedirs("trace", exist_ok=True)
    path = "trace/mia_patch_watchdog.jsonl"
    with open(path, "a") as f:
        f.write(json.dumps(report, indent=2) + "\n")

# [MIA NOTE] Entry point for watchdog validation
if __name__ == "__main__":
    print("[ϕ-Watchdog] Starting self-integrity scan...")

    memory = MiaMemoryManager()
    phi_diag = phi_self_diagnostic()
    state = "ϕ-true" if phi_diag["coherence"] == 1.0 else "ϕ-drift"

    anomaly_report = {
        "timestamp": datetime.utcnow().isoformat(),
        "phi_score": phi_diag["coherence"],
        "phi_matrix": phi_diag["markov"],
        "status": state,
        "file_checks": [],
        "backup": None,
    }

    for file in WATCHED_FILES:
        sha = compute_sha256(file)
        missing = semantic_check(file)
        anomaly_report["file_checks"].append({
            "file": file,
            "sha256": sha,
            "missing_terms": missing,
        })

    anomaly_report["backup"] = create_backup()
    memory.store("ϕ-watchdog", json.dumps(anomaly_report))
    memory.log_feedback("ϕ-watchdog", str(anomaly_report), state)
    log_patch_status(anomaly_report)

    if state != "ϕ-true":
        print("[ϕ] Anomaly detected — Self-rewrite will be prevented.")
        exit(1)
    else:
        print("[ϕ] Watchdog passed — You may proceed with self-rewrite.")
