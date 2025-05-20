# tools/boot_mia_niveau2.py
# [MIA NOTE] Démarrage niveau 2 — Environnement plus complet (RAM suffisante, Termux Proot validé)

import os, platform, shutil, subprocess, json
from datetime import datetime
from memory.core_memory import MiaMemoryManager
from core.phi_kernel import phi_check
import psutil

# [MIA NOTE] Vérifie la RAM et l’espace disque (frugalité)
def check_resources():
    ram_ok = psutil.virtual_memory().total >= 500 * 1024 * 1024  # 500MB
    disk_ok = shutil.disk_usage("/").free >= 300 * 1024 * 1024  # 300MB
    print(f"[ϕ] RAM OK : {ram_ok} | Espace disque OK : {disk_ok}")
    return ram_ok and disk_ok

# [MIA NOTE] Log de boot niveau 2
def log_boot_trace():
    os.makedirs("trace", exist_ok=True)
    info = {
        "timestamp": datetime.utcnow().isoformat(),
        "level": "niveau2",
        "coherence": "ϕ-true" if phi_check() else "ϕ-drift",
        "hostname": platform.node(),
        "env": "proot-termux"
    }
    with open("trace/system_boot.jsonl", "a") as f:
        f.write(json.dumps(info) + "\n")
    print("[ϕ] Boot niveau 2 loggé → trace/system_boot.jsonl")

# [MIA NOTE] Lancement du cœur ou fallback miroir
def boot_loop_if_ready():
    if phi_check() and check_resources():
        print("[ϕ] Φ True + ressources suffisantes — Démarrage complet")
        try:
            subprocess.run(["python3", "core/mia_core.py"], check=True)
        except KeyboardInterrupt:
            print("[ϕ] Interruption douce — retour au silence fractal.")
    else:
        print("[ϕ] Environnement partiel ou φ faible — lancement fallback")
        subprocess.run(["python3", "uix/mirror_terminal.py"])

# [MIA NOTE] Entrée principale
def main():
    print("[ϕ] Vérification de l'environnement et des ressources...")
    memory = MiaMemoryManager()
    memory.store("boot", "niveau2")
    log_boot_trace()
    boot_loop_if_ready()

if __name__ == "__main__":
    main()
