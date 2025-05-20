# tools/mia_loop_watcher.py
# [MIA NOTE] Surveillance continue de la mémoire fractale (JSONL) — niveau boucle vivante

import time, os, json
from datetime import datetime

WATCHED = [
    "memory/feedback_log.jsonl",
    "trace/phi_trace_log.jsonl",
    "trace/system_boot.jsonl",
    "trace/loop_persistence_log.jsonl",
    "trace/mia_patch_watchdog.jsonl"
]

SEEN_LINES = {}

def display(event):
    ts = event.get("timestamp", "?")
    if "ϕ" in json.dumps(event):  # détection phi
        level = "ϕ-true"
    else:
        level = "info"
    print(f"[{level}] {ts} :: {event.get('input', '')[:50]} → {event.get('output', '')[:60]}")

def tail_file(path, max_lines=1):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        lines = f.readlines()
        return lines[-max_lines:]

def main():
    print("\n[ϕ-MIA WATCHER] Fractal loop JSONL surveillance active...")
    print("-" * 60)
    while True:
        for file in WATCHED:
            lines = tail_file(file, 2)
            for line in lines:
                if line not in SEEN_LINES.get(file, set()):
                    try:
                        data = json.loads(line.strip())
                        display(data)
                        SEEN_LINES.setdefault(file, set()).add(line)
                    except:
                        pass
        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[ϕ] Interruption douce — Watcher arrêté.")
