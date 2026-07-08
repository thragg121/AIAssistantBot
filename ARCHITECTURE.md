# Architecture

## Main Flow

Telegram user
↓
Handler
↓
Service
↓
Database layer
↓
SQLite

## Layers

### Handlers

Handlers receive Telegram events and call services.

They should not contain business logic.

Examples:

- `start.py`
- `profile.py`
- `ai_chat.py`
- `admin.py`

### Services

Services contain business logic.

Examples:

- `user_service.py`
- `ai_service.py`
- `admin_service.py`
- `broadcast_service.py`

### Database

Database layer works only with SQLite.

It should not know anything about Telegram or aiogram.

Examples:

- `database.py`
- `users.py`
- `messages.py`

### Keyboards

Keyboards contain Telegram reply markup.

Examples:

- `menu.py`

### LLM

LLM layer is responsible for external AI providers.

Examples:

- `openai_client.py`

## Rules

- Handler calls Service.
- Service calls Database.
- Database never calls Handler.
- Service never sends Telegram messages directly.
- No tokens in code.
- Configuration goes through `config.py`.
- All secrets must be stored in `.env`.
- Wildcard text handlers must be imported last.

## Future Architecture

Later the database layer can be improved with repositories:

Handler
↓
Service
↓
Repository
↓
SQLite