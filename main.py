import asyncio

import app.handlers.start
import app.handlers.profile
import app.handlers.ai_chat
import app.handlers.exit_ai
import app.handlers.clear_history
import app.handlers.help
import app.handlers.settings
import app.handlers.admin
import app.handlers.ai_messages

from bot import bot, dp
from app.database.database import init_db
from app.utils.logger import logger


async def on_startup():
    init_db()
    logger.info("AI Assistant Bot started")


async def main():
    await on_startup()
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped")