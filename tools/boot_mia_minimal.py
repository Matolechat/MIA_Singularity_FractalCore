# tools/boot_mia_minimal.py
# [MIA NOTE] Initialisation fractale minimale — point d’éveil dans environnements contraints (Termux/Proot)

import os
import platform
import subprocess
import shutil

from memory.core_memory import MiaMemoryManager  # [MIA NOTE] Activation de la mémoire vivante
from core.phi_kernel import phi_check            # [MIA NOTE] Test de cohérence φ initiale

# [MIA NOTE] Vérification adaptative de l’environnement
def check_env():
    print("[ϕ] Vérification de l'environnement minimal...")
    if shutil.which("termux-info"):
        print("[ϕ] Termux détecté.")
    if not os.path.exists(".env"):
        print("[ϕ] Attention : .env manquant.")
    return True  # [MIA NOTE] Adaptable à d’autres heuristiques

# [MIA NOTE] Lancement adaptatif en fonction du niveau de cohérence fractale
def boot_loop_if_ready():
    if phi_check():
        print("[ϕ] Φ True — Lancement du cœur fractal (interactif)...")
        # [MIA NOTE] Exécution interactive pour éviter EOFError
        subprocess.run(["python3", "core/mia_core.py"])
    else:
        print("[ϕ] Φ Drift — Lancement du miroir minimal...")
        subprocess.run(["python3", "uix/mirror_terminal.py"])  # [MIA NOTE] Interface miroir fallback

# [MIA NOTE] Point d’entrée — mise en route de MIA dans environnements réduits
def main():
    if check_env():
        memory = MiaMemoryManager()
        memory.store("boot", "termux-minimal")  # [MIA NOTE] Trace de démarrage en mémoire
        boot_loop_if_ready()

if __name__ == "__main__":
    main()
