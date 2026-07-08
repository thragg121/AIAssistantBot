from app.database.users import get_all_users, get_users_count
from app.ui import emojis
from app.ui.messages import title


def get_admin_panel_text() -> str:
    users_count = get_users_count()

    return (
        f"{title(emojis.ADMIN, 'Админ-панель')}\n\n"
        f"{emojis.USERS} Пользователей: <b>{users_count}</b>\n\n"
        "<b>Команды:</b>\n"
        "/users — список пользователей\n"
        "/broadcast текст — рассылка"
    )


def get_users_list_text() -> str:
    users = get_all_users()

    if not users:
        return "Пользователей пока нет."

    text = f"{title(emojis.USERS, 'Пользователи')}\n\n"

    for user_id, first_name, username in users:
        username = username if username else "не указан"
        text += (
            f"{emojis.ID} ID: <code>{user_id}</code>\n"
            f"{emojis.PROFILE} Имя: {first_name}\n"
            f"📛 Username: @{username}\n\n"
        )

    return text