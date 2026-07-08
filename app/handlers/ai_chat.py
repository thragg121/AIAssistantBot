from aiogram import F
from aiogram.types import Message

from bot import dp
from app.keyboards.menu import get_ai_menu
from app.services.ai_service import enable_ai_mode
from app.ui import emojis
from app.ui.messages import title


@dp.message(F.text == "🤖 AI Чат")
async def ai_chat_handler(message: Message):
    enable_ai_mode(message.from_user.id)

    await message.answer(
        f"{title(emojis.ROBOT, 'AI-режим включён')}\n\n"
        "Напиши любое сообщение, и бот ответит.\n\n"
        "Для выхода нажми кнопку ниже.",
        reply_markup=get_ai_menu()
    )