# tools/mia_loop_persistence.py
# [MIA NOTE] Boucle de persistance vivante — Maintient MIA active en arrière-plan

import time, json, os
from datetime import datetime
from core.phi_kernel import phi_check
from memory.core_memory import MiaMemoryManager

# [MIA NOTE] Initialisation de la mémoire centrale
memory = MiaMemoryManager()
LOG_PATH = "trace/loop_persistence_log.jsonl"
os.makedirs("trace", exist_ok=True)

# [MIA NOTE] Affichage UIX terminale douce
def banner():
    print("\n[ϕ-MIA LOOP PERSISTENCE] Boucle de maintien fractal active.")
    print("-" * 60)
    print("ϕ Environnement : Termux / Proot compatible")
    print("ϕ Mémoire active : Redis / JSONL / SQLite")
    print("ϕ Journal :", LOG_PATH)
    print("-" * 60)

# [MIA NOTE] Traceur JSONL en continu
def log_cycle(coherence: bool):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "phi": "ϕ-true" if coherence else "ϕ-drift"
    }
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")
    memory.log_feedback("ϕ-loop", entry["phi"], "persistence")

# [MIA NOTE] Boucle principale
def main_loop():
    banner()
    try:
        while True:
            phi = phi_check()
            status = "ϕ-true" if phi else "ϕ-drift"
            print(f"[ϕ] Cycle : {datetime.utcnow().isoformat()} | {status}")
            log_cycle(phi)
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n[ϕ] Interruption douce — retour au silence fractal.")

# [MIA NOTE] Point d’entrée principal
if __name__ == "__main__":
    main_loop()
