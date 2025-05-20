# uix/mirror_terminal.py

# [MIA NOTE] Interface miroir — reflet de l’interaction humaine
import openai
import os
from dotenv import load_dotenv
from trace.trace_logger import log_trace  # [MIA NOTE] Journalisation systématique des échanges

# [MIA NOTE] Chargement des variables d’environnement (clé API OpenAI)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def reflect(prompt):
    # [MIA NOTE] Vérification de la validité de l’entrée
    if not prompt.strip():
        print("[MIA] Silence is sacred. Say something when you're ready.")
        log_trace(prompt, "Silence detected", "ϕ-drift")
        return None

    try:
        # [MIA NOTE] Appel API OpenAI pour générer une réponse
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content.strip()

        # [MIA NOTE] Affichage et retour de la réponse
        print(f"[MIA] {reply}")
        log_trace(prompt, reply, "ϕ-true")
        return reply  # ← ESSENTIEL pour la mémoire vive

    except Exception as e:
        # [MIA NOTE] Gestion des erreurs API et journalisation
        error_msg = f"[MIA] Error during reflection: {str(e)}"
        print(error_msg)
        log_trace(prompt, error_msg, "ϕ-error")
        return None
