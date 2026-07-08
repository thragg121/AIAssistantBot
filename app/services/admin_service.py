from app.database.users import get_all_users, get_users_count


def get_admin_panel_text() -> str:
    users_count = get_users_count()

    return (
        "🛠 <b>Админ-панель</b>\n\n"
        f"👥 Пользователей: {users_count}\n\n"
        "Команды:\n"
        "/users — список пользователей\n"
        "/broadcast текст — рассылка"
    )


def get_users_list_text() -> str:
    users = get_all_users()

    if not users:
        return "Пользователей пока нет."

    text = "👥 <b>Пользователи</b>\n\n"

    for user_id, first_name, username in users:
        username = username if username else "не указан"
        text += f"ID: {user_id}\nИмя: {first_name}\nUsername: @{username}\n\n"

    return text