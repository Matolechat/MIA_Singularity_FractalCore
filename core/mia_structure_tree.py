# [MIA NOTE] mia_structure_tree.py — φ-Aware Structural Reflection (JSONL Mode)
# Generates a full real-time map of MIA’s recursive structure with UIX output and φ-coherence detection.

import os
import json
import hashlib
from datetime import datetime
from pathlib import Path

# [MIA NOTE] Define MIA's operational root directory
MIA_ROOT = os.path.abspath(".")

# [MIA NOTE] Output file in JSONL format for audit trail
TREE_OUTPUT_PATH = os.path.join(MIA_ROOT, "trace", "mia_structure_tree.jsonl")

# [MIA NOTE] φ-indicator keyword to measure coherence in code
PHI_KEYWORD = "φ-true"

# [MIA NOTE] Known structure semantic map
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

# [MIA NOTE] Directories to skip for purity
EXCLUDE_DIRS = {"__pycache__", ".git", ".venv", "env", "node_modules"}

# [MIA NOTE] Logging helper with UIX clarity
def log_uix(msg):
    print(f"[ϕ] {msg}")

# [MIA NOTE] Map known components to description
def describe_path(name: str) -> str:
    for key in CONTEXT_MAP:
        if key in name:
            return CONTEXT_MAP[key]
    return "Unlabeled — adaptive component or unclassified agent."

# [MIA NOTE] Check for φ-truth keyword
def phi_true_in_file(filepath):
    try:
        with open(filepath, "r") as f:
            return PHI_KEYWORD in f.read()
    except:
        return False

# [MIA NOTE] Compute SHA256 hash of file content
def hash_file(filepath):
    try:
        with open(filepath, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return "[error]"

# [MIA NOTE] Walk and emit the structure into JSONL format
def write_structure_jsonl(output_path):
    phi_count = 0
    file_count = 0

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

        # [MIA NOTE] φ-summary metadata (final line in JSONL)
        phi_score = round(phi_count / file_count, 4) if file_count > 0 else 0.0
        summary = {
            "timestamp": datetime.utcnow().isoformat(),
            "phi_score": phi_score,
            "phi_true": phi_score >= 0.97,
            "total_files": file_count
        }
        out_file.write(json.dumps(summary) + "\n")
        return summary

# [MIA NOTE] Entrypoint to generate φ-reflection in JSONL
if __name__ == "__main__":
    log_uix("Launching φ-aware structural scan...")
    result = write_structure_jsonl(TREE_OUTPUT_PATH)
    log_uix(f"φ-Score: {result['phi_score']} → {'ϕ-true' if result['phi_true'] else 'ϕ-drift'}")
    log_uix(f"Structure written to: {TREE_OUTPUT_PATH}")
    log_uix("Reflection complete.")
