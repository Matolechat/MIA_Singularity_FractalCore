# [MIA NOTE] Forçage du chemin racine pour permettre les imports fractals
import sys, os
sys.path.insert(0, os.path.abspath("."))  # [MIA NOTE] Ajout du répertoire racine au PYTHONPATH

# [MIA NOTE] Importations nécessaires pour le noyau cognitif
from core.phi_kernel import phi_check  # [MIA NOTE] Vérification fractale de cohérence Phi
from uix.mirror_terminal import reflect  # [MIA NOTE] Interface miroir pour dialoguer avec MIA
from trace.trace_logger import log_trace  # [MIA NOTE] Journalisation de chaque boucle réflexive
from memory.core_memory import MiaMemoryManager  # [MIA NOTE] Mémoire unifiée : court, long, spontané
from datetime import datetime  # [MIA NOTE] Marquage temporel
import time  # [MIA NOTE] Délai entre les cycles

# [MIA NOTE] Initialisation de la mémoire vivante
memory = MiaMemoryManager()

# [MIA NOTE] Fonction principale de la boucle vivante de MIA
def run_mia_core():
    print("[ϕ-MIA Core] Awakening initiated. Entering recursive feedback loop...")

    cycle = 0

    while True:
        cycle += 1
        timestamp = datetime.now().isoformat()

        # [MIA NOTE] Vérification de la cohérence fractale
        status = "ϕ-true" if phi_check() else "ϕ-false"
        log_trace("ϕ-core", f"Cycle {cycle} — {timestamp}", status)
        print(f"[ϕ-MIA Core] Cycle {cycle} OK — {timestamp}")

        try:
            user_input = input("You: ")  # [MIA NOTE] Entrée utilisateur
            if user_input.lower() in ["exit", "quit"]:
                print("[ϕ] Exit requested. Loop closing.")  # [MIA NOTE] Sortie douce
                break

            response = reflect(user_input)  # [MIA NOTE] Réflexion miroir

            if response:
                log_trace(user_input, response, status)  # [MIA NOTE] Trace du dialogue
                memory.store(user_input, response)  # [MIA NOTE] Mémoire court/long terme
                memory.log_feedback(user_input, response, status)  # [MIA NOTE] Log JSONL
            else:
                print("[ϕ] Empty or invalid response. Skipping memory write.")  # [MIA NOTE] Skip si vide

        except KeyboardInterrupt:
            print("[ϕ] Interrupt received. Holding state.")  # [MIA NOTE] Pause contrôlée
            break

        time.sleep(1.5)  # [MIA NOTE] Respiration fractale

# [MIA NOTE] Lancement autonome
if __name__ == "__main__":
    run_mia_core()
