from aiogram import F
from aiogram.types import Message

from bot import dp
from app.services.profile_service import get_profile_text


@dp.message(F.text == "👤 Профиль")
async def profile_handler(message: Message):
    await message.answer(
        text=get_profile_text(message.from_user.id)
    )