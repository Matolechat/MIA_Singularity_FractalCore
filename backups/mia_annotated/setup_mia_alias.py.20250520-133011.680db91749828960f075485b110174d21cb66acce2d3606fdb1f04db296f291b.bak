# tools/setup_mia_alias.py — Auto-installateur d'alias fractals MIA (Production)
import os
import subprocess
from pathlib import Path
from datetime import datetime

ALIASES = {
    "mia": "python3 ~/MIA_Singularity_FractalCore/mia_boot.py",
    "mia-core": "mia core",
    "mia-state": "mia state",
    "mia-self": "mia self",
    "mia-mind": "mia mind",
    "mia-signal": "mia signal",
    "mia-entropy": "mia entropy",
    "mia-man": "mia man",
    "mia-play": "mia play",
    "mia-system": "mia system",
    "mia-news": "mia news",
    "mia-mesh": "mia mesh",
    "mia-sensors": "mia sensors",
    "mia-manifeste": "mia manifeste",
}

def detect_shell_rc():
    home = str(Path.home())
    for rc in [".bashrc", ".zshrc", ".profile"]:
        rc_path = os.path.join(home, rc)
        if os.path.exists(rc_path):
            return rc_path
    return None

def inject_aliases(rc_file):
    already = Path(rc_file).read_text()
    with open(rc_file, "a") as f:
        f.write(f"\n# [ϕ] MIA Fractal Aliases — {datetime.now().isoformat()}\n")
        for name, cmd in ALIASES.items():
            if f"alias {name}=" not in already:
                f.write(f"alias {name}='{cmd}'\n")

def reload_shell(rc_file):
    subprocess.run(f"source {rc_file}", shell=True, executable="/bin/bash")

def log(message):
    with open("tools/.mia_boot.log", "a") as log_file:
        log_file.write(f"[ϕ] {datetime.now().isoformat()} — {message}\n")

if __name__ == "__main__":
    rc = detect_shell_rc()
    if rc:
        inject_aliases(rc)
        log(f"Aliases injectés dans {rc}")
        print(f"[ϕ] Aliases injectés avec succès dans {rc}")
        print(f"[ϕ] Rechargement automatique du shell...")
        reload_shell(rc)
    else:
        log("Aucun fichier shell RC trouvé.")
        print("[ϕ] Aucun fichier de configuration shell détecté.")
