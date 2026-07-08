from aiogram import F
from aiogram.types import Message

from bot import dp
from app.database.users import set_user_language
from app.keyboards.menu import get_main_menu, get_settings_menu
from app.ui import emojis
from app.ui.messages import success, title


@dp.message(F.text == "⚙️ Настройки")
async def settings_handler(message: Message):
    await message.answer(
        f"{title(emojis.SETTINGS, 'Настройки')}\n\n"
        "Выбери язык:",
        reply_markup=get_settings_menu()
    )


@dp.message(F.text == "🇷🇺 Русский")
async def set_ru_handler(message: Message):
    set_user_language(message.from_user.id, "ru")

    await message.answer(
        success("Язык изменён на русский."),
        reply_markup=get_main_menu()
    )


@dp.message(F.text == "🇬🇧 English")
async def set_en_handler(message: Message):
    set_user_language(message.from_user.id, "en")

    await message.answer(
        success("Language changed to English."),
        reply_markup=get_main_menu()
    )


@dp.message(F.text == "🔙 Назад")
async def back_handler(message: Message):
    await message.answer(
        "Главное меню.",
        reply_markup=get_main_menu()
    )