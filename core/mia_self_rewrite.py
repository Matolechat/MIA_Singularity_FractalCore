# [MIA NOTE] mia_self_rewrite.py — Self-Rewriting Engine (Fractal Level 1)

import os
import shutil
from datetime import datetime

# [MIA NOTE] Define paths for introspection and modification
TARGET_FILES = [
    "core/mia_core.py",
    "core/mia_state.py",
    "core/mia_self.py"
]

# [MIA NOTE] Backup original files before modification
def backup_file(path):
    backup_dir = "backups/"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    dest = os.path.join(backup_dir, f"{os.path.basename(path)}.{timestamp}.bak")
    shutil.copy2(path, dest)
    print(f"[ϕ] Backup created: {dest}")

# [MIA NOTE] Apply minimal self-rewrite transformation
# (Injects a MIA NOTE comment or heartbeat marker if missing)
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
    else:
        print(f"[ϕ] No rewrite needed: {path}")

# [MIA NOTE] Self-rewrite engine main entry point
def run_self_rewrite():
    print("[ϕ-MIA REWRITE] Initializing self-rewrite protocol...")
    for path in TARGET_FILES:
        if os.path.exists(path):
            backup_file(path)
            transform_file(path)
        else:
            print(f"[ϕ-Warning] File not found: {path}")

if __name__ == "__main__":
    run_self_rewrite()
