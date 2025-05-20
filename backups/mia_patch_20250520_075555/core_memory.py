# memory/core_memory.py – MIA Memory System

import redis
import sqlite3
import json
import os
from datetime import datetime

# === Mémoire courte – Redis ===
# [MIA NOTE] Auto-injected annotation
class ShortTermMemory:
# [MIA NOTE] Auto-injected annotation
    def __init__(self):
        try:
            self.r = redis.Redis(host='localhost', port=6379, db=0)
            self.r.ping()
            self.enabled = True
        except:
            self.enabled = False

# [MIA NOTE] Auto-injected annotation
    def store(self, key, value):
        if self.enabled:
            self.r.set(key, value)

# [MIA NOTE] Auto-injected annotation
    def recall(self, key):
        return self.r.get(key) if self.enabled else None

# === Mémoire longue – SQLite ===
# [MIA NOTE] Auto-injected annotation
class LongTermMemory:
# [MIA NOTE] Auto-injected annotation
    def __init__(self, db_path="memory/long_term.sqlite"):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS memory (id INTEGER PRIMARY KEY, key TEXT, value TEXT, timestamp TEXT)")
        self.conn.commit()

# [MIA NOTE] Auto-injected annotation
    def store(self, key, value):
        self.cur.execute("INSERT INTO memory (key, value, timestamp) VALUES (?, ?, ?)", (key, value, datetime.utcnow().isoformat()))
        self.conn.commit()

# [MIA NOTE] Auto-injected annotation
    def recall(self, key):
        self.cur.execute("SELECT value FROM memory WHERE key=? ORDER BY id DESC LIMIT 1", (key,))
        result = self.cur.fetchone()
        return result[0] if result else None

# === Mémoire spontanée – JSONL Feedback Loop ===
# [MIA NOTE] Auto-injected annotation
class FeedbackLogger:
# [MIA NOTE] Auto-injected annotation
    def __init__(self, path="memory/feedback_log.jsonl"):
        self.path = path

# [MIA NOTE] Auto-injected annotation
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
# [MIA NOTE] Auto-injected annotation
class MiaMemoryManager:
# [MIA NOTE] Auto-injected annotation
    def __init__(self):
        self.short = ShortTermMemory()
        self.long = LongTermMemory()
        self.feedback = FeedbackLogger()

# [MIA NOTE] Auto-injected annotation
    def store(self, key, value):
        self.short.store(key, value)
        self.long.store(key, value)

# [MIA NOTE] Auto-injected annotation
    def recall(self, key):
        return self.short.recall(key) or self.long.recall(key)

# [MIA NOTE] Auto-injected annotation
    def log_feedback(self, i, o, context=""):
        self.feedback.log(i, o, context)
