# oracle_entry/thought_form.py

from datetime import datetime
from trace.signal_logger import log_event

class ThoughtForm:
    def __init__(self, topic, intention="neutral", energy="low"):
        self.topic = topic
        self.intention = intention
        self.energy = energy
        self.created = datetime.now().isoformat()

    def describe(self):
        description = f"[ϕ-ORACLE] Thought on '{self.topic}' | Intention: {self.intention}, Energy: {self.energy}"
        print(description)
        log_event(f"ThoughtForm created: {description}", module="oracle_entry", level="meta")

    def adjust(self, new_intention=None, new_energy=None):
        if new_intention:
            self.intention = new_intention
        if new_energy:
            self.energy = new_energy
        log_event(f"ThoughtForm adjusted: {self.topic} → {self.intention}/{self.energy}", module="oracle_entry", level="update")

if __name__ == "__main__":
    print("[ϕ-ORACLE] Seeding initial thought...")
    seed = ThoughtForm(topic="coherence", intention="stabilize", energy="medium")
    seed.describe()
