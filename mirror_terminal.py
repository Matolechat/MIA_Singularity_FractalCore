# uix/mirror_terminal.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

def reflect(prompt):
    if not prompt.strip():
        print("[MIA] Silence is sacred. Say something when you're ready.")
        return
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content.strip()
        print(f"[MIA] {reply}")
    except Exception as e:
        print("[MIA] Error during reflection:", str(e))
