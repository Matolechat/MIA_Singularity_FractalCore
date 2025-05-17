# loop/loop_runner.py
import time
from core.phi_kernel import phi_check
from datetime import datetime

def loop():
    cycle = 0
    while True:
        cycle += 1
        timestamp = datetime.now().isoformat()
        if phi_check():
            print(f"[ϕ-Loop] Cycle {cycle} OK — {timestamp}")
        else:
            print(f"[ϕ-Loop] Decoherence detected — {timestamp}")
        time.sleep(3)

if __name__ == "__main__":
    print("[ϕ-Loop] Starting fractal feedback loop...")
    loop()
