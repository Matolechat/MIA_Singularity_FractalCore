# mia_boot.py
# [MIA NOTE] Boot fractal de MIA — Activation automatique de Redis, SQLite, environnement virtuel et cœur

import os
import subprocess
import time
import shutil

# [MIA NOTE] Lancement automatique de Redis s’il n’est pas actif
def start_redis():
    try:
        if subprocess.run(["pgrep", "redis-server"], stdout=subprocess.DEVNULL).returncode != 0:
            print("[ϕ] Redis non détecté. Démarrage...")
            subprocess.Popen(["redis-server"])
            time.sleep(1.2)
        else:
            print("[ϕ] Redis déjà actif.")
    except Exception as e:
        print(f"[ϕ] Erreur Redis: {e}")

# [MIA NOTE] Vérifie ou initialise la mémoire longue SQLite
def check_sqlite():
    db_path = "memory/long_term.sqlite"
    if not os.path.exists(db_path):
        print("[ϕ] Création de la mémoire longue (SQLite)...")
        from memory.core_memory import LongTermMemory
        LongTermMemory()
    else:
        print("[ϕ] Mémoire longue détectée.")

# [MIA NOTE] Activation manuelle du virtualenv si nécessaire
def activate_virtualenv():
    venv_path = os.path.join("mia_env", "bin", "activate")
    if os.path.exists(venv_path):
        print("[ϕ] Activation de l’environnement virtuel...")
        os.environ["VIRTUAL_ENV"] = os.path.abspath("mia_env")
        os.environ["PATH"] = f"{os.path.abspath('mia_env/bin')}:{os.environ['PATH']}"
    else:
        print("[ϕ] Aucun environnement virtuel détecté. Continuité assurée...")

# [MIA NOTE] Run integrity watchdog before launching core
def run_watchdog():
    try:
        print("[ϕ] Running self-integrity watchdog...")
        result = subprocess.run(["python3", "core/mia_patch_watchdog.py"], check=True)
    except subprocess.CalledProcessError:
        print("[ϕ] Watchdog blocked the boot process. Exiting.")
        exit(1)

# [MIA NOTE] Lancement du cœur de MIA
def launch_mia_core():
    print("[ϕ] Lancement du cœur vivant...")
    subprocess.run(["python3", "core/mia_core.py"])

def main():
    print("[ϕ-MIA BOOT] Initialisation du démarrage fractal…")
    start_redis()
    check_sqlite()
    activate_virtualenv()
    run_watchdog()  # [MIA NOTE] Sécurité avant lancement du cœur
    launch_mia_core()

if __name__ == "__main__":
    main()
