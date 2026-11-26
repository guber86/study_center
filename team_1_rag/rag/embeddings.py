
from pathlib import Path
from sentence_transformers import SentenceTransformer

from vector_store import save_index, load_index


MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"


def load_model():
    """Загружает модель для создания embeddings."""
    return SentenceTransformer(MODEL_NAME)


def create_embeddings(chunks, model):
    """Преобразует текстовые чанки в векторы."""
    return model.encode(chunks, convert_to_numpy=True)

if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parents[1]

    # Добавляем путь к папке rag для импорта vector_store
    import sys
    sys.path.insert(0, str(project_dir / "rag"))

    # Импортируем функции подготовки текста
    sys.path.insert(0, str(project_dir))
    from preparation.chunking import load_text, clean_text, split_into_chunks

    source_path = project_dir / "source" / "source.txt"
    index_dir = project_dir / "index"

    # Подготавливаем текст
    text = load_text(source_path)
    cleaned_text = clean_text(text)
    chunks = split_into_chunks(cleaned_text, chunk_size=1)

    # Создаём векторы
    model = load_model()
    embeddings = create_embeddings(chunks, model)

    print("Количество чанков:", len(chunks))
    print("Форма матрицы векторов:", embeddings.shape)

    # Сохраняем индекс
    save_index(chunks, embeddings, index_dir)

    # Проверяем повторную загрузку
    loaded_chunks, loaded_embeddings = load_index(index_dir)

    print("\nПроверка загрузки индекса:")
    print("Загружено чанков:", len(loaded_chunks))
    print("Форма загруженных векторов:", loaded_embeddings.shape)
