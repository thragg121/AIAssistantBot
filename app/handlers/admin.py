from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message

from bot import bot, dp
from config import ADMIN_ID
from app.services.admin_service import get_admin_panel_text, get_users_list_text
from app.services.broadcast_service import send_broadcast
from app.ui.messages import error, success


def is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID


@dp.message(F.text == "🛠 Админ-панель")
async def admin_panel_handler(message: Message):
    if not is_admin(message.from_user.id):
        await message.answer(error("У тебя нет доступа."))
        return

    await message.answer(get_admin_panel_text())


@dp.message(Command("users"))
async def users_handler(message: Message):
    if not is_admin(message.from_user.id):
        await message.answer(error("У тебя нет доступа."))
        return

    await message.answer(get_users_list_text())


@dp.message(Command("broadcast"))
async def broadcast_handler(message: Message):
    if not is_admin(message.from_user.id):
        await message.answer(error("У тебя нет доступа."))
        return

    text = message.text.replace("/broadcast", "").strip()

    if not text:
        await message.answer(
            "Напиши текст после команды:\n"
            "/broadcast Привет всем!"
        )
        return

    success_count, failed_count = await send_broadcast(bot, text)

    await message.answer(
        f"{success('Рассылка завершена.')}\n\n"
        f"✅ Отправлено: {success_count}\n"
        f"❌ Ошибок: {failed_count}"
    )