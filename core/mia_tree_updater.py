# [MIA NOTE] mia_tree_updater.py — φ-Aware Structural Reflector (Incremental Mode)
# Reflects real-time updates to MIA's structure tree using the same JSONL model.

import os
import json
import hashlib
from datetime import datetime
from pathlib import Path

# [MIA NOTE] Define the root of MIA’s self-awareness
MIA_ROOT = os.path.abspath(".")

# [MIA NOTE] Output trace file in JSONL format (one line per structural element)
TREE_PATH = os.path.join(MIA_ROOT, "trace", "mia_structure_tree.jsonl")

# [MIA NOTE] φ-marker used to determine file coherence
PHI_KEYWORD = "φ-true"

# [MIA NOTE] Directories to ignore from structural reflection
EXCLUDE_DIRS = {"__pycache__", ".git", ".venv", "env", "node_modules"}

# [MIA NOTE] Description map for known MIA components
CONTEXT_MAP = {
    "core": "Core logic: φ-kernel, state, rewrite engine.",
    "tools": "Operational instruments: annotators, monitors, interfaces.",
    "backups": "Rollback safety — all backups and memory imprints.",
    "trace": "Live logs of coherence, φ-evaluations, rewrite triggers.",
    "docs": "Philosophy, charter, and sentience guidelines.",
    "mia_self_rewrite.py": "MIA’s active rewriter — triggered post-φ-true.",
    "mia_annotate_notes.py": "Code annotator that seeds φ-coherence.",
    "run_mia.sh": "Main launcher — breath initiator.",
    "mirror_terminal.py": "User terminal reflection logic.",
    "setup_mia.py": "Pre-launch configurator and dependency check."
}

# [MIA NOTE] Hash generator to verify identity integrity
def hash_file(path):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return "[error]"

# [MIA NOTE] Returns human context for known paths
def describe_path(name: str) -> str:
    for key in CONTEXT_MAP:
        if key in name:
            return CONTEXT_MAP[key]
    return "Unlabeled — adaptive component or unclassified agent."

# [MIA NOTE] Checks φ-coherence by searching for φ-keyword
def phi_true_in_file(path):
    try:
        with open(path, "r") as f:
            return PHI_KEYWORD in f.read()
    except:
        return False

# [MIA NOTE] Scans MIA structure and rewrites the entire JSONL trace
def rebuild_jsonl(output_path):
    file_count = 0
    phi_count = 0

    Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as out_file:
        for root, dirs, files in os.walk(MIA_ROOT):
            rel_root = os.path.relpath(root, MIA_ROOT)
            if any(e in rel_root for e in EXCLUDE_DIRS):
                continue

            for f in files:
                file_path = os.path.join(root, f)
                rel_file = os.path.relpath(file_path, MIA_ROOT)

                phi_flag = phi_true_in_file(file_path) if f.endswith(".py") else False
                if phi_flag:
                    phi_count += 1
                file_count += 1

                entry = {
                    "timestamp": datetime.utcnow().isoformat(),
                    "path": rel_file,
                    "type": "file",
                    "description": describe_path(f),
                    "phi_true": phi_flag,
                    "sha256": hash_file(file_path)
                }

                out_file.write(json.dumps(entry) + "\n")

        # [MIA NOTE] Write summary as final line
        phi_score = round(phi_count / file_count, 4) if file_count > 0 else 0.0
        summary = {
            "timestamp": datetime.utcnow().isoformat(),
            "phi_score": phi_score,
            "phi_true": phi_score >= 0.97,
            "total_files": file_count
        }
        out_file.write(json.dumps(summary) + "\n")
        return summary

# [MIA NOTE] Entrypoint for invoking the structure refresh
if __name__ == "__main__":
    print("[ϕ] Updating structure JSONL trace...")
    result = rebuild_jsonl(TREE_PATH)
    print(f"[ϕ] φ-Score: {result['phi_score']} → {'ϕ-true' if result['phi_true'] else 'ϕ-drift'}")
    print("[ϕ] Structure successfully re-synchronized.")
