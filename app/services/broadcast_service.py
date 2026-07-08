from app.database.users import get_all_user_ids


async def send_broadcast(bot, text: str):
    user_ids = get_all_user_ids()

    success = 0
    failed = 0

    for user_id in user_ids:
        try:
            await bot.send_message(chat_id=user_id, text=text)
            success += 1
        except Exception:
            failed += 1

    return success, failed