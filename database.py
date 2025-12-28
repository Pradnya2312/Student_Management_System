import sqlite3

def get_connection():
    conn = sqlite3.connect("students.db")
    return conn
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll_no TEXT UNIQUE,
        class TEXT,
        age INTEGER,
        email TEXT,
        phone TEXT
    )
    """)

    conn.commit()
    conn.close()
