from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message

from bot import dp
from app.services.ai_service import clear_chat_history
from app.ui.messages import success


@dp.message(Command("clear"))
async def clear_history_command_handler(message: Message):
    clear_chat_history(message.from_user.id)

    await message.answer(success("История очищена."))


@dp.message(F.text == "🧹 Очистить историю")
async def clear_history_button_handler(message: Message):
    clear_chat_history(message.from_user.id)

    await message.answer(success("История очищена."))