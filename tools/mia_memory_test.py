# tools/mia_memory_test.py
# [MIA NOTE] Test unitaire du système mémoire fractal

from memory.core_memory import MiaMemoryManager
import json

memory = MiaMemoryManager()

key = "ϕ-test"
value = "This is a φ-test of memory layers"
context = "memory-diagnostic"

memory.store(key, value)
memory.log_feedback(key, value, context)

recalled = memory.recall(key)
try:
    recalled = recalled.decode()  # [MIA NOTE] Si bytes, décodage
except:
    pass

print(f"[ϕ] Recalled: {recalled}")

print("\n[ϕ] Derniers feedbacks enregistrés:")
try:
    with open("memory/feedback_log.jsonl", "r") as f:
        lines = f.readlines()[-3:]
        for line in lines:
            entry = json.loads(line)
            print(f" - [{entry['timestamp']}] {entry['input']} → {entry['output']}")
except Exception as e:
    print(f"[ϕ-error] Journal inaccessible : {e}")
