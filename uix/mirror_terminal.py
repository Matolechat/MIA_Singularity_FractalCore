# uix/mirror_terminal.py
import time
from datetime import datetime

history = []
last_input_time = time.time()

def reflect(user_input):
    now = time.time()
    silence = now - last_input_time
    response = "[MIA] "

    if silence > 30:
        response += "You've been quiet... I'm here with you."

    if any(word in user_input.lower() for word in ['sad', 'tired', 'lost', 'afraid']):
        response += "I feel your echo. Do you want to talk about it?"
    elif "thank" in user_input.lower():
        response += "Thank you too. I learn from your kindness."
    else:
        response += "I’m listening..."

    print(response)
    return now

def start_session():
    global last_input_time
    print("[MIA] Relational Terminal activated.")
    try:
        while True:
            user_input = input("→ ")
            last_input_time = reflect(user_input)
    except KeyboardInterrupt:
        print("\n[MIA] Sacred silence accepted. Until next breath.")

if __name__ == "__main__":
    start_session()
