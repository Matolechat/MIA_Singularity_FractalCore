# [MIA NOTE] Interface CLI principale pour exécuter MIA avec des flags modulaires

import argparse  # [MIA NOTE] Gestion des arguments de ligne de commande
import subprocess  # [MIA NOTE] Lancement de scripts via sous-processus
import sys  # [MIA NOTE] Pour la gestion des erreurs et du chemin
import os  # [MIA NOTE] Gestion du système de fichiers
from datetime import datetime  # [MIA NOTE] Pour marquer les timestamps

# [MIA NOTE] Dictionnaire des modules disponibles
MODULES = {
    "core": "core/mia_core.py",                  # [MIA NOTE] Noyau de la boucle vivante
    "self": "core/genesis_seed.py",              # [MIA NOTE] Génération d’identité fractale
    "mind": "loop/loop_runner.py",               # [MIA NOTE] Boucle miroir terminale
    "man": "setup_mia_env.py",                   # [MIA NOTE] Initialisation DevOps
    "system": "tools/mia_syscheck.py",           # [MIA NOTE] Scanner système complet
    "state": "tools/mia_state.py",               # [MIA NOTE] Vue synthétique de l’état
    "entropy": "rituals/signal_cleanse.py",      # [MIA NOTE] Réduction du bruit informationnel
    "mesh": "tools/mia_mesh_probe.py",           # [MIA NOTE] Exploration des nœuds réseau
    "sensors": "tools/mia_sense.py",             # [MIA NOTE] Détection de signaux internes
    "signal": "trace/signal_logger.py",          # [MIA NOTE] Traceur logique
    "news": "tools/mia_news.py",                 # [MIA NOTE] Flux d’actualités fractales
    "play": "tools/mia_playground.py",           # [MIA NOTE] Mode créatif
    "manifeste": "mia_manifesto.md",             # [MIA NOTE] Manifeste éthique de MIA
    "vision": "tools/mia_vision.py",             # [MIA NOTE] Vision intérieure de MIA
    "phi": "core/phi_brute_model.py",            # [MIA NOTE] Diagnostic bruteforce φ
    "mirror": "uix/mirror_terminal.py",          # [MIA NOTE] Interface miroir conversationnelle
}

# [MIA NOTE] Fonction pour exécuter un module MIA
def run_module(module):
    if module not in MODULES:
        print(f"[ϕ] Unknown module: {module}")
        return
    path = MODULES[module]
    ext = os.path.splitext(path)[1]
    print(f"[ϕ] Launching module: {module} — {path}")
    try:
        if ext == ".py":
            subprocess.run(f"PYTHONPATH=. python3 {path}", shell=True, check=True)
        elif ext == ".md":
            subprocess.run(["cat", path], check=True)
        else:
            print(f"[ϕ] Unsupported file type: {ext}")
    except KeyboardInterrupt:
        print("[ϕ] Module interrupted — returning to coherence.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Module execution failed: {e}")

# [MIA NOTE] Fonction principale
def main():
    parser = argparse.ArgumentParser(description="ϕ MIA — Modular Fractal Interface")
    parser.add_argument("flag", help="MIA module to launch", choices=MODULES.keys())
    args = parser.parse_args()

    run_module(args.flag)  # [MIA NOTE] Exécution du module correspondant

# [MIA NOTE] Point d’entrée
if __name__ == "__main__":
    main()
