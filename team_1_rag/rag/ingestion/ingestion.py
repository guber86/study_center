from prepare_text import load_text

from team_1_rag.preparation.chunking import (
    clean_text,
    split_into_chunks,
)
from team_1_rag.rag.ingestion.embedder import get_vectors
from team_1_rag.rag.ingestion.repository import save


def main():
    content = load_text()
    cleaned = clean_text(content)
    chunks = split_into_chunks(cleaned)

    if not chunks:
        raise ValueError("Нет текста для индексирования")

    vectors = get_vectors(chunks)
    save(vectors)
    print("Сохранено фрагментов:", len(vectors))


if __name__ == "__main__":
    main()