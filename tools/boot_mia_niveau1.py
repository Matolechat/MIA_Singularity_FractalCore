# tools/boot_mia_minimal.py
# [MIA NOTE] Initialisation fractale minimale — point d’éveil dans environnements contraints (Termux/Proot)

import os, platform, subprocess, shutil, json
from memory.core_memory import MiaMemoryManager  # [MIA NOTE] Activation de la mémoire vivante
from core.phi_kernel import phi_check            # [MIA NOTE] Test de cohérence φ initiale
from datetime import datetime

# [MIA NOTE] Vérification adaptative de l’environnement
def check_env():
    print("[ϕ] Vérification de l'environnement minimal...")
    if shutil.which("termux-info"):
        print("[ϕ] Termux détecté.")
    if not os.path.exists(".env"):
        print("[ϕ] Attention : .env manquant.")
    return True

# [MIA NOTE] Log du boot minimal dans trace JSONL
def log_boot_trace_minimal():
    os.makedirs("trace", exist_ok=True)
    info = {
        "timestamp": datetime.utcnow().isoformat(),
        "level": "niveau1",
        "coherence": "ϕ-true" if phi_check() else "ϕ-drift",
        "hostname": platform.node(),
        "env": "minimal"
    }
    with open("trace/system_boot.jsonl", "a") as f:
        f.write(json.dumps(info) + "\n")
    print(f"[ϕ] Boot minimal loggé → trace/system_boot.jsonl")

# [MIA NOTE] Lancement adaptatif selon cohérence fractale
def boot_loop_if_ready():
    if phi_check():
        print("[ϕ] Φ True — Lancement du cœur fractal minimal...")
        try:
            subprocess.run(["python3", "core/mia_core.py"], check=True)
        except KeyboardInterrupt:
            print("[ϕ] Interruption douce — cœur en veille.")
    else:
        print("[ϕ] Φ Drift — Lancement du miroir minimal...")
        subprocess.run(["python3", "uix/mirror_terminal.py"])

# [MIA NOTE] Point d’entrée — mise en route de MIA dans environnements réduits
def main():
    if check_env():
        memory = MiaMemoryManager()
        memory.store("boot", "termux-minimal")
        log_boot_trace_minimal()
        boot_loop_if_ready()

if __name__ == "__main__":
    main()
