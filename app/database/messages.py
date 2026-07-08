from app.database.database import get_connection


def save_message(user_id: int, role: str, text: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO messages (user_id, role, text)
        VALUES (?, ?, ?)
    """, (user_id, role, text))

    connection.commit()
    connection.close()


def get_last_messages(user_id: int, limit: int = 10):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT role, text
        FROM messages
        WHERE user_id = ?
        ORDER BY id DESC
        LIMIT ?
    """, (user_id, limit))

    messages = cursor.fetchall()
    connection.close()

    return list(reversed(messages))


def clear_messages(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM messages WHERE user_id = ?", (user_id,))

    connection.commit()
    connection.close()