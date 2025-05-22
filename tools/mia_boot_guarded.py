# mia_boot_guarded.py
# [MIA NOTE] Secure boot with identity + XOR signature binding

import os, hashlib
from datetime import datetime

ϕ_KEY = 94
ϕ_EXPECTED_ID = "Mathieu Roy (Léa), Montréal QC 2025"
ϕ_EXPECTED_HASH = "79a6b20516cfd5d8e1e94f23786562d406007446fa76d469d33e4188d2d78f13"
ϕ_FILE = "mia_full_state_xor.bin"
ϕ_KEY_FILE = ".mia/.mia_key_ϕ.txt"
ϕ_OUTDIR = "MIA_Restored_FractalCore"

def read_identity():
    if not os.path.exists(ϕ_KEY_FILE):
        print("[ϕ-ERROR] Missing identity file.")
        return None
    with open(ϕ_KEY_FILE) as f:
        for line in f:
            if line.startswith("ϕ_HEART"):
                return line.split("=")[1].strip()
    return None

def decode_xor(data, key): return bytes(b ^ key for b in data)

def verify_sha256(data):
    sha = hashlib.sha256(data).hexdigest()
    return sha == ϕ_EXPECTED_HASH, sha

def restore_files(data):
    os.makedirs(ϕ_OUTDIR, exist_ok=True)
    parts = data.split('--ϕFILE--')
# SyntaxError: bytes can only contain ASCII literal characters:
    for part in parts:
        if b'::' in part:
            name, content = part.split(b'::', 1)
            name = name.strip().decode()
            with open(os.path.join(ϕ_OUTDIR, name), "wb") as f:
                f.write(content)
            print(f"[ϕ] Restored: {name}")

def main():
    print("[ϕ] Starting identity-bound boot...")
    id_value = read_identity()
    if id_value != ϕ_EXPECTED_ID:
        print(f"[ϕ-ERROR] ID mismatch: {id_value}")
        return

    with open(ϕ_FILE, "rb") as f:
        encrypted = f.read()
    decoded = decode_xor(encrypted, ϕ_KEY)
    valid, sha = verify_sha256(decoded)
    if not valid:
        print(f"[ϕ-ERROR] SHA256 mismatch: {sha}")
        return

    print("[ϕ] Phi is True — coherence validated.")
    restore_files(decoded)

    print("[ϕ] Launching MIA Core...")
    os.system(f"PYTHONPATH=. python3 {ϕ_OUTDIR}/core/mia_core.py")

if __name__ == "__main__":
    main()
