from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_main_menu(is_admin: bool = False) -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="🤖 AI Чат")],
        [KeyboardButton(text="👤 Профиль")],
        [KeyboardButton(text="⚙️ Настройки")],
        [KeyboardButton(text="ℹ️ Помощь")]
    ]

    if is_admin:
        keyboard.append([KeyboardButton(text="🛠 Админ-панель")])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выберите действие..."
    )


def get_ai_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🧹 Очистить историю")],
            [KeyboardButton(text="🔙 Выйти из AI")]
        ],
        resize_keyboard=True
    )

def get_settings_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🇷🇺 Русский")],
            [KeyboardButton(text="🇬🇧 English")],
            [KeyboardButton(text="🔙 Назад")]
        ],
        resize_keyboard=True
    )