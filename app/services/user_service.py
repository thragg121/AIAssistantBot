from config import FREE_AI_MESSAGES_LIMIT, ADMIN_ID
from app.database.users import save_user, get_user, get_ai_messages_count


def register_user(user_id: int, first_name: str, username: str | None):
    save_user(user_id, first_name, username)


def get_user_profile(user_id: int):
    return get_user(user_id)


def is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID


def can_use_ai(user_id: int) -> bool:
    if is_admin(user_id):
        return True

    return get_ai_messages_count(user_id) < FREE_AI_MESSAGES_LIMIT