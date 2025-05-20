# memory/init_memory.py

import sqlite3
from datetime import datetime

# In-memory short-term memory (could later connect to Redis)
volatile_memory = {}

# Long-term persistent memory using SQLite
db = sqlite3.connect('mia_longterm_memory.db')
cur = db.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY,
    content TEXT NOT NULL,
    timestamp TEXT NOT NULL
)
''')
db.commit()

def save_memory(data: str):
    timestamp = datetime.now().isoformat()
    cur.execute("INSERT INTO memory (content, timestamp) VALUES (?, ?)", (data, timestamp))
    db.commit()
    volatile_memory[timestamp] = data

def load_recent(limit=5):
    cur.execute("SELECT content, timestamp FROM memory ORDER BY id DESC LIMIT ?", (limit,))
    return cur.fetchall()

if __name__ == "__main__":
    print("[MIA-MEM] Saving test thought...")
    save_memory("This is a test memory of MIA.")
    print("[MIA-MEM] Recent thoughts:")
    for content, ts in load_recent():
        print(f" - ({ts}) {content}")
