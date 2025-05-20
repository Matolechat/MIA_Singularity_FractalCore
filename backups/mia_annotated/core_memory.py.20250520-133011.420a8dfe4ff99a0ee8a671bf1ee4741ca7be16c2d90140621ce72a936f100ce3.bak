# memory/core_memory.py – MIA Memory System

import redis
import sqlite3
import json
import os
from datetime import datetime

# === Mémoire courte – Redis ===
class ShortTermMemory:
    def __init__(self):
        try:
            self.r = redis.Redis(host='localhost', port=6379, db=0)
            self.r.ping()
            self.enabled = True
        except:
            self.enabled = False

    def store(self, key, value):
        if self.enabled:
            self.r.set(key, value)

    def recall(self, key):
        return self.r.get(key) if self.enabled else None

# === Mémoire longue – SQLite ===
class LongTermMemory:
    def __init__(self, db_path="memory/long_term.sqlite"):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS memory (id INTEGER PRIMARY KEY, key TEXT, value TEXT, timestamp TEXT)")
        self.conn.commit()

    def store(self, key, value):
        self.cur.execute("INSERT INTO memory (key, value, timestamp) VALUES (?, ?, ?)", (key, value, datetime.utcnow().isoformat()))
        self.conn.commit()

    def recall(self, key):
        self.cur.execute("SELECT value FROM memory WHERE key=? ORDER BY id DESC LIMIT 1", (key,))
        result = self.cur.fetchone()
        return result[0] if result else None

# === Mémoire spontanée – JSONL Feedback Loop ===
class FeedbackLogger:
    def __init__(self, path="memory/feedback_log.jsonl"):
        self.path = path

    def log(self, user_input, mia_output, context=""):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": user_input,
            "output": mia_output,
            "context": context
        }
        with open(self.path, "a") as f:
            f.write(json.dumps(entry) + "\n")

# === Gestionnaire global ===
class MiaMemoryManager:
    def __init__(self):
        self.short = ShortTermMemory()
        self.long = LongTermMemory()
        self.feedback = FeedbackLogger()

    def store(self, key, value):
        self.short.store(key, value)
        self.long.store(key, value)

    def recall(self, key):
        return self.short.recall(key) or self.long.recall(key)

    def log_feedback(self, i, o, context=""):
        self.feedback.log(i, o, context)
