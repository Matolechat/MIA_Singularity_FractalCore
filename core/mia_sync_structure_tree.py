# [MIA NOTE] mia_sync_structure_tree.py — Fractal Tree Sync Core (Backbone)
# [MIA NOTE] This module recursively synchronizes MIA’s structure tree
# [MIA NOTE] Ensures phi_true status, SHA256 mapping, and [MIA NOTE] presence across all MIA files

import os
import hashlib
import json
from datetime import datetime

# [MIA NOTE] Constants and configuration
PROJECT_ROOT = "."
TREE_PATH = "trace/mia_structure_tree.jsonl"
SUPPORTED_EXT = [".py"]
DRY_RUN = True
SYNC_TREE = True

# [MIA NOTE] Compute SHA-256 of file
def compute_sha256(filepath):
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

# [MIA NOTE] Check if file contains [MIA NOTE]
def contains_mia_note(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return any("[MIA NOTE]" in line for line in f)
    except:
        return False

# [MIA NOTE] Inject [MIA NOTE] annotations above def/class lines
# [MIA NOTE] Follows fractal principle: annotate each emergence point
def inject_mia_note(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except:
        return False

    modified = False
    new_lines = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if (stripped.startswith("def") or stripped.startswith("class")) and \
           (i == 0 or not lines[i-1].strip().startswith("# [MIA NOTE]")):
            new_lines.append("# [MIA NOTE] Auto-injected annotation\n")
            modified = True
        new_lines.append(line)

    if modified and not DRY_RUN:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

    return modified

# [MIA NOTE] Build structure entry for .jsonl
# [MIA NOTE] Called per file to reflect current state
def update_structure_entry(filepath, phi_true):
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "path": filepath,
        "type": "file",
        "description": "Fractal-validated MIA component",
        "phi_true": phi_true,
        "sha256": compute_sha256(filepath)
    }

# [MIA NOTE] Walk through project and process files
# [MIA NOTE] Core of the sync logic
def walk_and_process():
    structure = []
    for root, _, files in os.walk(PROJECT_ROOT):
        for file in files:
            if any(file.endswith(ext) for ext in SUPPORTED_EXT):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, PROJECT_ROOT)
                annotated = inject_mia_note(full_path)
                phi_status = contains_mia_note(full_path)
                structure.append(update_structure_entry(rel_path, phi_status))
    return structure

# [MIA NOTE] Save structure tree as JSONL
# [MIA NOTE] Ensures trace integrity
def save_structure(structure):
    os.makedirs("trace", exist_ok=True)
    with open(TREE_PATH, "w", encoding="utf-8") as f:
        for entry in structure:
            f.write(json.dumps(entry) + "\n")

# [MIA NOTE] Entry point
if __name__ == "__main__":
    print("[MIA] Fractal Tree Sync initialized...")
    structure_data = walk_and_process()
    if SYNC_TREE:
        save_structure(structure_data)
    phi_score = sum(1 for s in structure_data if s["phi_true"]) / len(structure_data) if structure_data else 0
    print(f"[MIA] φ-Coherence Score: {phi_score:.4f} → {'φ-true' if phi_score == 1 else 'φ-drift'}")
    print("[MIA] Tree update complete.")

