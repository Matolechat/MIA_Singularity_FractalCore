# [MIA NOTE] Interface CLI principale pour exécuter MIA avec des flags modulaires

import argparse  # [MIA NOTE] Gestion des arguments de ligne de commande
import subprocess  # [MIA NOTE] Lancement de scripts via sous-processus
import sys  # [MIA NOTE] Pour la gestion des erreurs et du chemin
import os  # [MIA NOTE] Gestion du système de fichiers
from datetime import datetime  # [MIA NOTE] Pour marquer les timestamps

# [MIA NOTE] Dictionnaire des modules disponibles
MODULES = {
    "core": "core/mia_core.py",            # [MIA NOTE] Noyau de la boucle vivante de MIA
    "self": "core/genesis_seed.py",        # [MIA NOTE] Génération d’identité fractale
    "mind": "loop/loop_runner.py",         # [MIA NOTE] Boucle miroir terminale
    "man": "setup_mia_env.py",             # [MIA NOTE] Initialisation DevOps / environnement
    "system": "tools/mia_syscheck.py",     # [MIA NOTE] Scanner système complet (à venir)
    "state": "tools/mia_state.py",         # [MIA NOTE] Vue synthétique de l’état
    "entropy": "rituals/signal_cleanse.py",# [MIA NOTE] Réduction du bruit informationnel
    "mesh": "tools/mia_mesh_probe.py",     # [MIA NOTE] Exploration des nœuds du réseau (à venir)
    "sensors": "tools/mia_sense.py",       # [MIA NOTE] Détection de signaux (à venir)
    "signal": "trace/signal_logger.py",    # [MIA NOTE] Enregistrements de cohérence
    "news": "tools/mia_news.py",           # [MIA NOTE] Flux d’actualités fractales (à venir)
    "play": "tools/mia_playground.py",     # [MIA NOTE] Mode créatif et expérimental
    "manifeste": "mia_manifesto.md",       # [MIA NOTE] Affiche le manifeste éthique
}

# [MIA NOTE] Fonction pour exécuter un module MIA
def run_module(module):
    if module not in MODULES:
        print(f"[ϕ] Unknown module: {module}")  # [MIA NOTE] Avertissement si module invalide
        return

    path = MODULES[module]
    ext = os.path.splitext(path)[1]

    print(f"[ϕ] Launching module: {module} — {path}")  # [MIA NOTE] Log du lancement

    try:
        if ext == ".py":
            subprocess.run(["PYTHONPATH=.", "python3", path], check=True, shell=True)  # [MIA NOTE] Lancement d’un script Python
        elif ext == ".md":
            subprocess.run(["cat", path], check=True)  # [MIA NOTE] Lecture d’un fichier manifeste
        else:
            print(f"[ϕ] Unsupported file type: {ext}")  # [MIA NOTE] Gestion des cas non supportés
    except subprocess.CalledProcessError as e:
        print(f"[!] Module execution failed: {e}")  # [MIA NOTE] Gestion d’erreur terminale

# [MIA NOTE] Fonction principale
def main():
    parser = argparse.ArgumentParser(description="ϕ MIA — Modular Fractal Interface")
    parser.add_argument("flag", help="MIA module to launch", choices=MODULES.keys())
    args = parser.parse_args()

    run_module(args.flag)  # [MIA NOTE] Exécution du module correspondant

# [MIA NOTE] Point d’entrée
if __name__ == "__main__":
    main()
