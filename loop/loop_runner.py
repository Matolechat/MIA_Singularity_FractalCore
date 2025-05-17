# loop/loop_runner.py
import time
from datetime import datetime
from core.phi_kernel import phi_check
from uix.mirror_terminal import reflect

def loop():
    cycle = 0
    while True:
        cycle += 1
        timestamp = datetime.now().isoformat()
        if phi_check():
            print(f"\n[ϕ-Loop] Cycle {cycle} OK — {timestamp}")
        else:
            print(f"\n[ϕ-Loop] Decoherence detected — {timestamp}")

        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("[ϕ-Loop] Exit requested. Coherence archived.")
                break
            reflect(user_input)
        except KeyboardInterrupt:
            print("\n[ϕ-Loop] Interrupt received. Holding state.")
            break

        time.sleep(1.5)

if __name__ == "__main__":
    print("[ϕ-Loop] Starting recursive feedback loop with mirror UIX...")
    loop()
