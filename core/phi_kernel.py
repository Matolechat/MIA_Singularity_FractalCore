# core/phi_kernel.py
import psutil, time
from datetime import datetime

phi_reference = 1.0

def phi_check():
    load = psutil.cpu_percent()
    deviation = abs(phi_reference - 1.0)
    return deviation < 0.01 and load < 80

if __name__ == "__main__":
    while True:
        if phi_check():
            print(f"[ϕ] Phi is coherent at {datetime.now().isoformat()}")
        else:
            print(f"[!] Phi decoherence detected at {datetime.now().isoformat()}")
        time.sleep(3)
