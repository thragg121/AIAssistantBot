from aiogram import F
from aiogram.types import Message

from bot import dp
from app.services.ai_service import (
    get_ai_answer,
    is_ai_mode_enabled
)
from app.services.user_service import can_use_ai


@dp.message(F.text)
async def ai_message_handler(message: Message):
    if not is_ai_mode_enabled(message.from_user.id):
        await message.answer(
            "Я не понял сообщение.\n\n"
            "Используй меню или напиши /start."
        )
        return

    if not can_use_ai(message.from_user.id):
        await message.answer(
            "❌ Лимит бесплатных AI-сообщений закончился.\n\n"
            "В будущем здесь будет подключение подписки."
        )
        return

    answer = get_ai_answer(
        user_id=message.from_user.id,
        text=message.text
    )

    await message.answer(answer)