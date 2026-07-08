import sqlite3

from config import DATABASE_NAME


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            username TEXT,
            ai_mode INTEGER DEFAULT 0,
            ai_messages_count INTEGER DEFAULT 0,
            language TEXT DEFAULT 'ru'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            role TEXT,
            text TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()