from pathlib import Path

from embeddings import load_model, create_embeddings
from vector_store import load_index


def create_query_embedding(query, model):
    """Преобразует вопрос пользователя в вектор."""
    return create_embeddings([query], model)


if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parents[1]
    index_dir = project_dir / "index"

    # Загружаем сохранённый индекс
    chunks, embeddings = load_index(index_dir)

    # Загружаем ту же embedding-модель
    model = load_model()

    query = "Сколько стоит обучение Python?"
    query_embedding = create_query_embedding(query, model)

    print("Форма вектора вопроса:", query_embedding.shape)
    print("Количество текстовых чанков:", len(chunks))
    print("Размерность векторов индекса:", embeddings.shape[1])
    print(
        "Размерности совпадают:",
        query_embedding.shape[1] == embeddings.shape[1]
    )
