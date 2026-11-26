from pathlib import Path


def load_text(file_path):
    """Загружает исходный текст из файла."""
    return Path(file_path).read_text(encoding="utf-8")
