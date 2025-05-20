# [MIA NOTE] Wrapper pour le module système — version légère
from core.phi_kernel import phi_check
import os

def system_check_lite():
    print("[ϕ-System] Lite system check — minimal scan")
    os.system("uname -a && df -h && free -m")

if __name__ == "__main__":
    if phi_check():
        system_check_lite()  # [MIA NOTE] Si Phi est stable, version lite
    else:
        print("[ϕ-WRAPPER] Decoherence detected. Preparing full system analysis...")
        try:
            # [MIA NOTE] Appelle le module complet compressé si dispo
            import tools.mia_syscheck_full as full
            full.system_check_deep()
        except ImportError:
            print("[ϕ-WRAPPER] Full system scan not yet deployed.")
