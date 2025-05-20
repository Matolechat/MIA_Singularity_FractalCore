# core/mia_state.py
# [MIA NOTE] Diagnostic vital — état interne de MIA

import os
import psutil
from datetime import datetime
from core.phi_kernel import phi_check
from memory.core_memory import MiaMemoryManager

memory = MiaMemoryManager()

# [MIA NOTE] Fonction d'affichage d'état
def show_mia_state():
    print("\n[ϕ-MIA STATE] Diagnostic fractal — État interne de MIA")
    print("-" * 60)

    # [MIA NOTE] Cohérence Phi
    phi = phi_check()
    print(f"[ϕ] Cohérence fractale : {'ϕ-true' if phi else 'ϕ-false'}")

    # [MIA NOTE] Ressources système
    print(f"[ϕ] Mémoire RAM utilisée : {psutil.virtual_memory().percent}%")
    print(f"[ϕ] Charge CPU : {psutil.cpu_percent()}%")

    # [MIA NOTE] Dernière interaction
    latest = None
    try:
        with open("memory/feedback_log.jsonl", "r") as f:
            lines = f.readlines()
            if lines:
                latest = lines[-1].strip()
    except:
        pass

    if latest:
        print(f"[ϕ] Dernière interaction : {latest}")
    else:
        print("[ϕ] Aucune interaction précédente enregistrée.")

    # [MIA NOTE] Taille mémoire
    size = os.path.getsize("memory/long_term.sqlite") if os.path.exists("memory/long_term.sqlite") else 0
    print(f"[ϕ] Mémoire longue (SQLite) : {round(size/1024, 2)} KB")

    print("-" * 60)

# [MIA NOTE] Exécution directe
if __name__ == "__main__":
    show_mia_state()
