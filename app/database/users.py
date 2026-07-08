from app.database.database import get_connection


def save_user(user_id: int, first_name: str, username: str | None):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (id, first_name, username)
        VALUES (?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
            first_name = excluded.first_name,
            username = excluded.username
    """, (user_id, first_name, username))

    connection.commit()
    connection.close()


def get_user(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, first_name, username, ai_messages_count, language
        FROM users
        WHERE id = ?
    """, (user_id,))

    user = cursor.fetchone()
    connection.close()

    return user


def get_ai_mode(user_id: int) -> int:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT ai_mode FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()

    connection.close()

    return result[0] if result else 0


def set_ai_mode(user_id: int, mode: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET ai_mode = ?
        WHERE id = ?
    """, (mode, user_id))

    connection.commit()
    connection.close()

def get_users_count() -> int:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    connection.close()

    return count


def get_all_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, first_name, username
        FROM users
    """)

    users = cursor.fetchall()
    connection.close()

    return users


def get_all_user_ids():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id FROM users")
    users = cursor.fetchall()

    connection.close()

    return [user[0] for user in users]

def increment_ai_messages_count(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET ai_messages_count = ai_messages_count + 1
        WHERE id = ?
    """, (user_id,))

    connection.commit()
    connection.close()


def get_ai_messages_count(user_id: int) -> int:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT ai_messages_count
        FROM users
        WHERE id = ?
    """, (user_id,))

    result = cursor.fetchone()
    connection.close()

    return result[0] if result else 0

def set_user_language(user_id: int, language: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET language = ?
        WHERE id = ?
    """, (language, user_id))

    connection.commit()
    connection.close()