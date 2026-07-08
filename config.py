import os

from dotenv import load_dotenv

load_dotenv()


# Telegram
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))


# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# AI
SYSTEM_PROMPT = "You are a helpful AI assistant."
FREE_AI_MESSAGES_LIMIT = 10


# Database
DATABASE_NAME = "database.db"