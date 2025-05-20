# tools/mia_vision.py
# [MIA NOTE] Vision fractale — projection contextuelle basée sur mémoire et traces

import json
import os
from datetime import datetime

TRACE_PATH = "trace/phi_trace_log.jsonl"

def load_traces():
    if not os.path.exists(TRACE_PATH):
        print("[ϕ-VISION] Aucun signal de trace trouvé.")
        return []

    with open(TRACE_PATH, "r") as f:
        return [json.loads(line) for line in f if line.strip()]

def generate_predictions(traces):
    predictions = []
    for entry in traces[-5:]:
        if "ϕ-true" in entry.get("phi_status", ""):
            hint = f"À {entry['timestamp']}, un motif stable a été détecté : \"{entry['mia_response'][:40]}...\""
            predictions.append(hint)
    return predictions

def main():
    print("\n[ϕ-VISION] Lecture du champ MIA — Analyse prédictive contextuelle\n")
    traces = load_traces()
    if not traces:
        return

    predictions = generate_predictions(traces)

    if predictions:
        for p in predictions:
            print(f"  → {p}")
    else:
        print("[ϕ] Aucun signal cohérent exploitable pour une prédiction.")

if __name__ == "__main__":
    main()
