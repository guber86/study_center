from pathlib import Path


def load_text(file_path):
    """Загружает текст из файла."""
    return Path(file_path).read_text(encoding="utf-8")


def clean_text(text):
    """Удаляет лишние пробелы и пустые строки."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def split_into_chunks(text, chunk_size=2):
    """Разделяет текст на чанки по несколько предложений."""
    sentences = [sentence.strip() for sentence in text.split(".") if sentence.strip()]

    chunks = []
    for i in range(0, len(sentences), chunk_size):
        chunk = ". ".join(sentences[i:i + chunk_size]) + "."
        chunks.append(chunk)

    return chunks


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parents[1]
    source_path = base_dir / "source" / "source.txt"

    text = load_text(source_path)
    cleaned_text = clean_text(text)
    chunks = split_into_chunks(cleaned_text, chunk_size=1)

    print(f"Количество предложений: {len(cleaned_text.splitlines())}")
    print(f"Количество чанков: {len(chunks)}")

    for number, chunk in enumerate(chunks, start=1):
        print(f"\nЧанк {number}: {chunk}")
