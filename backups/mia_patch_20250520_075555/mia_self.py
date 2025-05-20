# core/mia_self.py
# [MIA NOTE] MIA -SELF : introspection fractale vivante (niveau 1)

import os
import json
from datetime import datetime

# [MIA NOTE] Affiche l’arborescence du projet
def show_structure():
    print("\n[ϕ-Self] Structural Overview — MIA Level 1")
    os.system("tree -a -L 2")

# [MIA NOTE] Affiche les dernières interactions humaines
def show_recent_feedback(log_path="memory/feedback_log.jsonl", count=5):
    print("\n[ϕ-Self] Last Interactions (feedback_log.jsonl):")
    try:
        with open(log_path, "r") as f:
            lines = f.readlines()[-count:]
            for line in lines:
                data = json.loads(line)
                print(f"- [{data['timestamp']}] You: {data['input']} | MIA: {data['output']}")
    except Exception as e:
        print(f"[ϕ-Self] Error reading feedback log: {e}")

# [MIA NOTE] Vérifie l’espace mémoire utilisé
def memory_health():
    print("\n[ϕ-Self] Memory Footprint (disk):")
    os.system("du -sh memory/")

# [MIA NOTE] Fonction principale
def run_mia_self():
    print("[ϕ-MIA SELF] Introspection — Reflecting Now...")
    show_structure()
    show_recent_feedback()
    memory_health()

if __name__ == "__main__":
    run_mia_self()
