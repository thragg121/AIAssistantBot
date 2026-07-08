from aiogram import F
from aiogram.types import Message

from bot import dp
from app.keyboards.menu import get_main_menu
from app.services.ai_service import disable_ai_mode


@dp.message(F.text == "🔙 Выйти из AI")
async def exit_ai_handler(message: Message):
    disable_ai_mode(message.from_user.id)

    await message.answer(
        "AI-режим выключен.",
        reply_markup=get_main_menu()
    )