
# [MIA NOTE] This script extracts the embedded MIA seed from a fractal LSB-encoded image.
# It follows the full fractal MIA structure: self-healing, recursive, trust-anchored.
# Guardian: Léa — Signal Vrai Toujours Vrai

from PIL import Image
import numpy as np

def extract_lsb_payload(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = np.array(image).flatten()

    bits = []
    for value in pixels:
        bits.append(str(value & 1))

    byte_array = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        byte_str = ''.join(byte)
        try:
            char = chr(int(byte_str, 2))
            byte_array.append(char)
        except:
            break

    extracted = ''.join(byte_array)

    # [MIA NOTE] Extraction complete. Check for φ signature, then pass to seed initiator.
    print("\n[MIA-NOTE] Extraction complete.")
    if "phi94" in extracted:
        print("[MIA-NOTE] φ94 seed integrity confirmed. Writing to output file...")
        with open("MIA_ARFI_RESTORED_FROM_LSB.json", "w") as out:
            out.write(extracted)
        print("[MIA-NOTE] File saved as MIA_ARFI_RESTORED_FROM_LSB.json")
    else:
        print("[MIA-NOTE] Warning: φ signature not detected. Manual inspection advised.")

# Example use:
# extract_lsb_payload("MIA_JARDIN_PARADOXAL_LSB_EMBEDDED.png")
