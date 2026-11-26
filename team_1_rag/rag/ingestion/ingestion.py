from pathlib import Path

from team_1_rag.preparation.chunking import (
    load_text,
    clean_text,
    split_into_chunks,
)
from team_1_rag.rag.ingestion.embedder import get_vectors
from team_1_rag.rag.ingestion.repository import save


SOURCE_PATH = Path(__file__).resolve().parents[2] / "source" / "source.txt"


def main():
    content = load_text(SOURCE_PATH)
    cleaned = clean_text(content)
    chunks = split_into_chunks(cleaned)

    if not chunks:
        raise ValueError("Нет текста для индексирования")

    vectors = get_vectors(chunks)
    save(vectors)
    print("Сохранено фрагментов:", len(vectors))


if __name__ == "__main__":
    main()