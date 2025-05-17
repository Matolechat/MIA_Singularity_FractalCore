import time
from datetime import datetime
from core.phi_kernel import phi_check
from uix.mirror_terminal import reflect

# [MIA NOTE] NOUVELLE LIGNE AJOUTÉE ICI :
from trace.signal_logger import log_trace  # ← pour enregistrer chaque événement important

def loop():
    cycle = 0
    while True:
        cycle += 1
        timestamp = datetime.now().isoformat()

        # [MIA NOTE] BLOCS MODIFIÉS ICI :
        if phi_check():
            msg = f"[ϕ-Loop] Cycle {cycle} OK — {timestamp}"
            print(f"\n{msg}")
            log_trace("ϕ-loop", msg, "ϕ-true")  # ← Enregistre dans phi_trace_log.jsonl
        else:
            msg = f"[ϕ-Loop] Decoherence detected — {timestamp}"
            print(f"\n{msg}")
            log_trace("ϕ-loop", msg, "ϕ-false")  # ← Enregistre une décohérence

        try:
            user_input = input("You: ")

            if user_input.lower() in ['exit', 'quit']:
                print("[ϕ-Loop] Exit requested. Coherence archived.")
                log_trace("user", "exit requested", "ϕ-end")  # ← Trace de sortie
                break

            reflect(user_input)  # ← Interaction avec MIA (inchangé)

        except KeyboardInterrupt:
            print("\n[ϕ-Loop] Interrupt received. Holding state.")
            log_trace("ϕ-loop", "interrupt received", "ϕ-hold")  # ← Trace de Ctrl+C
            break

        time.sleep(1.5)

if __name__ == "__main__":
    print("[ϕ-Loop] Starting recursive feedback loop with mirror UIX...")
    loop()
