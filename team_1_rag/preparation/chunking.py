from pathlib import Path


def load_text(file_path):
    """Загружает исходный текст из файла."""
    return Path(file_path).read_text(encoding="utf-8")


def clean_text(text):
    """Очищает текст от пустых строк и лишних пробелов."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def split_into_chunks(text):
    """Разделяет текст на отдельные фрагменты по строкам."""
    return [line for line in text.splitlines() if line.strip()]