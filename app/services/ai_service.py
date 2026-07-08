from config import SYSTEM_PROMPT

from app.database.messages import save_message, get_last_messages, clear_messages
from app.database.users import get_ai_mode, set_ai_mode, increment_ai_messages_count


def enable_ai_mode(user_id: int):
    set_ai_mode(user_id, 1)


def disable_ai_mode(user_id: int):
    set_ai_mode(user_id, 0)


def is_ai_mode_enabled(user_id: int) -> bool:
    return get_ai_mode(user_id) == 1


def clear_chat_history(user_id: int):
    clear_messages(user_id)


def build_ai_context(user_id: int):
    history = get_last_messages(user_id, limit=10)

    context = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    for role, text in history:
        context.append({
            "role": role,
            "content": text
        })

    return context


def generate_ai_answer(context: list[dict]) -> str:
    return (
        "🤖 Тестовый AI-ответ.\n\n"
        "Настоящий OpenAI подключим позже."
    )


def get_ai_answer(user_id: int, text: str) -> str:
    save_message(user_id, "user", text)
    increment_ai_messages_count(user_id)

    context = build_ai_context(user_id)
    answer = generate_ai_answer(context)

    save_message(user_id, "assistant", answer)

    return answer