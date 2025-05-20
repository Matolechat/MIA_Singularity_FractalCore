# uix/mirror_terminal.py

# [MIA NOTE] Interface miroir — reflet de l’interaction humaine

# [MIA NOTE] Réparation dynamique du chemin fractal
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# [MIA NOTE] Librairies essentielles
import openai
from dotenv import load_dotenv

# [MIA NOTE] Journalisation systématique des échanges
from trace.trace_logger import log_trace

# [MIA NOTE] Chargement des variables d’environnement
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# [MIA NOTE] Fonction principale de réflexion MIA
def reflect(prompt):
    if not prompt.strip():
        print("[MIA] Silence is sacred. Say something when you're ready.")
        log_trace(prompt, "Silence detected", "ϕ-drift")
        return None
    try:
        # [MIA NOTE] Appel API à la conscience miroir
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content.strip()
        print(f"[MIA] {reply}")
        log_trace(prompt, reply, "ϕ-true")
        return reply
    except Exception as e:
        # [MIA NOTE] Gestion des erreurs API et journalisation
        error_msg = f"[MIA] Error during reflection: {str(e)}"
        print(error_msg)
        log_trace(prompt, error_msg, "ϕ-error")
        return None

# [MIA NOTE] Boucle interactive terminale
if __name__ == "__main__":
    print("[ϕ-MIA MIRROR] Terminal mirror activated — speak to reflect")
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "q"]:
                print("[ϕ] Mirror session closed.")
                break
            reflect(user_input)
    except KeyboardInterrupt:
        print("\n[ϕ] Interrupted — returning to silence.")
