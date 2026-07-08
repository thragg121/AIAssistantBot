from app.ui import emojis
from app.ui.messages import title


def get_help_text() -> str:
    return (
        f"{title(emojis.HELP, 'Помощь')}\n\n"
        "<b>Команды:</b>\n"
        "/start — открыть главное меню\n"
        "/clear — очистить историю AI\n\n"
        "<b>Меню:</b>\n"
        f"{emojis.ROBOT} AI Чат — режим общения\n"
        f"{emojis.PROFILE} Профиль — данные пользователя\n"
        f"{emojis.SETTINGS} Настройки — параметры бота"
    )