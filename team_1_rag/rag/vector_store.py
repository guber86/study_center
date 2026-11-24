
import numpy as np
from pathlib import Path


def save_index(chunks, embeddings, index_dir):
    """Сохраняет чанки и векторы на диск."""
    index_dir = Path(index_dir)
    index_dir.mkdir(parents=True, exist_ok=True)

    np.save(index_dir / "embeddings.npy", embeddings)

    with open(index_dir / "chunks.txt", "w", encoding="utf-8") as file:
        for chunk in chunks:
            file.write(chunk + "\n")

    print("Индекс успешно сохранён!")
    print("Количество записей:", len(chunks))


def load_index(index_dir):
    """Загружает сохранённые чанки и векторы."""
    index_dir = Path(index_dir)

    embeddings = np.load(index_dir / "embeddings.npy")

    with open(index_dir / "chunks.txt", "r", encoding="utf-8") as file:
        chunks = [line.strip() for line in file if line.strip()]

    return chunks, embeddings
