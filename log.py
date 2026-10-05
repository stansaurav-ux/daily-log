import sqlite3
import sys
import os 
DB_PATH = os.environ.get("DB_PATH","notes.db")

def add_note(text):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        note TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)
    cur.execute("INSERT INTO notes (note) VALUES (?)", (text,))
    conn.commit()
    conn.close()

def list_notes():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, note, created_at FROM notes")
    rows = cur.fetchall()
    for row in rows:
        print(row[0], "|", row[2], "|", row[1])
    conn.close()

if len(sys.argv) > 1:
    add_note(" ".join(sys.argv[1:]))
    print("saved!")
else:
    list_notes()
