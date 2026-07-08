# AI Assistant Telegram Bot

Portfolio-ready Telegram bot built with Python, aiogram and SQLite.

## Features

- AI chat mode
- User registration
- User profile
- Message history
- Clear AI history
- Free AI message limit
- Settings menu
- Admin panel
- User list
- Broadcast messages
- SQLite database
- Environment variables via `.env`
- Clean project architecture

## Tech Stack

- Python
- aiogram
- SQLite
- python-dotenv
- OpenAI-ready architecture

## Project Structure

```text
app/
├── database/
├── handlers/
├── keyboards/
├── llm/
├── services/
├── texts/
└── utils/
```

## Setup

```bash
python -m venv venv
```

```bash
venv\Scripts\activate.bat
```

```bash
python -m pip install -r requirements.txt
```

Create `.env` file:

```env
BOT_TOKEN=your_telegram_bot_token
ADMIN_ID=your_telegram_id
OPENAI_API_KEY=
```

Run bot:

```bash
python main.py
```

## Admin Commands

```text
/users
/broadcast Your message
```

## Notes

OpenAI integration is prepared in the architecture.  
By default, the bot uses a test AI response until an API key and billing are configured.