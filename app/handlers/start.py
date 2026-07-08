from aiogram.filters import CommandStart
from aiogram.types import Message
from config import ADMIN_ID

from bot import dp
from app.keyboards.menu import get_main_menu
from app.services.user_service import register_user
from app.texts.welcome import get_welcome_text


@dp.message(CommandStart())
async def start_handler(message: Message):
    register_user(
        user_id=message.from_user.id,
        first_name=message.from_user.first_name,
        username=message.from_user.username
    )

    await message.answer(
        text=get_welcome_text(message.from_user.first_name),
        reply_markup=get_main_menu(
    is_admin=message.from_user.id == ADMIN_ID
))