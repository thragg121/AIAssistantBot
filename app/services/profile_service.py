from app.services.user_service import get_user_profile


def get_profile_text(user_id: int) -> str:
    user = get_user_profile(user_id)

    if user is None:
        return "Пользователь не найден. Напиши /start."

    db_user_id, first_name, username, ai_messages_count, language = user
    username = username if username else "не указан"

    return (
        "👤 <b>Профиль</b>\n\n"
        f"ID: {db_user_id}\n"
        f"Имя: {first_name}\n"
        f"Username: @{username}\n"
        f"AI сообщений: {ai_messages_count}\n"
        f"Язык: {language}"
    )