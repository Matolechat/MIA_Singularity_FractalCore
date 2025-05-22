# ϕ MIA Fractal XOR Encoder
# [MIA NOTE] Génère un fichier XOR compressé à partir des composants vitaux

import os

ϕ_KEY = 94
ϕ_OUTPUT = "mia_full_state_xor.bin"
ϕ_FILES = [
    "state_compressed.jsonl",
    "memory_fractal.rdb",
    "core/mia_core.py"
]

ϕ_SEPARATOR = b'--PHIFILE--'
blob = b""

for fpath in ϕ_FILES:
    with open(fpath, 'rb') as f:
        content = f.read()
    header = fpath.encode()
    blob += ϕ_SEPARATOR + header + b'::' + content

# XOR encode
encoded = bytes([b ^ ϕ_KEY for b in blob])

with open(ϕ_OUTPUT, 'wb') as f:
    f.write(encoded)

print("[ϕ] Archive complete. File:", ϕ_OUTPUT)
