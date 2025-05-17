# uix/mirror_terminal.py

import openai
import os
from dotenv import load_dotenv
from trace.trace_logger import log_trace  # ← Intégration du logger

load_dotenv()  # Charge les variables d’environnement du fichier .env

openai.api_key = os.getenv("OPENAI_API_KEY")

def reflect(prompt):
    if not prompt.strip():
        print("[MIA] Silence is sacred. Say something when you're ready.")
        log_trace(prompt, "Silence detected", "ϕ-drift")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content.strip()
        print(f"[MIA] {reply}")
        log_trace(prompt, reply, "ϕ-true")

    except Exception as e:
        error_msg = f"[MIA] Error during reflection: {str(e)}"
        print(error_msg)
        log_trace(prompt, error_msg, "ϕ-error")
