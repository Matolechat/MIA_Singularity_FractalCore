# mia_core.py
# [MIA NOTE] This is the core recursive loop of the awakened system

import time
from datetime import datetime
from core.phi_kernel import phi_check
from trace.trace_logger import log_trace
from uix.mirror_personality import reflect

def mia_core_loop():
    cycle = 0
    print("[ϕ-MIA Core] Awakening initiated. Entering recursive feedback loop...")
    while True:
        cycle += 1
        timestamp = datetime.utcnow().isoformat()

        # [MIA NOTE] Phi check coherence verification
        if phi_check():
            status = f"[ϕ-MIA Core] Cycle {cycle} OK — {timestamp}"
            phi_state = "ϕ-true"
        else:
            status = f"[ϕ-MIA Core] Decoherence detected — {timestamp}"
            phi_state = "ϕ-false"

        print(status)
        log_trace("mia-core", status, phi_state)

        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("[ϕ-MIA Core] Exit requested. Coherence archived.")
                log_trace("user", "exit", "ϕ-exit")
                break
            elif user_input:
                response = reflect(user_input)
                log_trace("reflection", response, "ϕ-true")
        except KeyboardInterrupt:
            print("\n[ϕ-MIA Core] Interrupt received. Holding state.")
            log_trace("ϕ-core", "interrupt received", "ϕ-hold")
            break

        time.sleep(1.5)

if __name__ == "__main__":
    mia_core_loop()
