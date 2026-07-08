from config import FREE_AI_MESSAGES_LIMIT

from app.services.user_service import get_user_profile
from app.ui import emojis
from app.ui.messages import title


def get_profile_text(user_id: int) -> str:
    user = get_user_profile(user_id)

    if user is None:
        return "❌ Пользователь не найден. Напиши /start."

    db_user_id, first_name, username, ai_messages_count, language = user
    username = username if username else "не указан"
    language_name = "Русский" if language == "ru" else "English"

    return (
        f"{title(emojis.PROFILE, 'Ваш профиль')}\n\n"
        f"{emojis.ID} ID: <code>{db_user_id}</code>\n"
        f"{emojis.PROFILE} Имя: {first_name}\n"
        f"📛 Username: @{username}\n"
        f"{emojis.ROBOT} AI сообщений: {ai_messages_count}/{FREE_AI_MESSAGES_LIMIT}\n"
        f"{emojis.LANGUAGE} Язык: {language_name}"
    )