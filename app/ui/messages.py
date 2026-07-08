from app.ui import emojis


def success(text: str) -> str:
    return f"{emojis.SUCCESS} {text}"


def error(text: str) -> str:
    return f"{emojis.ERROR} {text}"


def warning(text: str) -> str:
    return f"{emojis.WARNING} {text}"


def title(icon: str, text: str) -> str:
    return f"{icon} <b>{text}</b>"