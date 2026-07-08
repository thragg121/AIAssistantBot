from aiogram import F
from aiogram.types import Message

from bot import dp
from app.keyboards.menu import get_ai_menu
from app.services.ai_service import enable_ai_mode


@dp.message(F.text == "🤖 AI Чат")
async def ai_chat_handler(message: Message):
    enable_ai_mode(message.from_user.id)

    await message.answer(
        text="🤖 AI-режим включён.\n\nНапиши любое сообщение.",
        reply_markup=get_ai_menu()
    )