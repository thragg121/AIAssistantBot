from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message

from bot import dp
from app.services.help_service import get_help_text


@dp.message(Command("help"))
async def help_command_handler(message: Message):
    await message.answer(get_help_text())


@dp.message(F.text == "ℹ️ Помощь")
async def help_button_handler(message: Message):
    await message.answer(get_help_text())